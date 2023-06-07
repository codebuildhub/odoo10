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
            total_amount_due = 0.0
            amount_dues = self.env['account.invoice'].search(
                [('partner_id', '=', self.partner_id.id), ('type', '=', 'out_invoice')])
            for amount_due in amount_dues:
                total_amount_due += amount_due.residual
            self.balance = total_amount_due
            amount_dues = self.env['account.invoice'].search(
                [('partner_id', '=', self.partner_id.id), ('type', '=', 'in_invoice')])
            for amount_due in amount_dues:
                total_amount_due += amount_due.residual
            self.balance = total_amount_due

