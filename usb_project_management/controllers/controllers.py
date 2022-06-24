# -*- coding: utf-8 -*-
# from odoo import http


# class UsbProjectManagement(http.Controller):
#     @http.route('/usb_project_management/usb_project_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/usb_project_management/usb_project_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('usb_project_management.listing', {
#             'root': '/usb_project_management/usb_project_management',
#             'objects': http.request.env['usb_project_management.usb_project_management'].search([]),
#         })

#     @http.route('/usb_project_management/usb_project_management/objects/<model("usb_project_management.usb_project_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('usb_project_management.object', {
#             'object': obj
#         })
