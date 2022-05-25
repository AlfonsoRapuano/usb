# -*- coding: utf-8 -*-
# from odoo import http


# class UsbCustomPartnerFields(http.Controller):
#     @http.route('/usb_custom_partner_fields/usb_custom_partner_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/usb_custom_partner_fields/usb_custom_partner_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('usb_custom_partner_fields.listing', {
#             'root': '/usb_custom_partner_fields/usb_custom_partner_fields',
#             'objects': http.request.env['usb_custom_partner_fields.usb_custom_partner_fields'].search([]),
#         })

#     @http.route('/usb_custom_partner_fields/usb_custom_partner_fields/objects/<model("usb_custom_partner_fields.usb_custom_partner_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('usb_custom_partner_fields.object', {
#             'object': obj
#         })
