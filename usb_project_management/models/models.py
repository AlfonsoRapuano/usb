# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
import logging
_logger = logging.getLogger("====== USB Project Management ======")


class ProjectProjectInherit(models.Model):
    _inherit = "project.project"
    
    project_order = fields.Boolean('Progetto Ordine di vendita',copy=False)
    
    # dati tecnici
    product_qty = fields.Integer('Quantità prodotti', readonly=True)
    budget = fields.Integer('Budget', readonly=True)
    plugin_type = fields.Selection(
        [ 
            ('booking_landing', 'BOOKING LANDING'),
            ('facebook', 'FACEBOOK'),
            ('form_landing', 'FORM LANDING'),
            ('messenger', 'MESSENGER'),
            ('whatsapp', 'WHATSAPP')
        ],'Tipologia Plugin', readonly=True)
    art_mark_qty = fields.Integer('Quantità Article Marketing', readonly=True)
    article = fields.Boolean(readonly=True)
    super_key = fields.Char('Super Key', readonly=True)
    qty_panoramiche = fields.Integer('Quantità Panoramiche', readonly=True)
    
    @api.model
    def create(self, values):
        # aggiungiamo i dati tecnici al progetto nel momento della sua creazione
        # a partire dai dati del prodotto
        values.update({
            'product_qty': self.sale_line_id.product_id.product_qty,
            'budget': self.sale_line_id.product_id.budget,
            'plugin_type': self.sale_line_id.product_id.plugin_type,
            'art_mark_qty': self.sale_line_id.product_id.art_mark_qty,
            'article': self.sale_line_id.product_id.article,
            'super_key': self.sale_line_id.product_id.super_key,
            'qty_panoramiche': self.sale_line_id.product_id.qty_panoramiche,
        })
        
        res = super(ProjectProjectInherit, self).create(values)
        return res
    
    def copy(self, default=None):
        self.ensure_one()
        res = super(ProjectProjectInherit, self.with_context(project_copy=True)).copy(default)
        # quando duplichiamo un progetto, ne duplichiamo anche le fasi
        project_phases = self.env['project.phase'].search(
            [("project_id", "=", self.id)]
        )
        for phase in project_phases:
            new_phase = phase.copy()
            new_phase.project_id = res
            tasks = self.env['project.task'].search(
                [('project_phase_id','=', phase.id),('project_id','=', res.id)]
            )
            for task in tasks:
                task.project_phase_id = new_phase
                
        return res
    
    
class SaleOrder(models.Model):
    _inherit = "sale.order"   
    
    @api.depends('order_line.product_id', 'order_line.project_id')
    def _compute_project_ids(self):
        for order in self:
            #projects = order.order_line.mapped('product_id.project_id')
            #projects |= order.order_line.mapped('project_id')
            #projects |= order.project_id
            # cambiata computazione dei progetti collegati basandosi sulle righe di ordine collegate a quel progetto
            projects = order.project_id.search(['|', ('sale_line_id', 'in', order.order_line.ids), ('sale_order_id', '=', order.id)])

            order.project_ids = projects
            # order.tasks_ids = self.env['project.task'].search(['|', ('sale_line_id', 'in', order.order_line.ids), ('sale_order_id', '=', order.id)])
            
    def _action_confirm(self):
        """ On SO confirmation, some lines should generate a task or a project. """
        result = super()._action_confirm()
        if len(self.company_id) == 1:
            # All orders are in the same company
            self.order_line.sudo().with_company(self.company_id)._timesheet_service_generation()

            if not self.project_id: 
                # copia un progetto e lo  aggiunge all'ordine di vendita
                project = self.env['project.project'].search([('project_order','=', True)]).copy()
                # X usb ci dirà con quale parola dovremmo sostiurlo
                project.name = "%s - %s - XOO" % (self.name, project.name.replace('(copia)',''))
                project.partner_id = self.partner_id.id
                project.sale_order_id = self.id
                project.active: True
                project.company_id: self.company_id.id

                self.write({'project_id': project.id})
        else:
            # Orders from different companies are confirmed together
            for order in self:
                order.order_line.sudo().with_company(order.company_id)._timesheet_service_generation()
        return result
                
            
            
