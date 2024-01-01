# -*- coding: utf-8 -*-
# from odoo import http


# class PlanificacionMod1(http.Controller):
#     @http.route('/planificacion_mod1/planificacion_mod1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/planificacion_mod1/planificacion_mod1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('planificacion_mod1.listing', {
#             'root': '/planificacion_mod1/planificacion_mod1',
#             'objects': http.request.env['planificacion_mod1.planificacion_mod1'].search([]),
#         })

#     @http.route('/planificacion_mod1/planificacion_mod1/objects/<model("planificacion_mod1.planificacion_mod1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('planificacion_mod1.object', {
#             'object': obj
#         })
