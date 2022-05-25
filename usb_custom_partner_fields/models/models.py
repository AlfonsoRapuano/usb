from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    
    id_cliente_USB = fields.Integer()
    vies = fields.Boolean()
    split_payment = fields.Boolean()
    tipo_esenzione = fields.Selection(
        [("N2", "N2"), ("N4", "N4")]
    )
    cig = fields.Char()
    cup = fields.Char()
    nato_il = fields.Date()
    luogo_di_nascita = fields.Char()
    provinca_di_nascita = fields.Many2one('res.country.state')
    
    doc_type = fields.Selection(
        [("passaporto", "Passaporto"), ("cdi", "Carta d'identità"), ("pdg", "Patente di guida")],
        string = "Tipo documento",
    )
    doc_num = fields.Char(string = "Numero documento")
    doc_emesso_il = fields.Date("Emesso il")
    doc_scadenza = fields.Date("Scade il")
    luogo_emissione_documento = fields.Char("Luogo emissione documento")
    
    gdpr1= fields.Boolean()
    gdpr2 = fields.Boolean()

    associazione = fields.Boolean()
    anag_da_escludere = fields.Boolean()
    data_ins_canc_newsletter = fields.Date()

    
    des_categoria_merceologica = fields.Selection(
        [
            ("ALIMENTARI", "ALIMENTARI"), 
            ("SERVIZI", "SERVIZI"), 
            ("VENDITA", "VENDITA"),            
            ("IMPIANTISTICA", "IMPIANTISTICA"),
            ("EDILIZIA", "EDILIZIA"),
            ("SALUTE_E_BENESSERE", "SALUTE E BENESSERE"),           
            ("SPORT_E_HOBBIES", "SPORT E HOBBIES"),            
            ("RISTORAZIONE", "RISTORAZIONE"),
            ("MOTORI", "MOTORI"),
            ("VIAGGI_E_TURISMO", "VIAGGI E TURISMO"),
            ("SERVIZI_DI_CONSULENZA", "SERVIZI DI CONSULENZA"),
            ("ARREDAMENTO", "ARREDAMENTO"),
            ("ISTRUZIONE_E_FORMAZIONE", "ISTRUZIONE E FORMAZIONE"),
            ("PRODUZIONE_E_FORNITURA", "PRODUZIONE E FORNITURA"),
            ("ABBIGLIAMENTO_E_ACCESSORI", "ABBIGLIAMENTO E ACCESSORI"),
        ],
        string = "Des. Categoria Merceologica", 
    )
    des_gruppo_anagrafica = fields.Char()
    des_agente_anagrafica = fields.Char()
    des_attivita = fields.Char(string = "Des. Attività")
    
    country_id = fields.Many2one('res.country', string='Nazione Fatturazione')
    
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")]
    )