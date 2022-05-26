# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "All in One Hide Create, Duplicate, Delete, Import, Export, Print, Action Buttons",
    'version': '14.0.0.2',
    "category" : "Extra Tools",
    'summary': 'All in one hide button all in one hide action button hide create button hide duplicate button hide export button hide import button hide delete button hide edit button hide export action hide print button hide all button invisible button show button all',
    "description": """
        
            All In One Hide/Show Functionality in odoo,
            Hide/Show Create button in odoo,
            Hide/Show Edit button in odoo,
            Hide/Show Delete action button in odoo,
            Hide/Show Duplicate action button in odoo,
            Hide/Show Print button in odoo,
            Hide/Show Action button in odoo,
            Hide/Show Import button in odoo,
            Hide/Show Export button in odoo,
            Hide/Show Export All button in odoo,

    """ , 
    'price': 19,
    'currency': "EUR",
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.in',
    'depends': ['web', 'base_import'],
    'data': [
        'security/groups.xml',
        'views/assets.xml',
    ],
    'qweb': [
        'static/src/xml/create_edit_button.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    "live_test_url" : 'https://youtu.be/01gSh-GFryc',
    "images":['static/description/Banner.png'],
}
