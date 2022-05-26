# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'
    
    
    assign_user_ids = fields.Many2many(
        'res.users',
        'project_assign_users',
        string='Responsible Users',
    )

class Task(models.Model):
    _inherit = 'project.task'
    
    
    assign_user_ids = fields.Many2many(
        'res.users',
        'task_assign_users',
        string='Responsible Users',
    )

    @api.onchange('project_id','project_id.assign_user_ids')
    def _onchange_project_custom(self):
        if self.project_id:
            self.assign_user_ids = self.project_id.assign_user_ids.ids
    
#    @api.multi #odoo13
    def write(self, vals):
        result = super(Task, self).write(vals)
        for rec in self:
            if 'assign_user_ids' in vals and vals.get('assign_user_ids'):
                partner_ids = rec.assign_user_ids.mapped('partner_id')
                rec.message_subscribe(partner_ids.ids)
        return result
            

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: