# -*- coding: utf-8 -*-
# from odoo import http


# class Testy(http.Controller):
#     @http.route('/testy/testy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testy/testy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testy.listing', {
#             'root': '/testy/testy',
#             'objects': http.request.env['testy.testy'].search([]),
#         })

#     @http.route('/testy/testy/objects/<model("testy.testy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testy.object', {
#             'object': obj
#         })
