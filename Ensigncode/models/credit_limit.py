from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, values):
        sale_order = super(SaleOrder, self).create(values)
        
        # Get the customer's credit limit (ensure the correct field is used)
        customer = sale_order.partner_id
        if customer.use_partner_credit_limit:  # Use the correct field name here
            credit_limit = customer.use_partner_credit_limit
            credit_used = customer.credit

            # Check if credit used exceeds 80% of credit limit
            if credit_used > (credit_limit * 0.8):
                # Send email if the limit is below 20%
                template = self.env.ref('Ensigncode.credit_limit_warning_email')
                if template:
                    template.send_mail(sale_order.id, force_send=True)
        
        return sale_order
