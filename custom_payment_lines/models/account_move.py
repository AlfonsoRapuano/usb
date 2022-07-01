# -*- coding: utf-8 -*-
from itertools import chain
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class AccountPaymentTerm(models.Model):
    _inherit= 'account.payment.term'
    
    is_custom_payment_term = fields.Boolean()


class AccountMoveInherit(models.Model):
    _inherit= 'account.move'
    
    custom_payment_line_ids = fields.One2many(
        'custom.payment.line', 'move_id', string='Scadenze',
        copy=True, readonly=False)
    
    payment_method_id = fields.Many2one(
        'account.payment.method', string="Metodo di pagamento")
    
    custom_payment_term = fields.Boolean(related='invoice_payment_term_id.is_custom_payment_term')
    
    @api.onchange('invoice_payment_term_id')
    def _onchange_payment_term_custom_payment(self):
        if not self.invoice_payment_term_id.is_custom_payment_term:
            self.payment_method_id = False
            self.custom_payment_line_ids = False
    
    
    def action_post(self):
        if sum([i.amount_due for i in self.custom_payment_line_ids]) != self.amount_total and self.custom_payment_term:
            raise UserError("Attenzione!L'ammontare delle righe di pagamento non coincide con il totale dell'ordine!")
        return super(AccountMoveInherit, self).action_post()
    
    def _check_balanced(self):
        if self.custom_payment_term:
            return
        else:
            return super(AccountMoveInherit, self)._check_balanced()
    
    def _recompute_payment_terms_lines(self):
        if not self.custom_payment_term:
            super(AccountMoveInherit, self)._recompute_payment_terms_lines()
        else:
            self.ensure_one()
            self = self.with_company(self.company_id)
            in_draft_mode = self != self._origin
            today = fields.Date.context_today(self)
            self = self.with_company(self.journal_id.company_id)
            
            existing_terms_lines = self.line_ids.filtered(lambda line: line.account_id.user_type_id.type in ('receivable', 'payable'))
            others_lines = self.line_ids.filtered(lambda line: line.account_id.user_type_id.type not in ('receivable', 'payable'))
            company_currency_id = (self.company_id or self.env.company).currency_id
            total_balance = sum(others_lines.mapped(lambda l: company_currency_id.round(l.balance)))
            total_amount_currency = sum(others_lines.mapped('amount_currency'))

            if not others_lines:
                self.line_ids -= existing_terms_lines
                return
            
            computation_date = today
            account = self.partner_id.property_account_receivable_id if self.is_sale_document(include_receipts=True) else self.partner_id.property_account_payable_id
            if not account:
                domain = [
                    ('company_id', '=', self.company_id.id),
                    ('internal_type', '=', 'receivable' if self.move_type in ('out_invoice', 'out_refund', 'out_receipt') else 'payable'),
                ]
                account = self.env['account.account'].search(domain, limit=1)
                
                
            def _compute_custom_payment_terms(self, computation_date, total_balance, total_amount_currency):
                # return [("2022-06-28", 1220.0, 1220.0), ("2022-08-27", 1220.0, 1220.0)]
                return [(str(custom_payment_line.date_due), custom_payment_line.amount_due, custom_payment_line.amount_due) for custom_payment_line in self.custom_payment_line_ids]
            
            
            def _compute_diff_payment_terms_lines(self, existing_terms_lines, account, to_compute):
                ''' Process the result of the '_compute_payment_terms' method and creates/updates corresponding invoice lines.
                :param self:                    The current account.move record.
                :param existing_terms_lines:    The current payment terms lines.
                :param account:                 The account.account record returned by '_get_payment_terms_account'.
                :param to_compute:              The list returned by '_compute_payment_terms'.
                '''
                # As we try to update existing lines, sort them by due date.
                existing_terms_lines = existing_terms_lines.sorted(lambda line: line.date_maturity or today)
                existing_terms_lines_index = 0

                # Recompute amls: update existing line or create new one for each payment term.
                new_terms_lines = self.env['account.move.line']
                for date_maturity, balance, amount_currency in to_compute:
                    currency = self.journal_id.company_id.currency_id
                    if currency and currency.is_zero(balance) and len(to_compute) > 1:
                        continue

                    if existing_terms_lines_index < len(existing_terms_lines):
                        # Update existing line.
                        candidate = existing_terms_lines[existing_terms_lines_index]
                        existing_terms_lines_index += 1
                        candidate.update({
                            'date_maturity': date_maturity,
                            #'amount_currency': -amount_currency,
                            'debit': balance < 0.0 and -balance or 0.0,
                            'credit': balance > 0.0 and balance or 0.0,
                        })
                    else:
                        # Create new line.
                        create_method = in_draft_mode and self.env['account.move.line'].new or self.env['account.move.line'].create
                        candidate = create_method({
                            'name': self.payment_reference or '',
                            'debit': balance < 0.0 and -balance or 0.0,
                            'credit': balance > 0.0 and balance or 0.0,
                            'quantity': 1.0,
                            #'amount_currency': -amount_currency,
                            'date_maturity': date_maturity,
                            'move_id': self.id,
                            'currency_id': self.currency_id.id,
                            'account_id': account.id,
                            'partner_id': self.commercial_partner_id.id,
                            'exclude_from_invoice_tab': True,
                        })
                    new_terms_lines += candidate
                    if in_draft_mode:
                        candidate.update(candidate._get_fields_onchange_balance(force_computation=True))
                return new_terms_lines
        
            
            to_compute = _compute_custom_payment_terms(self, computation_date, total_balance, total_amount_currency)
            new_terms_lines = _compute_diff_payment_terms_lines(self, existing_terms_lines, account, to_compute)

            # Remove old terms lines that are no longer needed.
            self.line_ids -= existing_terms_lines - new_terms_lines

            if new_terms_lines:
                self.payment_reference = new_terms_lines[-1].name or ''
                
                
