# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import Warning


class ConfirmSqlquery(models.TransientModel):
    _name = 'confirm.query.perform'

    is_confirm_to_perform_query = fields.Boolean(
        string = 'Are you sure do you want to execute query?',
    )

    def action_confirm_query(self):
        if not self.is_confirm_to_perform_query:
            raise Warning("Please confirm to execute query")
        sql_query_generator_id = self.env['sql.query.generator'].browse(self._context.get('active_id'))
        return sql_query_generator_id._action_generate_query()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
