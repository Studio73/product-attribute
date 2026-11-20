# Copyright 2026 Studio73
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    avg_cost = fields.Monetary(groups="product_cost_security.group_product_cost")
    total_value = fields.Monetary(groups="product_cost_security.group_product_cost")
