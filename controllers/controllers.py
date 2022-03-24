# -*- coding: utf-8 -*-
# from odoo import http


# class AngelOnlineShop(http.Controller):
#     @http.route('/angel_online_shop/angel_online_shop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/angel_online_shop/angel_online_shop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('angel_online_shop.listing', {
#             'root': '/angel_online_shop/angel_online_shop',
#             'objects': http.request.env['angel_online_shop.angel_online_shop'].search([]),
#         })

#     @http.route('/angel_online_shop/angel_online_shop/objects/<model("angel_online_shop.angel_online_shop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('angel_online_shop.object', {
#             'object': obj
#         })
