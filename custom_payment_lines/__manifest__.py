# -*- coding: utf-8 -*-
{
    'name': "Custom Payment Lines",

    'summary': """
        This module modifies Odoo's default invoice-workflow.
      """,

    'description': """
        This module modifies Odoo's default invoice-workflow.
      """,

    'author': "Gesca",
    'website': "https://gesca.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Invoicing & Payments',
    'version': '14.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','account_due_list', 'l10n_it_fiscal_payment_term','l10n_it_fiscal_document_type'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/account_move.xml',
        'data/invoice_payment_term.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable' : True,
    'application': False,
    'auto_install': False,
    'images': []
}