from odoo import models,fields


class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Product Brand'

    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    photo = fields.Image(string="Image")