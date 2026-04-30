
from odoo import http
from odoo.http import request

class WebsiteContact(http.Controller):

    @http.route('/customer', type='http', auth='user', website=True)
    def create_contacts(self, **kw):
        return request.render('website_practice_module.contact')


    @http.route('/contactform/submit', type='http', auth='user', website=True, method=['POST'], csrf=False)
    def create_button_method(self, **post):
        request.env['res.partner'].sudo().create({
            'name': post.get('name'),
            'phone': post.get('phone'),
            'email': post.get('email'),
            'street' : post.get('street'),
            'birthday' : post.get('birthday')
        })
        return request.render('website_practice_module.contact')

    