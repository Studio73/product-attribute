# Copyright 2026 Studio73
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Product Cost Security Purchase",
    "summary": "Keep purchase product forms usable without product cost access",
    "version": "19.0.1.0.0",
    "category": "Product",
    "author": "Studio73, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/product-attribute",
    "license": "AGPL-3",
    "depends": ["product_cost_security", "purchase"],
    "data": ["views/product_views.xml"],
    "auto_install": True,
    "installable": True,
}
