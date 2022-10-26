# -*- coding: utf-8 -*-
{
    'name': "Gesca Basic Import Extension",

    'summary': """
        Estende le funzionalità del modulo sh_all_in_one_basic_import""",

    'description': """
        Estende le funzionalità del modulo sh_all_in_one_basic_import""",

    'author': "Gesca",
    'website': "https://gesca.it",
    
    "category": "Extra Tools",
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sh_all_in_one_basic_import'],

    # always loaded
    'data': [
        'views/views.xml',
        'sh_import_inv/import_inv_wizard.xml'
    ],
}
