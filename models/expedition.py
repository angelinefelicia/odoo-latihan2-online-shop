from odoo import api, fields, models


class Expedition(models.Model):
    _name = 'os.expedition'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    type = fields.Char(string='Type')
    
    
