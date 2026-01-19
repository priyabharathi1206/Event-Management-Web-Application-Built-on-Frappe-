import frappe
from frappe.model.document import Document

class Ticket(Document):
    def validate(self):
        event = frappe.get_doc("Event", self.event)
        self.total_amount = self.quantity * event.ticket_price

        if self.quantity > event.remaining_capacity:
            frappe.throw("Not enough tickets available")

    def on_submit(self):
        event = frappe.get_doc("Event", self.event)
        event.tickets_sold += self.quantity
        event.save(ignore_permissions=True)
