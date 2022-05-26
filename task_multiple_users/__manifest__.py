# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Task Assigned Multi Users Responsibles Project Tasks',
    'version': '4.12',
    'price': 49.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'author' : 'Probuse Consulting Service Pvt. Ltd.',
    'website' : 'www.probuse.com',
    'support': 'contact@probuse.com',
    'category': 'Services/Project',
    'summary':  """Allow you to assign multiple responsible on project tasks.""",
    'description': """
Task Assigned Multi Users Responsibles Project Tasks
assign tasks to multiple users
multi user task
Multi-user
Assigning multiple users to a task
multiple responsible tasks
multiple users task
multiple assigned tasks
project tasks multiple users assign
     """,
    'images': ['static/description/img1.png'],
    #'live_test_url': 'https://youtu.be/h0nj7jzZzvs',
    'live_test_url': 'https://probuseappdemo.com/probuse_apps/task_multiple_users/938',#'https://youtu.be/8-zwnq-oLhg',
    'depends': [
        'project',
    ],
    'data': [
        'security/task_security.xml',
        'views/task_view.xml',
     ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
