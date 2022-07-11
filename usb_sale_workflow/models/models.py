from odoo import fields, models, api
from odoo.exceptions import UserError

import logging
_logger = logging.getLogger("===== USB Sale Workflow =====")

# interviste facebook
class IntervistaFacebook(models.Model):
    _name = "intervista.facebook"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    url_pagina_facebook = fields.Char()
    nome_pagina_facebook = fields.Char()
    informazioni_grafiche = fields.Char()
    indicazione_contenuti = fields.Char()
    raggio_sponsorizzate = fields.Char()
    target = fields.Char()
    account_bm_facebook = fields.Char()
    user_facebook = fields.Char()
    pw_facebook = fields.Char()
    

# interviste instagram
class IntervistaInstagram(models.Model):
    _name = "intervista.instagram"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    url_pagina_instagram = fields.Char()
    nome_pagina_instagram = fields.Char()
    user_instagram = fields.Char()
    password_instagram = fields.Char()

# interviste virtual tour
class IntervistaVirtualTour(models.Model):
    _name = "intervista.virtual.tour"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    url_inserimento_virtual = fields.Char()
    tipo_prodotto_inserimento_virtual = fields.Char()
    

# interviste landing
class IntervistaLanding(models.Model):
    _name = "intervista.landing"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    dominio_cliente_ftp = fields.Char()
    dominio_acquistato = fields.Char()
    dominio_stock = fields.Char()
    descrizione_attivita = fields.Char()
    grafica_e_contenuti = fields.Char()
    nomi_mail_scelte = fields.Char()
    tipologia_sito = fields.Char()
    numero_plugin_whatsapp = fields.Integer()
    numero_plugin_facebook = fields.Integer()
    credenziali_plugin_messenger = fields.Char()
    hosting_user = fields.Char()
    hosting_pw = fields.Char()
    hosting_url = fields.Char()
    ftp_host = fields.Char()
    ftp_user = fields.Char()
    ftp_pw = fields.Char()
    cms_cliente_url = fields.Char()
    cms_cliente_user = fields.Char()
    cms_cliente_pw = fields.Char()
    database_nome = fields.Char()
    database_user = fields.Char()
    database_pw = fields.Char()
    database_host = fields.Char()
    database_url = fields.Char()
    hosting = fields.Char()
    elenco_server = fields.Char()
    account_server_user = fields.Char()
    account_server_pw = fields.Char()
    account_db_username = fields.Char()
    account_db_host = fields.Char()
    cms_url = fields.Char()
    cms_user = fields.Char()
    cms_pw = fields.Char()
    user_console = fields.Char()
    pw_console = fields.Char()
    user_analytics = fields.Char()
    pw_analytics = fields.Char()
    user_email = fields.Char()
    

# interviste sito
class IntervistaEcommerce(models.Model):
    _name = "intervista.ecommerce"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    dominio_cliente_ftp = fields.Char()
    dominio_acquistato = fields.Char()
    dominio_stock = fields.Char()
    descrizione_attivita = fields.Char()
    grafica_e_contenuti = fields.Char()
    nomi_mail_scelte = fields.Char()
    tipologia_sito = fields.Char()
    numero_plugin_whatsapp = fields.Integer()
    numero_plugin_facebook = fields.Integer()
    credenziali_plugin_messenger = fields.Char()
    hosting_user = fields.Char()
    hosting_pw = fields.Char()
    hosting_url = fields.Char()
    ftp_host = fields.Char()
    ftp_user = fields.Char()
    ftp_pw = fields.Char()
    cms_cliente_url = fields.Char()
    cms_cliente_user = fields.Char()
    cms_cliente_pw = fields.Char()
    database_nome = fields.Char()
    database_user = fields.Char()
    database_pw = fields.Char()
    database_host = fields.Char()
    database_url = fields.Char()
    hosting = fields.Char()
    elenco_server = fields.Char()
    account_server_user = fields.Char()
    account_server_pw = fields.Char()
    account_db_username = fields.Char()
    account_db_host = fields.Char()
    cms_url = fields.Char()
    cms_user = fields.Char()
    cms_pw = fields.Char()
    user_console = fields.Char()
    pw_console = fields.Char()
    user_analytics = fields.Char()
    pw_analytics = fields.Char()
    user_email = fields.Char()

