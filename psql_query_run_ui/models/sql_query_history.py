# -*- coding: utf-8 -*-

from odoo import models, fields


class QueryResultHistory(models.Model):
    _name = 'query.result.history'
    _description = 'Query Result History'
    _order ='id desc'

    name = fields.Text(
        string='Query',
        required=True,
    )
    query_run_datetime = fields.Datetime(
        string='Query Run at',
        required=True,
    )
    query_run_by = fields.Many2one(
        'res.users',
        string='Query Run by',
    )
    query_message = fields.Text(
        string='Query Result',
    )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
