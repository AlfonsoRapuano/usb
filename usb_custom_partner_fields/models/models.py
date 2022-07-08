from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger("====== USB Custom Partner Fields ======")


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
    
    '''
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
    '''
    # gdpr1 rinominato in flag_dati_gdpr
    flag_dati_gdpr= fields.Boolean()
    #gdpr2 = fields.Boolean()

    associazione = fields.Boolean()
    anag_da_escludere = fields.Boolean()
    data_ins_canc_newsletter = fields.Date()

    '''
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
    des_attivita = fields.Char(string = "Des. Attività")
    '''    
    des_gruppo_anagrafica = fields.Char()
    des_agente_anagrafica = fields.Char()
   
    
    fatturazione_country_id = fields.Many2one('res.country', string='Nazione Fatturazione')
    
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")]
    )
    
    #attributi nuovi
    
    tipologia_anagrafica = fields.Selection(
        [],
        string = "Tipologia Anagrafica",
    )
    
    nazionalita_anagrafica_fatturazione = fields.Selection(
        [],
        string = "Nazionalità Anagrafica-Fatturazione",
    )

    
    
    # attributi per gli indirizzi sede
    
    indirizzo_sede_legale = fields.Char(string = "Indirizzo Sede Legale")
    cap_sede_legale = fields.Char(string = "Cap Sede Legale")
    citta_sede_legale = fields.Char(string = "Città Sede Legale")
    provincia_sede_legale = fields.Many2one('res.country.state','Provincia Sede Legale')
    regione_sede_legale = fields.Selection(
        [],
        string = "Regione Sede Legale",
    )
    
    indirizzo_sede_operativa = fields.Char(string = "Indirizzo Sede Operativa")
    cap_sede_operativa = fields.Char(string = "Cap Sede Operativa")
    citta_sede_operativa = fields.Char(string = "Città Sede Operativa")
    provincia_sede_operativa = fields.Many2one('res.country.state','Provincia Sede Operativa')
    regione_sede_operativa = fields.Selection(
        [],
        string = "Regione Sede Operativa",
    )
    
    # attributi riferimenti di contatto
    
    telefono_fisso_principale = fields.Char(string = "Telefono Fisso Principale")
    telefono_fisso_2 = fields.Char(string = "Telefono Fisso 2")
    mobile_principale = fields.Char(string = "Mobile Principale")
    mobile_2 = fields.Char(string = "Mobile 2")
    mobile_3 = fields.Char(string = "Mobile 3")
    email_principale = fields.Char(string = "Email Principale")
    email_2 = fields.Char(string = "Email 2")
    email_3 = fields.Char(string = "Email 3")
    pec = fields.Char(string = "Pec")
    
    # attributi rappresentati legali
    
    referente_cognome1 = fields.Char(string = "Referente Cognome 1")
    referente_nome1 = fields.Char(string = "Referente Nome 1")
    data_nascita1 = fields.Date(string = "Data Nascita 1")
    luogo_nascita1 = fields.Char(string = "Luogo nascita 1")
    provincia1 = fields.Many2one('res.country.state','Provincia 1')
    codice_fiscale1 = fields.Char(string = "Codice Fiscale 1", size=16)
    sesso1 = fields.Selection([("M", "M"), ("F", "F")],string = "Sesso 1")
    tipo_documento1 = fields.Selection([],string = "Tipo documento 1")
    numero_documento1 = fields.Char(string = "Numero documento 1")
    data_emissione_documento1 = fields.Date(string = "Data Emissione Documento 1")
    data_scadenza_documento1 = fields.Date(string = "Data Scadenza Documento 1")
    # spostato luogo di emissione documento
    luogo_emissione_documento1 = fields.Char("Luogo emissione documento 1")
    
    referente_cognome2 = fields.Char(string = "Referente Cognome 2")
    referente_nome2 = fields.Char(string = "Referente Nome 2")
    data_nascita2 = fields.Date(string = "Data Nascita 2")
    luogo_nascita2 = fields.Char(string = "Luogo nascita 2")
    provincia2 = fields.Many2one('res.country.state','Provincia 2')
    codice_fiscale2 = fields.Char(string = "Codice Fiscale 2", size=16)
    sesso2 = fields.Selection([("M", "M"), ("F", "F")],string = "Sesso 2")
    tipo_documento2 = fields.Selection([],string = "Tipo documento 2")
    numero_documento2 = fields.Char(string = "Numero documento 2")
    data_emissione_documento2 = fields.Date(string = "Data Emissione Documento 2")
    data_scadenza_documento2 = fields.Date(string = "Data Scadenza Documento 2")
     # spostato luogo di emissione documento
    luogo_emissione_documento2 = fields.Char("Luogo emissione documento 2")
    
    
    # attributi delegato
    
    referente_tecnico_o_delegato_cognome = fields.Char(string = "Referente Tecnico o Delegato Cognome")
    referente_tecnico_o_delegato_nome = fields.Char(string = "Referente Tecnico o Delegato  nome")
    referente_tecnico_o_delegato_cf = fields.Char(string = "Referente Tecnico o Delegato  Codice Fiscale",size=16)
    referente_tecnico_o_delegato_mobile1 = fields.Char(string = "Referente Tecnico o Delegato Mobile")
    
    @api.constrains("cap_sede_legale","cap_sede_operativa")
    def check_cap_sedi(self):
        for partner in self:
            
            if not partner.cap_sede_legale or not partner.cap_sede_operativa:
                # non è obbligatorio
                continue
            
            elif partner.country_id.code == "ES":
                if len(partner.cap_sede_legale) != 5:
                    msg = _("il formato del cap sede legale non corretto deve contenere 5 caratteri")
                    raise ValidationError(msg)
                if len(partner.cap_sede_operativa) != 5:
                    msg = _("il formato del cap sede operativa non corretto deve contenere 5 caratteri")
                    raise ValidationError(msg)
            elif partner.country_id.code == "IT":
                if len(partner.cap_sede_legale) != 5:
                    msg = _("il formato del cap sede legale non corretto deve contenere 5 caratteri")
                    raise ValidationError(msg)
                if len(partner.cap_sede_operativa) != 5:
                    msg = _("il formato del cap sede operativa non corretto deve contenere 5 caratteri")
                    raise ValidationError(msg)

        return True
    
    
    
    
    @api.constrains("referente_tecnico_o_delegato_cf","codice_fiscale1","codice_fiscale2")
    def check_cf(self):
        for partner in self:
            if not partner.referente_tecnico_o_delegato_cf or not partner.codice_fiscale1 or not partner.codice_fiscale2:
                # non è obbligatorio
                continue
            elif partner.country_id.code == "ES":
                if len(partner.referente_tecnico_o_delegato_cf) != 9 or len(partner.codice_fiscale1) != 9 or len(partner.codice_fiscale2) != 9:
                    msg = _("il formato del codice fiscale non corretto deve contenere 9 caratteri")
                    raise ValidationError(msg)
            elif partner.country_id.code == "IT":
                if len(partner.referente_tecnico_o_delegato_cf) != 16 or len(partner.codice_fiscale1) != 16 or len(partner.codice_fiscale2) != 16:
                    msg = _("il formato del codice fiscale non corretto deve contenere 16 caratteri")
                    raise ValidationError(msg)

        return True
    


    @api.onchange("referente_tecnico_o_delegato_cf","codice_fiscale1","codice_fiscale2")
    def _cf_changed(self):
        if self.referente_tecnico_o_delegato_cf:
            self.referente_tecnico_o_delegato_cf = self.referente_tecnico_o_delegato_cf.upper()
        if self.codice_fiscale1:
            self.codice_fiscale1 = self.codice_fiscale1.upper()
        if self.codice_fiscale2:
            self.codice_fiscale2 = self.codice_fiscale2.upper()

    

    
    