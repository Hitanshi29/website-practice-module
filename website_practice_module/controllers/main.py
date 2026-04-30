
from odoo import http
from odoo.http import request

class WebsiteContact(http.Controller):

    @http.route('/crm_lead', type='http', auth='public', website=True)
    def create_crmlead(self, **kw):
        return request.render('website_practice_module.crm_lead')

    @http.route('/crm_lead/submit', type='http', auth='public', website=True, method=['POST'], csrf=False)
    def create_crm_button_method(self, **post):

        request.env['crm.lead'].sudo().create({
            "type" : 'lead',
            'contact_name': post.get('contact_name'),
            'email_from': post.get('email_from'),
            'phone': post.get('phone'),
            'partner_name' : post.get('partner_name'),
            'name' : post.get('name'),
            'description' : post.get('description')
        })
        return request.render('website_practice_module.crm_lead')


    @http.route('/customer', type='http', auth='public', website=True)
    def create_contacts(self, **kw):
        return request.render('website_practice_module.contact')


    @http.route('/contactform/submit', type='http', auth='public', website=True, method=['POST'], csrf=False)
    def create_button_method(self, **post):

        email = post.get('email')

        existing = request.env['res.partner'].sudo().search([
            ('email', '=', email)
        ], limit=1)

        if existing:
            return request.redirect('/form?error=duplicate')

        request.env['res.partner'].sudo().create({
            'name': post.get('name'),
            'phone': post.get('phone'),
            'email': post.get('email'),
            'street' : post.get('street'),
            'birthday' : post.get('birthday')
        })
        return request.render('website_practice_module.contact')




    # @http.route('/check_email', type='json', auth='public', website=True)
    # def check_email(self, email):
    #     partner = request.env['res.partner'].sudo().search([
    #         ('email', '=', email)
    #     ], limit=1)

    #     if partner:
    #         return {'exists': True}
    #     return {'exists': False}

        