class CustomPaymentLine(models.Model):
    _name = "custom.payment.line"
    _description = "Payment Line"
    
    move_id = fields.Many2one('account.move', string='Invoice Reference',
        ondelete='cascade', index=True)
    amount_due = fields.Monetary(string='Importo Pagamento', currency_field='company_currency_id',
        store=True)
    date_due = fields.Date(string='Scadenza', index=True, copy=False,
        help="Questo campo riguarda la possibilità di impostare una scadenza.", required=True)
    company_currency_id = fields.Many2one('res.currency', related='move_id.company_currency_id', readonly=True, related_sudo=False)
    payment_type = fields.Selection([ ('partial', 'Importo parziale'),('balance', 'Saldo'),],'Tipologia dovuto', default='partial')
    #percentage = fields.Float(string='Percentuale')
    payment_method_id = fields.Many2one(
        'account.payment.method', string="Metodo di pagamento", related = 'move_id.payment_method_id')
    
    
    @api.model
    def create(self, vals):
        res = super(CustomPaymentLine, self).create(vals)
        if res.move_id.custom_payment_term:
            res.move_id._recompute_payment_terms_lines()
        return res
    
    
    
    def write(self, values):
        res = super(CustomPaymentLine, self).write(values)
        # here you can do accordingly
        if self.move_id.custom_payment_term:
            self.move_id._recompute_payment_terms_lines()
        return res
    
    
    @api.onchange('payment_type')
    def _onchange_payment_type(self):
        lines_amount = sum([i.amount_due for i in self.move_id.custom_payment_line_ids]) 
        if self.payment_type == 'balance':
            self.amount_due = self.move_id.amount_total - lines_amount
            
        
# ereditiamo account.move.line per permettere di aggiungere un campo relativo al metodo di pagamento, derivante da quello messo nella fattura
# in questo modo, sarà poi possibile raggruppare e filtrare per metodo di pagamento
class AccountMoveLineInherit(models.Model):
    _inherit= 'account.move.line'
    
    stored_payment_method_id = fields.Char(compute='_compute_payment_method_id',
        string='Metodo di pagamento', store = True)
    
    @api.depends('move_id')
    def _compute_payment_method_id(self):
        for line in self:
            if line.move_id.payment_method_id:
                line.stored_payment_method_id = line.move_id.payment_method_id.display_name
            else:
                line.stored_payment_method_id = "Non definito"