# interviste seo
class IntervistaSeo(models.Model):
    _name = "intervista.seo"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    keywords_suggerite_cliente = fields.Char()
    keywords_utilizzate = fields.Char()
    keywords_rinnovo = fields.Char()

# interviste sito
class IntervistaSito(models.Model):
    _name = "intervista.sito"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    dominio_cliente_ftp = fields.Char()
    dominio_acquistato = fields.Char()
    dominio_stock = fields.Char()
    descrizione_attivita = fields.Char()
    grafica_e_contenuti = fields.Char()
    nomi_mail_scelte = fields.Char()
    tipologia_sito = fields.Char()
    numero_plugin_whatsapp = fields.Integer()
    numero_plugin_facebook = fields.Integer()
    credenziali_plugin_messenger = fields.Char()
    hosting_user = fields.Char()
    hosting_pw = fields.Char()
    hosting_url = fields.Char()
    ftp_host = fields.Char()
    ftp_user = fields.Char()
    ftp_pw = fields.Char()
    cms_cliente_url = fields.Char()
    cms_cliente_user = fields.Char()
    cms_cliente_pw = fields.Char()
    database_nome = fields.Char()
    database_user = fields.Char()
    database_pw = fields.Char()
    database_host = fields.Char()
    database_url = fields.Char()
    hosting = fields.Char()
    elenco_server = fields.Char()
    account_server_user = fields.Char()
    account_server_pw = fields.Char()
    account_db_username = fields.Char()
    account_db_host = fields.Char()
    cms_url = fields.Char()
    cms_user = fields.Char()
    cms_pw = fields.Char()
    user_console = fields.Char()
    pw_console = fields.Char()
    user_analytics = fields.Char()
    pw_analytics = fields.Char()
    user_email = fields.Char()
    
    
# interviste portale
class IntervistaPortale(models.Model):
    _name = "intervista.portale"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    regione_portale = fields.Char()
    servizi_portale = fields.Char()
    link_da_inserire_portale = fields.Char()

# interviste ads
class IntervistaAds(models.Model):
    _name = "intervista.ads"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    nome_attività_ads = fields.Char()
    url_di_appoggio_ads = fields.Char()
    nr_di_telefono_ads = fields.Char()
    raggio_di_azione_ads = fields.Char()
    categoria_merceologica_ads = fields.Char()
    data_partenza_programmata_ads = fields.Date()
    keywords_suggerite_dal_cliente_ads = fields.Char()
    keywords_utilizzate_ads = fields.Char()
    keywords_rinnovo_ads = fields.Char()
    user_gmail_per_ads = fields.Date()
    pw_gmail_per_ads = fields.Char()
    
# interviste gmb
class IntervistaGMB(models.Model):
    _name = "intervista.gmb"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    email_cliente_proprietaria = fields.Char()
    nome_pagina = fields.Char()
    indirizzo_gmb = fields.Char()
    categoria_merceologica_attività_GMB = fields.Char()
    visibilità_indirizzo = fields.Char()
    orari_attività = fields.Char()
    telefono = fields.Char()
    cellulare = fields.Char()
    email_attività = fields.Char()
    sito_web = fields.Char()
    descrizione = fields.Char()
    note_GMB = fields.Char()
    servizi_GMB = fields.Char()
    link_da_inserire_GMB = fields.Char()
    gmail_gmb_proprietaria_cliente = fields.Char()
    user_gmail_gmb = fields.Char()
    pw_gmail_per_gmb = fields.Char()
    
