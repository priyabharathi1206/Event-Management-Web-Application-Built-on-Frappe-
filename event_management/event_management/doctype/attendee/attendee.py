import frappe
from frappe.model.document import Document

class Attendee(Document):
    def validate(self):
        event = frappe.get_doc("Event", self.event)
        if event.remaining_capacity <= 0:
            frappe.throw("Event capacity exceeded")

        event.tickets_sold += 1
        event.save(ignore_permissions=True)
