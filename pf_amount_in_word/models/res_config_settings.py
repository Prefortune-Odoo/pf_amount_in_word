from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    l10n_in_gsp = fields.Boolean(string="L10n In GSP", help="Dummy field to fix OwlError in settings")
