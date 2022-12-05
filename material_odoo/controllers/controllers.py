# -*- coding: utf-8 -*-
# from odoo import http


# class MaterialOdoo(http.Controller):
#     @http.route('/material_odoo/material_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/material_odoo/material_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('material_odoo.listing', {
#             'root': '/material_odoo/material_odoo',
#             'objects': http.request.env['material_odoo.material_odoo'].search([]),
#         })

#     @http.route('/material_odoo/material_odoo/objects/<model("material_odoo.material_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('material_odoo.object', {
#             'object': obj
#         })
