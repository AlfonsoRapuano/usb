# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import fields, api, models, _
from odoo.exceptions import UserError

import logging

_logger = logging.getLogger("===== Gesca Update Fields Wizard =====")


class UpdateFieldWizard(models.TransientModel):
    _name = "update.field.wizard"

    sale_order_state = fields.Selection([
        ('null', 'Non aggiornare'),
        ('draft', 'Quotation'),
        ('sale', 'Sales Order'),
        ('cancel', 'Cancelled'),
        ], string='Status', default='null')
    
    
    # GESCA
    # metodo per chiamare le azioni corrispondenti ai vari stati
    def do_corresponding_state_action(self, so):
        # For Excel
        if self.sale_order_state == "sale":
            so.action_confirm()
        elif self.sale_order_state == "cancel":
            _logger.info(so)
            so.action_cancel()
        elif self.sale_order_state == "draft":
            so.action_draft()
            
    
    def apply_changes(self):
        records = self.env[self._context.get('active_model')].browse(self._context.get('active_ids', []))
        if self.sale_order_state != 'null':
            for rec in records:
                self.do_corresponding_state_action(rec)
            