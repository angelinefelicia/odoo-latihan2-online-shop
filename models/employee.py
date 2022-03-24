from odoo import api, fields, models


class Employee(models.Model):
    _name = 'os.employee'
    _description = 'New Description'

    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    contact = fields.Char(string='Contact')
    # total_order = fields.Integer(string='Total Order')
    
    
    
