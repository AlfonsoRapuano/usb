# -*- coding: utf-8 -*-
# from odoo import http


# class UsbCustomProductFields(http.Controller):
#     @http.route('/usb_custom_product_fields/usb_custom_product_fields/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/usb_custom_product_fields/usb_custom_product_fields/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('usb_custom_product_fields.listing', {
#             'root': '/usb_custom_product_fields/usb_custom_product_fields',
#             'objects': http.request.env['usb_custom_product_fields.usb_custom_product_fields'].search([]),
#         })

#     @http.route('/usb_custom_product_fields/usb_custom_product_fields/objects/<model("usb_custom_product_fields.usb_custom_product_fields"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('usb_custom_product_fields.object', {
#             'object': obj
#         })
