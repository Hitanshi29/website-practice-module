from odoo import models,fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(string="Dote of Birthday")