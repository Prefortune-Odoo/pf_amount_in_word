from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    amount_in_words = fields.Char(
        string="Amount In Words",
        compute='_compute_amount_in_words',
        store=True,
        help="Total amount in words"
    )

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_in_words(self):
        for order in self:
            if order.currency_id:
                order.amount_in_words = order.currency_id.amount_to_text(order.amount_total)
            else:
                order.amount_in_words = ""
