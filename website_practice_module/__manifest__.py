# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Practice Website',
    'version': '1.0',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com',
    'summary': '',
    'depends': ['crm','website','website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_contact.xml',
        'views/website_crm_lead.xml',
        'views/website_menu.xml',
        'views/product_brand_view.xml',
        'views/product_template_view.xml',
        'views/brand_template_view.xml',
    ],
    # 'assets': {
    #     'web.assets_frontend': [
    #         'website_practice_module/static/src/js/email_check.js',
    #     ],
    # },
    'sequence' : 1,
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}       