# tipologie di link
class UsbLinkType(models.Model):
    _name = "usb.link.type"
    
    sale_id = fields.Many2one('sale.order', string='Ordine di Vendita',
        ondelete='cascade', index=True)
    
    link_gmb = fields.Char("LINK GMB")
    link_facebook = fields.Char("LINK FACEBOOK")
    link_instagram = fields.Char("LINK INSTAGRAM")
    link_virtual_tour = fields.Char("LINK VIRTUAL TOUR")
    link_portale_regionale = fields.Char("LINK PORTALE REGIONALE")
    
    link_landing_page = fields.Char("LINK LANDING PAGE")
    dominio_proprieta_cliente_landing_page = fields.Boolean("DOMINIO PROPRIETA' DEL CLIENTE")
    data_acquisto_dominio_landing_page = fields.Date("DATA ACQUISTO DOMINIO")
    
    link_sito = fields.Char("LINK SITO")
    dominio_proprieta_cliente_sito = fields.Boolean("DOMINIO PROPRIETA' DEL CLIENTE")
    data_acquisto_dominio_sito = fields.Date("DATA ACQUISTO DOMINIO")
    
    link_ecommerce = fields.Char("LINK ECOMMERCE")
    dominio_proprieta_cliente_ecommerce = fields.Boolean("DOMINIO PROPRIETA' DEL CLIENTE")
    data_acquisto_dominio_ecommerce = fields.Date("DATA ACQUISTO DOMINIO")
    
    link_article_marketing_seo = fields.Char("LINK ARTICLE MARKETING SEO")
    provider_article = fields.Char("PROVIDER ARTICLE")
    
    project_id = fields.Many2one('project.project', string='Progetto')

    
    
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
    
    
    # altri attributi sugli ordini
    data_richiesta_disdetta = fields.Date()
    data_disdetta_prenotata = fields.Date()
    disdetta_prenotata = fields.Boolean()
    tacito_rinnovo = fields.Boolean()
    semaforo = fields.Selection([
        ('giallo', 'Giallo'),
        ('verde', 'Verde'),
        ('rosso', 'Rosso')], string='Semaforo',
        copy=False, default='giallo',)
    note_semaforo = fields.Text()

    
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
    
    
    # tipi di link da associare
    usb_link_type_ids = fields.One2many(
        'usb.link.type', 'sale_id', string='Tipologia Link',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|',('link_gmb', '!=', False), ('link_facebook', '!=', False), \
                                                        ('link_instagram', '!=', False),('link_virtual_tour', '!=', False),('link_portale_regionale', '!=', False),])
    usb_link_type_ids_2 = fields.One2many(
        'usb.link.type', 'sale_id', string='Tipologia Link',
        copy=False, readonly=False, domain=lambda self: ['|','|',('link_landing_page', '!=', False), ('dominio_proprieta_cliente_landing_page', '!=', False), \
                                                        ('data_acquisto_dominio_landing_page', '!=', False),])
    usb_link_type_ids_3 = fields.One2many(
        'usb.link.type', 'sale_id', string='Tipologia Link',
        copy=False, readonly=False, domain=lambda self: ['|','|',('link_sito', '!=', False), ('dominio_proprieta_cliente_sito', '!=', False), \
                                                        ('data_acquisto_dominio_sito', '!=', False),])
    usb_link_type_ids_4 = fields.One2many(
        'usb.link.type', 'sale_id', string='Tipologia Link',
        copy=False, readonly=False, domain=lambda self: ['|','|',('link_ecommerce', '!=', False), ('dominio_proprieta_cliente_ecommerce', '!=', False), \
                                                        ('data_acquisto_dominio_ecommerce', '!=', False),])
    usb_link_type_ids_5 = fields.One2many(
        'usb.link.type', 'sale_id', string='Tipologia Link',
        copy=False, readonly=False, domain=lambda self: ['|',('link_article_marketing_seo', '!=', False), ('provider_article', '!=', False)])
    
    
    # interviste gmb
    interviste_gmb_ids = fields.One2many(
        'intervista.gmb', 'sale_id', string='Intervista GMB',
        copy=False, readonly=False, domain=lambda self: ['|','|',('email_cliente_proprietaria', '!=', False), ('nome_pagina', '!=', False), \
                                                        ('indirizzo_gmb', '!=', False)])
    interviste_gmb_ids_2 = fields.One2many(
        'intervista.gmb', 'sale_id', string='Intervista GMB',
        copy=False, readonly=False, domain=lambda self: [('categoria_merceologica_attività_GMB', '!=', False)])
    interviste_gmb_ids_3 = fields.One2many(
        'intervista.gmb', 'sale_id', string='Intervista GMB',
        copy=False, readonly=False, domain=lambda self: ['|','|',('gmail_gmb_proprietaria_cliente', '!=', False), ('user_gmail_gmb', '!=', False), \
                                                        ('pw_gmail_per_gmb', '!=', False)])
    
    
    # interviste ads
    interviste_ads_ids = fields.One2many(
        'intervista.ads', 'sale_id', string='Intervista ADS',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|',('nome_attività_ads', '!=', False), ('url_di_appoggio_ads', '!=', False), \
                                   ('nr_di_telefono_ads', '!=', False), ('raggio_di_azione_ads', '!=', False), ('categoria_merceologica_ads', '!=', False),('data_partenza_programmata_ads', '!=', False)])
    interviste_ads_ids_2 = fields.One2many(
        'intervista.ads', 'sale_id', string='Intervista ADS (2)',
        copy=False, readonly=False, domain=lambda self: ['|','|',('keywords_suggerite_dal_cliente_ads', '!=', False), ('keywords_utilizzate_ads', '!=', False), \
                                                        ('keywords_rinnovo_ads', '!=', False)])
    interviste_ads_ids_3 = fields.One2many(
        'intervista.ads', 'sale_id', string='Intervista ADS (3)',
        copy=False, readonly=False, domain=lambda self: ['|',('user_gmail_per_ads', '!=', False), ('pw_gmail_per_ads', '!=', False)])
    
    
    # interviste portale
    interviste_portale_ids = fields.One2many(
        'intervista.portale', 'sale_id', string='Interviste Portale',
        copy=False, readonly=False)
    
    
    # interviste sito
    interviste_sito_ids = fields.One2many(
        'intervista.sito', 'sale_id', string='Interviste Sito',
        copy=False, readonly=False, domain=lambda self: ['|','|',('dominio_cliente_ftp', '!=', False), ('dominio_acquistato', '!=', False), \
                                                        ('dominio_stock', '!=', False)])
    interviste_sito_ids_2 = fields.One2many(
        'intervista.sito', 'sale_id', string='Interviste Sito (2)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|',('descrizione_attivita', '!=', False), ('grafica_e_contenuti', '!=', False), \
                                                        ('nomi_mail_scelte', '!=', False), ('descrizione_attivita', '!=', False), ('tipologia_sito', '!=', False)])
    interviste_sito_ids_3 = fields.One2many(
        'intervista.sito', 'sale_id', string='Interviste Sito (3)',
        copy=False, readonly=False, domain=lambda self: ['|','|',('numero_plugin_whatsapp', '!=', False), ('numero_plugin_facebook', '!=', False), \
                                                        ('credenziali_plugin_messenger', '!=', False)])
    interviste_sito_ids_4 = fields.One2many(
        'intervista.sito', 'sale_id', string='Interviste Sito (4)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|','|','|','|','|','|','|','|','|',('hosting_user', '!=', False), ('hosting_pw', '!=', False), \
                                                        ('hosting_url', '!=', False),('ftp_host', '!=', False), ('ftp_user', '!=', False), ('ftp_pw', '!=', False), \
                                                        ('cms_cliente_url', '!=', False) , ('cms_cliente_user', '!=', False) ,('cms_cliente_pw', '!=', False) ,('database_nome', '!=', False), \
                                                         ('database_user', '!=', False) ,('database_pw', '!=', False) ,('database_host', '!=', False) ,('database_url', '!=', False) ])
    interviste_sito_ids_5 = fields.One2many(
        'intervista.sito', 'sale_id', string='Interviste Sito (5)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|','|','|','|',('hosting', '!=', False), ('elenco_server', '!=', False), \
                                                        ('account_server_user', '!=', False),('account_server_pw', '!=', False), ('account_db_username', '!=', False), ('account_db_host', '!=', False), \
                                                        ('cms_url', '!=', False) , ('cms_user', '!=', False) ,('cms_pw', '!=', False) ])
    interviste_sito_ids_6 = fields.One2many(
        'intervista.sito', 'sale_id', string='Interviste Sito (6)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|',('user_console', '!=', False), ('pw_console', '!=', False), \
                                                        ('user_analytics', '!=', False), ('pw_analytics', '!=', False)])
    interviste_sito_ids_7 = fields.One2many(
        'intervista.sito', 'sale_id', string='Interviste Sito (7)',
        copy=False, readonly=False, domain=lambda self: [('user_email', '!=', False)])
    
    
    
    
    # interviste seo
    interviste_seo_ids = fields.One2many(
        'intervista.seo', 'sale_id', string='Interviste Seo',
        copy=False, readonly=False)
    
    
    
    
    # interviste ecommerce
    interviste_ecommerce_ids = fields.One2many(
        'intervista.ecommerce', 'sale_id', string='Interviste ecommerce',
        copy=False, readonly=False, domain=lambda self: ['|','|',('dominio_cliente_ftp', '!=', False), ('dominio_acquistato', '!=', False), \
                                                        ('dominio_stock', '!=', False)])
    interviste_ecommerce_ids_2 = fields.One2many(
        'intervista.ecommerce', 'sale_id', string='Interviste ecommerce (2)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|',('descrizione_attivita', '!=', False), ('grafica_e_contenuti', '!=', False), \
                                                        ('nomi_mail_scelte', '!=', False), ('descrizione_attivita', '!=', False), ('tipologia_sito', '!=', False)])
    interviste_ecommerce_ids_3 = fields.One2many(
        'intervista.ecommerce', 'sale_id', string='Interviste ecommerce (3)',
        copy=False, readonly=False, domain=lambda self: ['|','|',('numero_plugin_whatsapp', '!=', False), ('numero_plugin_facebook', '!=', False), \
                                                        ('credenziali_plugin_messenger', '!=', False)])
    interviste_ecommerce_ids_4 = fields.One2many(
        'intervista.ecommerce', 'sale_id', string='Interviste ecommerce (4)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|','|','|','|','|','|','|','|','|',('hosting_user', '!=', False), ('hosting_pw', '!=', False), \
                                                        ('hosting_url', '!=', False),('ftp_host', '!=', False), ('ftp_user', '!=', False), ('ftp_pw', '!=', False), \
                                                        ('cms_cliente_url', '!=', False) , ('cms_cliente_user', '!=', False) ,('cms_cliente_pw', '!=', False) ,('database_nome', '!=', False), \
                                                         ('database_user', '!=', False) ,('database_pw', '!=', False) ,('database_host', '!=', False) ,('database_url', '!=', False) ])
    interviste_ecommerce_ids_5 = fields.One2many(
        'intervista.ecommerce', 'sale_id', string='Interviste ecommerce (5)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|','|','|','|',('hosting', '!=', False), ('elenco_server', '!=', False), \
                                                        ('account_server_user', '!=', False),('account_server_pw', '!=', False), ('account_db_username', '!=', False), ('account_db_host', '!=', False), \
                                                        ('cms_url', '!=', False) , ('cms_user', '!=', False) ,('cms_pw', '!=', False) ])
    interviste_ecommerce_ids_6 = fields.One2many(
        'intervista.ecommerce', 'sale_id', string='Interviste ecommerce (6)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|',('user_console', '!=', False), ('pw_console', '!=', False), \
                                                        ('user_analytics', '!=', False), ('pw_analytics', '!=', False)])
    interviste_ecommerce_ids_7 = fields.One2many(
        'intervista.ecommerce', 'sale_id', string='Interviste ecommerce (7)',
        copy=False, readonly=False, domain=lambda self: [('user_email', '!=', False)])
    
    
    
    
    
    # interviste landing
    interviste_landing_ids = fields.One2many(
        'intervista.landing', 'sale_id', string='Interviste landing',
        copy=False, readonly=False, domain=lambda self: ['|','|',('dominio_cliente_ftp', '!=', False), ('dominio_acquistato', '!=', False), \
                                                        ('dominio_stock', '!=', False)])
    interviste_landing_ids_2 = fields.One2many(
        'intervista.landing', 'sale_id', string='Interviste landing (2)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|',('descrizione_attivita', '!=', False), ('grafica_e_contenuti', '!=', False), \
                                                        ('nomi_mail_scelte', '!=', False), ('descrizione_attivita', '!=', False), ('tipologia_sito', '!=', False)])
    interviste_landing_ids_3 = fields.One2many(
        'intervista.landing', 'sale_id', string='Interviste landing (3)',
        copy=False, readonly=False, domain=lambda self: ['|','|',('numero_plugin_whatsapp', '!=', False), ('numero_plugin_facebook', '!=', False), \
                                                        ('credenziali_plugin_messenger', '!=', False)])
    interviste_landing_ids_4 = fields.One2many(
        'intervista.landing', 'sale_id', string='Interviste landing (4)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|','|','|','|','|','|','|','|','|',('hosting_user', '!=', False), ('hosting_pw', '!=', False), \
                                                        ('hosting_url', '!=', False),('ftp_host', '!=', False), ('ftp_user', '!=', False), ('ftp_pw', '!=', False), \
                                                        ('cms_cliente_url', '!=', False) , ('cms_cliente_user', '!=', False) ,('cms_cliente_pw', '!=', False) ,('database_nome', '!=', False), \
                                                         ('database_user', '!=', False) ,('database_pw', '!=', False) ,('database_host', '!=', False) ,('database_url', '!=', False) ])
    interviste_landing_ids_5 = fields.One2many(
        'intervista.landing', 'sale_id', string='Interviste landing (5)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|','|','|','|',('hosting', '!=', False), ('elenco_server', '!=', False), \
                                                        ('account_server_user', '!=', False),('account_server_pw', '!=', False), ('account_db_username', '!=', False), ('account_db_host', '!=', False), \
                                                        ('cms_url', '!=', False) , ('cms_user', '!=', False) ,('cms_pw', '!=', False) ])
    interviste_landing_ids_6 = fields.One2many(
        'intervista.landing', 'sale_id', string='Interviste landing (6)',
        copy=False, readonly=False, domain=lambda self: ['|','|','|',('user_console', '!=', False), ('pw_console', '!=', False), \
                                                        ('user_analytics', '!=', False), ('pw_analytics', '!=', False)])
    interviste_landing_ids_7 = fields.One2many(
        'intervista.landing', 'sale_id', string='Interviste landing (7)',
        copy=False, readonly=False, domain=lambda self: [('user_email', '!=', False)])
    
    
    # interviste virtual tour
    interviste_virtual_tour_ids = fields.One2many(
        'intervista.virtual.tour', 'sale_id', string='Interviste Virtual Tour',
        copy=False, readonly=False)
    
    
    # interviste instagram
    interviste_instagram_ids = fields.One2many(
        'intervista.instagram', 'sale_id', string='Interviste Instagram',
        copy=False, readonly=False)
    
    
    # interviste facebook
    interviste_facebook_ids = fields.One2many(
        'intervista.facebook', 'sale_id', string='Interviste Facebook',
        copy=False, readonly=False, domain=lambda self: ['|','|','|','|','|',('url_pagina_facebook', '!=', False), ('nome_pagina_facebook', '!=', False), ('informazioni_grafiche', '!=', False), \
                                                        ('indicazione_contenuti', '!=', False), ('raggio_sponsorizzate', '!=', False), ('target', '!=', False)])
    interviste_facebook_ids_2 = fields.One2many(
        'intervista.facebook', 'sale_id', string='Interviste Facebook (2)',
        copy=False, readonly=False, domain=lambda self: ['|','|',('account_bm_facebook', '!=', False), ('user_facebook', '!=', False), ('pw_facebook', '!=', False)])
    
    
    def action_set_cessato(self):
        return self.write({'state': 'cessato'})
    

    def action_set_sospeso(self):
        return self.write({'state': 'sospeso'})
    
    
    def write(self, values):
        res = super(SaleOrder, self).write(values)
        # here you can do accordingly    
        for i in values.keys():
            if "ids" in i:
                one2many_data = values.get(i)[-1][2].values()
                if not any(one2many_data):
                    raise UserError("Attenzione! Stai inserendo una riga senza alcun dato all'interno!") 
        
        return res
    
    
    @api.onchange('order_line')
    def _compute_categ_ids(self):
        model_data_obj = self.env["ir.model.data"]
        ecommerce_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "ecommerce")[1]
        ads_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "ads")[1]
        facebook_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "facebook")[1]
        gmb_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "gmb")[1]
        instagram_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "instagram")[1]
        landing_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "landing")[1]
        plugin_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "plugin")[1]
        portale_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "portale")[1]
        seo_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "seo")[1]
        sito_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "sito")[1]
        virtual_tour_categ_id = model_data_obj.get_object_reference("usb_sale_workflow", "virtual_tour")[1]
        
        for rec in self:
            categ_ids_order = [line.product_id.categ_id.id for line in rec.order_line]
            rec.has_ecommerce_categ = ecommerce_categ_id in categ_ids_order
            rec.has_ads_categ = ads_categ_id in categ_ids_order
            rec.has_facebook_categ = facebook_categ_id in categ_ids_order
            rec.has_gmb_categ = gmb_categ_id in categ_ids_order
            rec.has_instagram_categ = instagram_categ_id in categ_ids_order
            rec.has_landing_categ = landing_categ_id in categ_ids_order
            rec.has_plugin_categ = plugin_categ_id in categ_ids_order
            rec.has_portale_categ = portale_categ_id in categ_ids_order
            rec.has_seo_categ = seo_categ_id in categ_ids_order
            rec.has_sito_categ = sito_categ_id in categ_ids_order
            rec.has_virtual_tour_categ = virtual_tour_categ_id in categ_ids_order
            
        
        
    
    has_ecommerce_categ = fields.Boolean(compute=_compute_categ_ids)
    has_ads_categ = fields.Boolean(compute=_compute_categ_ids)
    has_facebook_categ = fields.Boolean(compute=_compute_categ_ids)
    has_gmb_categ = fields.Boolean(compute=_compute_categ_ids)
    has_instagram_categ = fields.Boolean(compute=_compute_categ_ids)
    has_landing_categ = fields.Boolean(compute=_compute_categ_ids)
    has_plugin_categ = fields.Boolean(compute=_compute_categ_ids)
    has_portale_categ = fields.Boolean(compute=_compute_categ_ids)
    has_seo_categ = fields.Boolean(compute=_compute_categ_ids)
    has_sito_categ = fields.Boolean(compute=_compute_categ_ids)
    has_virtual_tour_categ = fields.Boolean(compute=_compute_categ_ids)
    
    
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    

    prog_riga_ordine_USB = fields.Integer()
    id_prodotto_USB = fields.Integer()