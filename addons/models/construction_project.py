from odoo import models, fields

class ConstructionProject(models.Model):
    _name = 'construction.project'
    _description = 'Construction Project'

    name = fields.Char(required=True)
    client = fields.Char()
    location = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()
    manager_id = fields.Many2one('res.users', string='Project Manager')
    phase_ids = fields.One2many('project.phase', 'project_id')

class ProjectPhase(models.Model):
    _name = 'project.phase'
    _description = 'Project Phase'

    name = fields.Char(required=True)
    project_id = fields.Many2one('construction.project')
    start_date = fields.Date()
    end_date = fields.Date()
    budget = fields.Float()
    actual_cost = fields.Float()
