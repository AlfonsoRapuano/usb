# -*- coding: utf-8 -*-
{
    'name': "Gesca Product Pack",

    'summary': """
        Aggiunge alle righe ordine di vendita i prodotti presenti nel prodotto/pack""",

    'description': """
        Aggiunge alle righe ordine di vendita i prodotti presenti nel prodotto/pack""",

    'author': "Gesca",
    'website': "https://gesca.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product_bundle_pack_advance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}