from odoo import api, fields, models

class sale_order(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def print_quotation_without_price(self):
        return self.env['report'].get_action(self, 'sale_order_report.report_saleorder_custom')
