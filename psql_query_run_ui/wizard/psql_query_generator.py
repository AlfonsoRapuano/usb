# -*- coding: utf-8 -*-

import xlwt
import io
import base64
from odoo import models, fields, api, exceptions, _


class SqlQueryGenerator(models.TransientModel):
    _name = 'sql.query.generator'
    _description = 'SQL Query Generator'

    name = fields.Text(
        string='Query',
        required=True,
    )
    query_result = fields.Text(
        string='Query Result',
    )
    xls_output = fields.Binary(
        string='Excel Output'
    )
    excel_file = fields.Char(
        string='File Name',
        help='Save report as .xls format',
        default='Query Result.xls'
    )
    is_query_success = fields.Boolean(
        string = 'Query Success',
    )
    search_model = fields.Many2one(
        'ir.model',
        string='Model',
    )
    searched_model_name = fields.Char(
        string='Model Name',
        related='search_model.model',
    )
    search_field = fields.Many2one(
        'ir.model.fields',
        string='Field',
    )
    searched_field_name = fields.Char(
        string='Field Name',
        related='search_field.name',
        domain=[('model_id', '=', search_model)]
    )

    @api.onchange("search_model")
    def _onchange_search_model(self):
        self.search_field = False
        return {
            'domain':{
                'search_field': [('model_id', '=', self.search_model.id)] if self.search_model else []
            },
        }

    def _prepare_query_result_history(self, params_vals={}):
        return {
            'name': params_vals.get('name'),
            'query_run_datetime': fields.Datetime.now(),
            'query_run_by': self.env.uid,
            'query_message': params_vals.get('query_message')
        }

    def _create_query_result_history(self, params_vals={}):
        vals = self._prepare_query_result_history(params_vals)
        return self.env['query.result.history'].create(vals)
 
    def _action_generate_query(self):
        if not self.env.user.has_group('psql_query_run_ui.grp_psql_query_generate'):
            raise exceptions.AccessError(
                    _('You are not allow to perform query directly'))

        query_message = ''
        result_dict = {}
        try:
            cr = self.env.cr
            query = self.name
            res = cr.execute(query)
            if query and 'select' in query.split(' ')[0].lower():
                result_dict = cr.dictfetchall()
            else:
                query_message = "Processed Record(s): %s \n"%(cr.rowcount)
                query_message += "Query has been successfully executed."
                self.write({
                    'query_result' : query_message,
                    'is_query_success': True,
                    'excel_file':False,
                    'xls_output': False,
                })
                self._create_query_result_history({
                    'name': self.name,
                    'query_message': query_message
                })
        except Exception as e:
            cr.rollback()
            query_message = str(e)
        
        if query_message:
            self.write({
                'query_result' : query_message,
                'is_query_success': False,
                'excel_file':False,
                'xls_output': False,
            })
            self._create_query_result_history({
                'name': self.name,
                'query_message': query_message
            })
        elif result_dict:
            result_excel_keys = list(result_dict[0].keys())
            result_excel = [tuple(result.values()) for result in result_dict]
            workbook = xlwt.Workbook()
            sheet_name = 'SQL Generate'
            sheet = workbook.add_sheet(sheet_name)

            row = 0
            col = 0
            for res_key in result_excel_keys:
                sheet.write(row, col, res_key)
                col += 1

            row += 1
            count_val = len(result_excel[0])
            for exc_val in result_excel:
                for len_exc_val in range(0, len(exc_val)):
                    sheet.write(row, len_exc_val, exc_val[len_exc_val])
                row += 1

            stream = io.BytesIO()
            workbook.save(stream)
            query_message = "Processed Record(s): %s \n"%(cr.rowcount)
            query_message += "Query has been successfully executed."
            self.write({
                'query_result' : query_message,
                'is_query_success': True,
                'excel_file':'Query Result.xls',
                'xls_output': base64.encodestring(stream.getvalue())
            })
            self._create_query_result_history({
                'name': self.name,
                'query_message': query_message
            })
        return {}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
