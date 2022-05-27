# -*- coding: utf-8 -*-
{
    'name': "USB Sale Workflow",

    'summary': """
        Customizzazione degli ordini di vendita per USB""",

    'description': """
        Customizzazione degli ordini di vendita per USB""",

    'author': "Gesca",
    'website': "https://gesca.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','account'],

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
