# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ToolEquipment(models.Model):
    _name = 'tool.equipment'
    _description = 'Main tool model'

    name = fields.Char(string="Nombre de la herramienta")
    code = fields.Char(string="Codigo Interno")
    description = fields.Char(string="Descripcion")
    date = fields.Char(string="Fecha de compra")
    state = fields.Selection(
        [('available', 'Disponible'), ('asignado', 'Asignado'),
         ('maintenance', 'En mantenimiento'),('lost','Perdido'),('damaged','Dañado')], 'Estado de la herramienta')
    current_employee_id = fields.Many2one(comodel_name='hr.employee', string="Empleado actual que tiene la herramienta asignada.")
    maintenance_ids = fields.One2many(comodel_name='tool.maintenance', inverse_name='tool_equipment_id')
    assignment_ids = fields.One2many(comodel_name='tool.assignment', inverse_name='tool_assignment_id')

    def available_button(self):
        self.state = 'available'

    def asignado_button(self):
        self.state = 'asignado'

    def maintenance_button(self):
        self.state = 'maintenance'

    def lost_button(self):
        self.state = 'lost'

    def damaged_button(self):
        self.state = 'damaged'

class ToolMaintenance(models.Model):
    _name = 'tool.maintenance'
    _description = 'Maintenance history.'

    tool_id = fields.Many2one(
        comodel_name='tool.equipment',
        string="Herramienta",
        required=True)
    tool_equipment_id = fields.Many2one(comodel_name='tool.equipment')
    date = fields.Date(string='Fecha del mantenimiento')
    description = fields.Text(string="Que se le hizo")
    cost = fields.Float(string="Costo del mantenimiento")
    performed_by = fields.Char(string="Quien hizo el mantenimiento")

class ToolAssigment(models.Model):
    _name = 'tool.assignment'
    _description = 'Assignment history'

    tool_id = fields.Many2one(
        comodel_name='tool.equipment',
        string="Herramienta",
        required=True)
    tool_assignment_id = fields.Many2one(comodel_name='tool.equipment')
    employee_id = fields.Many2one(comodel_name='hr.employee', string="Empleado")
    date_assigned = fields.Date(string="Fecha de asignación")
    date_returned = fields.Date(string="Fecha de devolución (si ya se devolvió)")


