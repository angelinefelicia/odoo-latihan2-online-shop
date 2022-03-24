from odoo import api, fields, models


class Customer(models.Model):
    _name = 'os.customer'
    _description = 'New Description'

    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    contact = fields.Char(string='Contact')
    # rank
