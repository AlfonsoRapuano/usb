from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    
    costo_banca = fields.Float(string="Costo Banca")
    costo_sito = fields.Float(string="Costo Sito")
    costo_seo = fields.Float(string="Costo Seo")
    costo_varie = fields.Float(string="Costo Varie")
    costo_gmb = fields.Float(string="Costo Gmb")
    costo_virtual_tour = fields.Float(string="Costo Virtual Tour")
    costo_social = fields.Float(string="Costo Social")
    costo_adwords = fields.Float(string="Costo Adwords")