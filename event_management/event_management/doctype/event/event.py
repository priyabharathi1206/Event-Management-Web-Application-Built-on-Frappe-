import frappe
from frappe.model.document import Document

class Event(Document):
    def validate(self):
        if self.capacity <= 0:
            frappe.throw("Capacity must be greater than zero")

        self.remaining_capacity = self.capacity - (self.tickets_sold or 0)
