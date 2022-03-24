from email.policy import default
from odoo import api, fields, models


class Order(models.Model):
    _name = 'os.order'
    _description = 'New Description'

    name = fields.Char(string='Order Number',
                    readonly=True, 
                    required=True,
                    copy=False,
                    default='New')
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('order.number') or 'New'
        result = super(Order, self).create(vals)
        return result

    date_order = fields.Datetime('Date Order', 
                            default=fields.Datetime.now(),
                            readonly=True)

    customer = fields.Many2one(comodel_name='os.customer', 
                            string='Customer',
                            required=True)
    address = fields.Char(string='Customer Address',
                            required=True,
                            compute='_compute_customer_detail')
    contact = fields.Char(string='Customer Contact',
                            required=True,
                            compute='_compute_customer_detail')
    @api.depends('customer')
    def _compute_customer_detail(self):
        for record in self:
            record.address = record.customer.address
            record.contact = record.customer.contact

    orderproduct_ids = fields.One2many(comodel_name='os.orderproduct', 
                                    inverse_name='order_id', 
                                    string='Order Product')

    expedition = fields.Many2one(comodel_name='os.expedition', string='Expedition')
    exp_price = fields.Integer(string='Expedition Price', default=0)

    total_payment = fields.Integer(string='Total Payment', compute='_compute_total_payment')
    @api.depends('orderproduct_ids', 'exp_price')
    def _compute_total_payment(self):
        for record in self:
            a = sum(self.env['os.orderproduct'].search([('order_id', '=', record.id)]).mapped('total_price'))
            record.total_payment = a + record.exp_price
    
    date_send = fields.Date(string='Date Send')
    no_resi = fields.Char(string='No. Resi')

    by_employee = fields.Many2one(comodel_name='os.employee', string='by employee')
    
    status = fields.Char(string='Status', default='In Progress')

    notes = fields.Char(string='Notes')
    
    
    
class OrderProduct(models.Model):
    _name = 'os.orderproduct'
    _description = 'New Description'

    order_id = fields.Many2one(comodel_name='os.order', string='Order')
    product_id = fields.Many2one(comodel_name='os.product', string='Product')
    
    name = fields.Char(string='Name')
    price = fields.Integer(string='Price', compute="_compute_price")
    qty = fields.Integer(string='Qty')
    total_price = fields.Integer(string='Total Price', compute='_compute_total_price')

    @api.depends('product_id')
    def _compute_price(self):
        for record in self:
            record.price = record.product_id.price

    @api.depends('price', 'qty')
    def _compute_total_price(self):
        for record in self:
            record.total_price = record.price * record.qty

    @api.model
    def create(self,vals):
        record = super(OrderProduct, self).create(vals)
        if record.qty:
            self.env['os.product'].search([('id','=',record.product_id.id)]).write({'stock': record.product_id.stock - record.qty})
            return record
    
    
    
    

    
    
    



    
    
    
    
    

    
