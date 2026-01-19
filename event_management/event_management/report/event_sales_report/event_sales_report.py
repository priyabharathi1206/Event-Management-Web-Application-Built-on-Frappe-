import frappe

def execute(filters=None):
    columns = [
        {"label": "Event", "fieldname": "event", "fieldtype": "Link", "options": "Event"},
        {"label": "Tickets Sold", "fieldname": "tickets_sold", "fieldtype": "Int"},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency"}
    ]

    data = frappe.db.sql("""
        SELECT
            name AS event,
            tickets_sold,
            tickets_sold * ticket_price AS revenue
        FROM `tabEvent`
    """, as_dict=True)

    return columns, data
