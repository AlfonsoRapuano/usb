from odoo import fields, models


class UsbSaleMacroGroup(models.Model):
    _name = "usb.sale.macro.group"
    
    name = fields.Char("Nome")
    

class UsbSaleGroup(models.Model):
    _name = "usb.sale.group"
    
    name = fields.Char("Nome")
    macro_group_id = fields.Many2one('usb.sale.macro.group', string='Capogruppo')
    

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    
    numero_rate = fields.Integer("Numero Rate Pagamento")
    data_pda = fields.Date("Data PDA")
    data_stato_ordine = fields.Date("Data Stato Ordine")
    agente_id = fields.Many2one('res.partner', string='Agente')
    
    usb_sale_group_id = fields.Many2one('usb.sale.group', string='Gruppo')
    usb_sale_macro_group_id = fields.Many2one('usb.sale.macro.group', string='Capogruppo')
    
    # https://www.odoo.com/it_IT/forum/assistenza-1/how-to-add-a-new-status-in-sale-order-in-odoo-9-110398
    state = fields.Selection([   
        ('draft', 'Preventivo'),
        ('sent', 'Preventivo Inviato'),    
        ('sale', 'Ordine di Vendita'),
        ('pending', 'Pending'),
        ('done', 'Completato'),
        ('cancel', 'Annullato'),
        ('cessato', 'Cessato'),
        ('sospeso', 'Sospeso'),
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    
    
    usb_custom_state = fields.Selection([   
        ('draft', 'Preventivo'),
        ('sent', 'Preventivo Inviato'),    
        ('sale', 'Ordine di Vendita'),
        ('pending', 'Pending'),
        ('done', 'Completato'),
        ('cancel', 'Annullato'),
        ('cessato', 'Cessato'),
        ('sospeso', 'Sospeso'),
    ], string='Status (tecnico)', copy=False, index=True, default='draft')
    
    
    def action_set_cessato(self):
        return self.write({'state': 'cessato'})

    def action_set_sospeso(self):
        return self.write({'state': 'sospeso'})
    
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    

    prog_riga_ordine_USB = fields.Integer()
    id_prodotto_USB = fields.Integer()