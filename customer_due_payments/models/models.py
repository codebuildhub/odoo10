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
        t_debit = []
        t_credit = []
        if self.partner_id:
            total_credit_lines = self.env['account.move.line'].search(
                [('partner_id', '=', self.partner_id.id)])
            for line in total_credit_lines:
                if line.account_id.user_type_id.name == 'Receivable':
                    if line.debit > 0:
                        t_debit.append(line.debit)
                    if line.credit > 0:
                        t_credit.append(line.credit)
            self.balance = sum(t_debit) -  sum(t_credit)