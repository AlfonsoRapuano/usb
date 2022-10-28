# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID

import logging

_logger = logging.getLogger("===== Product Bundle Pack =====")


class ProcurementRule(models.Model):
    _inherit = 'stock.rule'

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        result = super(ProcurementRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        config = self.env['res.config.settings'].search([],order="id desc", limit=1)
        if  product_id.pack_ids:
            for item in product_id.pack_ids:
                result.update({
                                'name': name[:2000],
                                'company_id': self.company_id.id or self.location_src_id.company_id.id or self.location_id.company_id.id or company_id.id,
                                'product_id': item.product_id.id,
                                'product_uom': item.uom_id and item.uom_id.id,
                                'product_uom_qty': item.qty_uom,
                                'partner_id': result.get('partner_id') if 'partner_id' in values else False,
                                'location_id': self.location_src_id.id,
                                'location_dest_id': location_id.id,
                                'move_dest_ids': result.get('move_dest_ids'),
                                'rule_id': self.id,
                                'procure_method': self.procure_method,
                                'origin': origin,
                                'picking_type_id': self.picking_type_id.id,
                                'group_id': result.get('group_id'),
                                'route_ids': [(4, route.id) for route in values.get('route_ids', [])],
                                'warehouse_id': self.propagate_warehouse_id.id or self.warehouse_id.id,
                                'date': result.get('date'),
                                'date_deadline': result.get('date_deadline'),
                                'propagate_cancel': self.propagate_cancel,
                                'description_picking': result.get('description_picking'),
                                'priority': values.get('priority', "0"),
                                'orderpoint_id': values.get('orderpoint_id') and values['orderpoint_id'].id,
                            })
        if product_id.is_pack == True :
            if config.stock_option_pack == 'both' :
                result.update({
                                'name': name[:2000],
                                'company_id': self.company_id.id or self.location_src_id.company_id.id or self.location_id.company_id.id or company_id.id,
                                'product_id': product_id.id,
                                'product_uom': product_uom.id,
                                'product_uom_qty': product_qty,
                                'partner_id': result.get('partner_id') if 'partner_id' in values else False,
                                'location_id': self.location_src_id.id,
                                'location_dest_id': location_id.id,
                                'move_dest_ids': result.get('move_dest_ids'),
                                'rule_id': self.id,
                                'procure_method': self.procure_method,
                                'origin': origin,
                                'picking_type_id': self.picking_type_id.id,
                                'group_id': result.get('group_id'),
                                'route_ids': [(4, route.id) for route in values.get('route_ids', [])],
                                'warehouse_id': self.propagate_warehouse_id.id or self.warehouse_id.id,
                                'date': result.get('date'),
                                'date_deadline': result.get('date_deadline'),
                                'propagate_cancel': self.propagate_cancel,
                                'description_picking': result.get('description_picking'),
                                'priority': values.get('priority', "0"),
                                'orderpoint_id': values.get('orderpoint_id') and values['orderpoint_id'].id,
                            })
        return result



class Sale_order_line(models.Model):
    _inherit = 'sale.order.line'


    def _prepare_procurement_values(self, group_id):
        res = super(Sale_order_line, self)._prepare_procurement_values(group_id=group_id)
        values = []
        config = self.env['res.config.settings'].search([],order="id desc", limit=1)
        
        if  self.product_id.pack_ids:
            for item in self.product_id.pack_ids:
                line_route_ids = self.env['stock.location.route'].browse(self.route_id.id)
                values.append({
                    'name': item.product_id.name,
                    'origin': self.order_id.name,
                    'product_id': item.product_id.id,
                    'product_qty': item.qty_uom * abs(self.product_uom_qty),
                    'product_uom': item.uom_id and item.uom_id.id,
                    'company_id': self.order_id.company_id,
                    'group_id': group_id,
                    'sale_line_id': self.id,
                    'warehouse_id' : self.order_id.warehouse_id and self.order_id.warehouse_id,
                    'location_id': self.order_id.partner_shipping_id.property_stock_customer.id,
                    'route_ids': self.route_id and line_route_ids or [],
                    'partner_dest_id': self.order_id.partner_shipping_id,
                    'partner_id': self.order_id.partner_id.id
                })

            if config.stock_option_pack == 'both' :
                line_route_ids = self.env['stock.location.route'].browse(self.route_id.id)
                values.append({
                    'name': self.product_id.name,
                    'origin': self.order_id.name,
                    'product_id': self.product_id.id,
                    'product_qty': self.product_uom_qty,
                    'product_uom': self.product_uom.id,
                    'company_id': self.order_id.company_id,
                    'group_id': group_id,
                    'sale_line_id': self.id,
                    'warehouse_id' : self.order_id.warehouse_id and self.order_id.warehouse_id,
                    'location_id': self.order_id.partner_shipping_id.property_stock_customer.id,
                    'route_ids': self.route_id and line_route_ids or [],
                    'partner_dest_id': self.order_id.partner_shipping_id,
                    'partner_id': self.order_id.partner_id.id
                })

            
            return values
        else:
            res.update({
            'company_id': self.order_id.company_id,
            'group_id': group_id,
            'sale_line_id': self.id,
            'route_ids': self.route_id,
            'warehouse_id': self.order_id.warehouse_id or False,
            'partner_dest_id': self.order_id.partner_shipping_id
        })
        return res


    def _compute_qty_delivered(self):
        res = super(Sale_order_line,self)._compute_qty_delivered();
        # GESCA fix della situazione in cui ci sono righe ordine di vendita afferenti a diversi ordini in _compute_qty_delivered
        for rec in self:
            stock = self.env['stock.picking'].search([("origin","=",rec.order_id.name)]);
            config = self.env['res.config.settings'].search([],order="id desc", limit=1);
            if stock:
                if config.stock_option_pack == 'bundle_items':
                    if stock.state == 'done':
                        #for rec in self:
                        #    rec.qty_delivered = rec.product_uom_qty;
                        rec.qty_delivered = rec.product_uom_qty;
        return res;


import inspect
class Sale_order(models.Model):
    _inherit = 'sale.order'

    
    def _create_invoices(self, grouped=False, final=False,date=None):
        res = super(Sale_order,self)._create_invoices(grouped, final,date)
        print(inspect.stack());
        for inv in res :
            invoice = inv
            config = self.env['res.config.settings'].search([],order="id desc", limit=1)
            values = []
            invoice_lines = self.env['account.move.line']
            if config.invoice_option_pack == 'bundle_items' :
                for line in invoice.invoice_line_ids :
                    sale_line = line.sale_line_ids and line.sale_line_ids[0]
                    if line.product_id.is_pack == True :
                        for pack in line.product_id.pack_ids :
                            vals = {
                                    'display_type': line.display_type,
                                    'sequence': line.sequence,
                                    'name': pack.product_id.name,
                                    'product_id': pack.product_id.id,
                                    'product_uom_id': pack.product_id.uom_id.id,
                                    'quantity': line.quantity * pack.qty_uom,
                                    'discount': line.discount,
                                    'price_unit': pack.product_id.lst_price,
                                    'tax_ids': [(6, 0, line.tax_ids.ids)],
                                    'analytic_account_id': sale_line.order_id.analytic_account_id.id,
                                    'analytic_tag_ids': [(6, 0, sale_line.analytic_tag_ids.ids)],
                                    'sale_line_ids': [(4, sale_line.id)],
                                    }
                            values.append((0,0,vals))
                        invoice.with_context(check_move_validity=False).write({'invoice_line_ids': [(2,line.id)]})
                invoice.with_context(check_move_validity=False).write({'invoice_line_ids': values})
            if config.invoice_option_pack == 'main_budle_items' :
                for line in invoice.invoice_line_ids :
                    sale_line = line.sale_line_ids and line.sale_line_ids[0]
                    if line.product_id.is_pack == True :
                        for pack in line.product_id.pack_ids :
                            vals = {
                                    'display_type': line.display_type,
                                    'sequence': line.sequence,
                                    'name': pack.product_id.name,
                                    'product_id': pack.product_id.id,
                                    'product_uom_id': pack.product_id.uom_id.id,
                                    'quantity': line.quantity * pack.qty_uom,
                                    'discount': line.discount,
                                    'price_unit': pack.product_id.lst_price,
                                    'tax_ids': [(6, 0, line.tax_ids.ids)],
                                    'analytic_account_id': sale_line.order_id.analytic_account_id.id,
                                    'analytic_tag_ids': [(6, 0, sale_line.analytic_tag_ids.ids)],
                                    'sale_line_ids': [(4, sale_line.id)],
                                    }
                            values.append((0,0,vals))
                invoice.write({'invoice_line_ids' :values })
        return res

   
