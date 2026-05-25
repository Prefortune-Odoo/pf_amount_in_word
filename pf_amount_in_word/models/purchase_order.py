from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    amount_in_words = fields.Char(
        string="Amount In Words",
        compute='_compute_amount_in_words',
        store=True,
        help="Total amount in words"
    )

    l10n_in_gst_treatment = fields.Selection([
        ('regular', 'Registered Business - Regular'),
        ('composition', 'Registered Business - Composition'),
        ('unregistered', 'Unregistered Business'),
        ('consumer', 'Consumer'),
        ('overseas', 'Overseas'),
        ('special_economic_zone', 'Special Economic Zone'),
        ('deemed_export', 'Deemed Export'),
    ], string="GST Treatment", readonly=True, help="Dummy field to fix OwlError in purchase order")

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_in_words(self):
        for order in self:
            if order.currency_id:
                order.amount_in_words = order.currency_id.amount_to_text(order.amount_total)
            else:
                order.amount_in_words = ""


