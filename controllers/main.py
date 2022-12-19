from odoo import http
from odoo.http import request


class Books(http.Controller):
    @http.route('/create_book', type="http", auth='user', website=True)
    def create_book(self, **kwargs):
        return request.render('odoo_js.create_book_template')

    @http.route('/create/book', type="http", auth='public', website=True)
    def create_book_to_model(self, **kwargs):
        request.env['lms.book'].sudo().create(kwargs)
