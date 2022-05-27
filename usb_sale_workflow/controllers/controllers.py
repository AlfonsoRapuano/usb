# -*- coding: utf-8 -*-
# from odoo import http


# class UsbSaleWorkflow(http.Controller):
#     @http.route('/usb_sale_workflow/usb_sale_workflow/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/usb_sale_workflow/usb_sale_workflow/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('usb_sale_workflow.listing', {
#             'root': '/usb_sale_workflow/usb_sale_workflow',
#             'objects': http.request.env['usb_sale_workflow.usb_sale_workflow'].search([]),
#         })

#     @http.route('/usb_sale_workflow/usb_sale_workflow/objects/<model("usb_sale_workflow.usb_sale_workflow"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('usb_sale_workflow.object', {
#             'object': obj
#         })
