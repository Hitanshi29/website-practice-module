# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by Bizople Solutions Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Practice Website',
    'version': '1.0',
    'author': 'Bizople Solutions Pvt. Ltd.',
    'website': 'https://www.bizople.com',
    'summary': '',
    'depends': ['crm','website'],
    'data': [
        'views/website_contact.xml',
        'views/website_crm_lead.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'website_practice_module/static/src/js/email_check.js',
        ],
    },
    'sequence' : 1,
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}       
