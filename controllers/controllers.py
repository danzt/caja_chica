# -*- coding: utf-8 -*-
from odoo import http

# class CajaChica(http.Controller):
#     @http.route('/caja_chica/caja_chica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/caja_chica/caja_chica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('caja_chica.listing', {
#             'root': '/caja_chica/caja_chica',
#             'objects': http.request.env['caja_chica.caja_chica'].search([]),
#         })

#     @http.route('/caja_chica/caja_chica/objects/<model("caja_chica.caja_chica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('caja_chica.object', {
#             'object': obj
#         })