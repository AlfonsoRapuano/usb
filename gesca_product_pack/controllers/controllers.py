# -*- coding: utf-8 -*-
# from odoo import http


# class GescaProductPack(http.Controller):
#     @http.route('/gesca_product_pack/gesca_product_pack/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gesca_product_pack/gesca_product_pack/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gesca_product_pack.listing', {
#             'root': '/gesca_product_pack/gesca_product_pack',
#             'objects': http.request.env['gesca_product_pack.gesca_product_pack'].search([]),
#         })

#     @http.route('/gesca_product_pack/gesca_product_pack/objects/<model("gesca_product_pack.gesca_product_pack"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gesca_product_pack.object', {
#             'object': obj
#         })
