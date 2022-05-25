# -*- coding: utf-8 -*-
{
    'name': "USB Custom Partner Fields",

    'summary': """
        Add custom fields to res partner""",

    'description': """
        Add custom fields to res partner""",

    'author': "Gesca",
    'website': "https://gesca.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Customer Relationship Management",
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
