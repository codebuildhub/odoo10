# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectTask(http.Controller):
#     @http.route('/project_task/project_task', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_task/project_task/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_task.listing', {
#             'root': '/project_task/project_task',
#             'objects': http.request.env['project_task.project_task'].search([]),
#         })

#     @http.route('/project_task/project_task/objects/<model("project_task.project_task"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_task.object', {
#             'object': obj
#         })
