# -*- coding: utf-8 -*-
# from odoo import http


# class ToolMaintenance(http.Controller):
#     @http.route('/tool_maintenance/tool_maintenance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tool_maintenance/tool_maintenance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tool_maintenance.listing', {
#             'root': '/tool_maintenance/tool_maintenance',
#             'objects': http.request.env['tool_maintenance.tool_maintenance'].search([]),
#         })

#     @http.route('/tool_maintenance/tool_maintenance/objects/<model("tool_maintenance.tool_maintenance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tool_maintenance.object', {
#             'object': obj
#         })

