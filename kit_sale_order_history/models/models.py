# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OrderHistoryLine(models.TransientModel):
    _name = 'order.history.line'

    order_id = fields.Many2one('sale.order',string='SO')
    customer_id = fields.Many2one('res.partner', string="Customer")
    product_id = fields.Many2one('product.product',string='Product')
    date = fields.Datetime(string='Date')
    qty_order = fields.Float(string='QTY Ordered')
    unit_price = fields.Float(string='Unit Price')
    direct_id = fields.Many2one('sale.order.history')
    discount = fields.Float(string='Discount')
    total_after_discount = fields.Float(string='Total After Discount',compute='_get_total_after_discount')

    @api.depends('discount','unit_price','qty_order')
    def _get_total_after_discount(self):
        for rec in self:
                discount_val = ((rec.unit_price * rec.qty_order) * rec.discount) / 100
                rec.total_after_discount = (rec.unit_price * rec.qty_order) - discount_val


class SaleOrderHistory(models.TransientModel):
    _name = 'sale.order.history'


    @api.model
    def default_get(self, fields):
        res = super(SaleOrderHistory, self).default_get(fields)
        if self.env.context.get('active_id') and self.env.context.get('active_model') == 'sale.order.line':
            line = self.env['sale.order.line'].browse(self.env.context.get('active_id'))
            if line.exists():
                res.update({'order_line_id': line.id})
        return res

    order_line_id = fields.Many2one('sale.order.line')
    history_line_ids = fields.One2many('order.history.line','direct_id')

    @api.onchange('order_line_id')
    def _onchange_order_line_id(self):
        if self.order_line_id:
            product_order_lines = self.env['sale.order.line'].search([('product_id','=',self.order_line_id.product_id.id),('order_id.state','=','sale')])
            if product_order_lines:
                self.history_line_ids = [(0, 0, {
                    'order_id': line.order_id.id,
                    'customer_id' : line.order_partner_id.id,
                    'product_id': line.product_id.id,
                    'date': line.order_id.date_order,
                    'qty_order': line.product_uom_qty,
                    'unit_price': line.price_unit,
                    'discount': line.discount,
                }) for line in product_order_lines if line != self.order_line_id]

