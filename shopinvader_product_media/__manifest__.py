# Copyright 2016 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopinvader Product Media",
    "summary": "Shopinvader Product Media",
    "version": "10.0.1.0.0",
    "category": "e-commerce",
    "website": "https://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": False,
    "installable": False,
    "auto_install": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["shopinvader", "storage_media_product"],
    "data": ["data/ir_product_export.xml"],
    "demo": [],
    "qweb": [],
}
