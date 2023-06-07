# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CustomerDuePAyments(models.TransientModel):
    _name = 'customer.due.payments'


    @api.model
    def default_get(self, fields):
        res = super(CustomerDuePAyments, self).default_get(fields)
        if self.env.context.get('active_id') and self.env.context.get('active_model') == 'sale.order':
            order = self.env['sale.order'].browse(self.env.context.get('active_id'))
            if order.exists():
                res.update({'partner_id': order.partner_id.id})
        return res

    partner_id = fields.Many2one('res.partner')
    balance = fields.Float(string='Balance')


    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            total_out_balance= 0.0
            total_in_balance= 0.0
            total_out = self.env['account.invoice'].search(
                [('partner_id', '=', self.partner_id.id), ('type', '=', 'out_invoice')])
            if total_out:
               total_out_balance = sum(total_out.mapped('residual'))
            total_in = self.env['account.invoice'].search(
                [('partner_id', '=', self.partner_id.id), ('type', '=', 'in_invoice')])
            if total_in:
                total_in_balance = sum(total_in.mapped('residual'))
            self.balance = total_in_balance - total_out_balance



