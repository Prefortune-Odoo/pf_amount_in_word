from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_in_words = fields.Char(
        string="Amount In Words",
        compute='_compute_amount_in_words',
        store=True,
        help="Total amount in words"
    )

    @api.depends('amount_total', 'currency_id')
    def _compute_amount_in_words(self):
        for move in self:
            if move.currency_id:
                move.amount_in_words = move.currency_id.amount_to_text(move.amount_total)
            else:
                move.amount_in_words = ""
