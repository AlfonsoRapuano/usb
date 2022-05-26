# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': "PSQL Query Run in User Interface",
    'summary': """Query Run User Interface in Odoo and Output in Excel.""",
    'currency': 'EUR',
    'price': 99.0,
    'version': '3.1.2',
    'description': """
PSQL Query Run User Interface
Allow users to execute query in odoo backend
user(s) can see sql query logs
PSQL Query Run User Interface
PSQL Query Run in User Interface
Query Run User Interface in Odoo and Output in Excel
odoo psql query run
sql query run
query run odoo
psql query odoo
run sql query odoo
run psql query odoo

    """,
    'license': 'Other proprietary',
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "http://www.probuse.com",
    'support': 'contact@probuse.com',
    'images': ['static/description/img1.jpg'],
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/psql_query_run_ui/740',#'https://youtu.be/lr3pwLugZ_k',
    'category': 'Sales/Sales',
    'depends': [
        'base',
    ],
    'data':[
        'security/psql_query_security.xml',
        'security/ir.model.access.csv',
        'views/query_result_history_view.xml',
        'wizard/confirm_to_sql_query_view.xml',
        'wizard/psql_query_generator_view.xml',
    ],
    'qweb': [
    ],
    'installable' : True,
    'application' : False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
