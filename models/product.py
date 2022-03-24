from odoo import api, fields, models


class Product(models.Model):
    _name = 'os.product'
    _description = 'New Description'

    name = fields.Char(string='Name', required=True)
    price = fields.Integer(string='Price', required=True)
    stock = fields.Integer(string='Stock', required=True)
    desc = fields.Char(string='Description')
    
    
    
