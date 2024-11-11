from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # Add new state option
    state = fields.Selection(selection_add=[('approved', 'Approved')])

    # Button visibility logic
    show_button_confirm = fields.Boolean(string="Show Confirm Button", compute='_compute_button_visibility')
    show_button_approve_reject = fields.Boolean(string="Show Approve/Reject Buttons", compute='_compute_button_visibility')

    @api.depends('state')
    def _compute_button_visibility(self):
        for order in self:
            order.show_button_confirm = order.state == 'approved'
            order.show_button_approve_reject = order.state == 'draft'

    def action_approve_order(self):
        """Change state to 'approved'."""
        self.write({'state': 'approved'})

    def action_reject_order(self):
        """Change state back to 'draft'."""
        self.write({'state': 'draft'})

    def button_confirm(self):
        """Change state to 'purchase' when confirmed, prevent in 'draft' state."""
        if self.state == 'draft':
            # Prevent the confirm button action if state is 'draft'
            return False
        if self.state == 'approved':
            # Change state to 'purchase' when approved
            self.write({'state': 'purchase'})
        else:
            # Call super method for other cases
            super().button_confirm()