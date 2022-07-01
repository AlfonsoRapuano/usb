# -*- coding: utf-8 -*-
# from odoo import http


# class GescaAccountAvatax(http.Controller):
#     @http.route('/gesca_account_avatax/gesca_account_avatax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gesca_account_avatax/gesca_account_avatax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gesca_account_avatax.listing', {
#             'root': '/gesca_account_avatax/gesca_account_avatax',
#             'objects': http.request.env['gesca_account_avatax.gesca_account_avatax'].search([]),
#         })

#     @http.route('/gesca_account_avatax/gesca_account_avatax/objects/<model("gesca_account_avatax.gesca_account_avatax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gesca_account_avatax.object', {
#             'object': obj
#         })
