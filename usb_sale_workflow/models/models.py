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
    
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    

    prog_riga_ordine_USB = fields.Integer()
    id_prodotto_USB = fields.Integer()