class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    

    
    def _timesheet_create_project(self,project_num=1):
        """ Generate project for the given so line, and link it.
            :param project: record of project.project in which the task should be created
            :return task: record of the created task
        """
        self.ensure_one()
        values = self._timesheet_create_project_prepare_values()
        
        if self.product_id.project_template_id:
            # X usb ci dirà con quale parola dovremmo sostiurlo
            values['name'] = "%s  - %s - X0%s" % (values['name'], self.product_id.name, str(project_num))
            project = self.product_id.project_template_id.copy(values)
            project.tasks.write({
                'sale_line_id': self.id,
                'partner_id': self.order_id.partner_id.id,
                'email_from': self.order_id.partner_id.email,
            })
            # duplicating a project doesn't set the SO on sub-tasks
            project.tasks.filtered(lambda task: task.parent_id != False).write({
                'sale_line_id': self.id,
                'sale_order_id': self.order_id,
            })
        else:
            project = self.env['project.project'].create(values)

        # Avoid new tasks to go to 'Undefined Stage'
        if not project.type_ids:
            project.type_ids = self.env['project.task.type'].create({'name': _('New')})

        # link project as generated by current so line
        self.write({'project_id': project.id})
        return project
    

    
    def _timesheet_service_generation(self):
        """ For service lines, create the task or the project. If already exists, it simply links
            the existing one to the line.
            Note: If the SO was confirmed, cancelled, set to draft then confirmed, avoid creating a
            new project/task. This explains the searches on 'sale_line_id' on project/task. This also
            implied if so line of generated task has been modified, we may regenerate it.
        """
        so_line_task_global_project = self.filtered(lambda sol: sol.is_service and sol.product_id.service_tracking == 'task_global_project')
        so_line_new_project = self.filtered(lambda sol: sol.is_service and sol.product_id.service_tracking in ['project_only', 'task_in_project'])

        # search so lines from SO of current so lines having their project generated, in order to check if the current one can
        # create its own project, or reuse the one of its order.
        map_so_project = {}
        if so_line_new_project:
            order_ids = self.mapped('order_id').ids
            so_lines_with_project = self.search([('order_id', 'in', order_ids), ('project_id', '!=', False), ('product_id.service_tracking', 'in', ['project_only', 'task_in_project']), ('product_id.project_template_id', '=', False)])
            map_so_project = {sol.order_id.id: sol.project_id for sol in so_lines_with_project}
            so_lines_with_project_templates = self.search([('order_id', 'in', order_ids), ('project_id', '!=', False), ('product_id.service_tracking', 'in', ['project_only', 'task_in_project']), ('product_id.project_template_id', '!=', False)])
            map_so_project_templates = {(sol.order_id.id, sol.product_id.project_template_id.id): sol.project_id for sol in so_lines_with_project_templates}

        # search the global project of current SO lines, in which create their task
        map_sol_project = {}
        if so_line_task_global_project:
            map_sol_project = {sol.id: sol.product_id.with_company(sol.company_id).project_id for sol in so_line_task_global_project}

        def _can_create_project(sol):
            
            '''
            if not sol.project_id:
                if sol.product_id.project_template_id:
                    #controllo la quantità
                    if sol.product_uom_qty:
                        return (sol.order_id.id, sol.product_id.project_template_id.id) not in map_so_project_templates
                elif sol.order_id.id not in map_so_project:
                    return True
            return False
            '''
            _logger.info("siamo in can_create_project")
            return True

        def _determine_project(so_line):
            """Determine the project for this sale order line.
            Rules are different based on the service_tracking:

            - 'project_only': the project_id can only come from the sale order line itself
            - 'task_in_project': the project_id comes from the sale order line only if no project_id was configured
              on the parent sale order"""

            if so_line.product_id.service_tracking == 'project_only':
                return so_line.project_id
            elif so_line.product_id.service_tracking == 'task_in_project':
                return so_line.order_id.project_id or so_line.project_id

            return False

        # task_global_project: create task in global project
        for so_line in so_line_task_global_project:
            if not so_line.task_id:
                if map_sol_project.get(so_line.id):
                    so_line._timesheet_create_task(project=map_sol_project[so_line.id])

        # project_only, task_in_project: create a new project, based or not on a template (1 per SO). May be create a task too.
        # if 'task_in_project' and project_id configured on SO, use that one instead
        for so_line in so_line_new_project:
            project = _determine_project(so_line)
            if not project and _can_create_project(so_line):
                #ciclo la quantità di ogni riga ordine e creo per ogni un progetto
                for line in range(int(so_line.product_uom_qty)):
                    project = so_line._timesheet_create_project(line+1) 
                
                # https://stackoverflow.com/questions/9377402/insert-into-many2many-odoo-former-openerp
                #so_line.order_id.write({'project_ids': [(4, project.id)] })
                
                #_logger.info(so_line.order_id.project_ids)

                
                if so_line.product_id.project_template_id:
                    map_so_project_templates[(so_line.order_id.id, so_line.product_id.project_template_id.id)] = project
                else:
                    map_so_project[so_line.order_id.id] = project
            elif not project:
                # Attach subsequent SO lines to the created project
                so_line.project_id = (
                    map_so_project_templates.get((so_line.order_id.id, so_line.product_id.project_template_id.id))
                    or map_so_project.get(so_line.order_id.id)
                )
            if so_line.product_id.service_tracking == 'task_in_project':
                if not project:
                    if so_line.product_id.project_template_id:
                        project = map_so_project_templates[(so_line.order_id.id, so_line.product_id.project_template_id.id)]
                    else:
                        project = map_so_project[so_line.order_id.id]
                if not so_line.task_id:
                    so_line._timesheet_create_task(project=project)


