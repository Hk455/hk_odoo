from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_merge_orders(self):
        # Step 1: Ensure that at least two orders are selected
        selected_orders = self.env.context.get('active_ids', [])
        
        # If there are fewer than two orders selected, raise an error
        if len(selected_orders) < 2:
            raise UserError("Please select at least two orders to merge.")

        # Step 2: Fetch the selected orders using their IDs
        orders = self.browse(selected_orders)

        # Step 3: Check if all selected orders belong to the same customer
        customer = orders[0].partner_id  # The customer of the first order
        for order in orders:
            if order.partner_id != customer:
                # If any order belongs to a different customer, raise an error
                raise UserError("All selected orders must be for the same customer to merge.")

        # Step 4: Start merging orders - we will merge all into the first order
        main_order = orders[0]  # The first order will be the main order where all lines are merged
        for order in orders[1:]:  # Go through all orders except the first one
            for line in order.order_line:  # Transfer each order line to the main order
                line.order_id = main_order.id

            # Step 5: Optionally cancel the merged orders (you can also delete them if needed)
            order.state = 'cancel'  # Mark the merged orders as canceled

            # Step 6: Delete the merged orders after transferring lines
            order.unlink()  # Delete the canceled orders from the system

 
