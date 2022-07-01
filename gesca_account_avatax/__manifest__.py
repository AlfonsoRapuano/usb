# -*- coding: utf-8 -*-
{
    'name': "gesca_account_avatax (modulo tecnico)",

    'summary': """
        fix per la generazione delle fatture nel caso in cui ci siano account_avatax e account_invoice_triple_discount installati""",

    'description': """
        fix per la generazione delle fatture nel caso in cui ci siano account_avatax e account_invoice_triple_discount installati""",

    'author': "Gesca",
    'website': "https://gesca.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Accounting & Finance",
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'account_avatax', 'account_invoice_triple_discount'],

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
