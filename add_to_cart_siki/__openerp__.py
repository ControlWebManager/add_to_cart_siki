# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Module Add to Cart',
    'summary': 'Child Module - Parent add_to_cart',
    'version': '1.0',
    'author' : 'SIKI SAS, Developer Ing Henry Vivas',
	'website' : 'www.sikisoftware.com',
    "support": "controlwebmanager@gmail.com",
    'category': 'Website',
    'description': """
This module extend App Add to Cart.
========================================================================

List of modifications:
-------------------
    * V.-1.0 Position icon Add to Cart Bottom - Right ( Req. 1061 )

*Required
   This module to work needs the installation of the website_sale_wishlist_siki module

 """,
    'depends': [
        'add_to_cart',
        'website',
        'sale',
        'website_sale',
        'payment',
    ],
    'data': [
        'views/add_to_cart_template_view.xml',

    ],
    'installable': True,
    'application': False,
}