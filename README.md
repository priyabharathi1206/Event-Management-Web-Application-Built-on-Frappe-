# Event Management Web Application (Frappe Framework)

## Overview
This project is a simple Event Management web application built using the **Frappe Framework**.  
It allows event planners to manage events, attendees, and ticket sales efficiently.

The application demonstrates:
- Proper DocType design
- Server-side business logic using Frappe ORM
- Report generation
- CSV-based bulk data import

---

## Tech Stack
- **Framework:** Frappe
- **Backend:** Python (Frappe ORM, Controllers)
- **Frontend:** Frappe Desk UI
- **Database:** MariaDB (MySQL)
- **Reports:** Script Report

---

## Features Implemented

### 1. Event Management
- Create, update, delete events
- Fields:
  - Event Title
  - Description
  - Event Date
  - Location
  - Capacity
  - Ticket Price
- Automatic calculation of:
  - Tickets Sold
  - Remaining Capacity

---

### 2. Attendee Management
- Register attendees for an event
- View attendees mapped to events
- Capacity validation to prevent overbooking

---

### 3. Ticket Sales
- Track ticket sales per event
- Auto-calculate total amount
- Update tickets sold count
- Prevent ticket sales beyond available capacity

---

### 4. Reports
- **Event Sales Report**
  - Event name
  - Tickets sold
  - Revenue per event

---

### 5. CSV Import
- Bulk event creation using CSV
- Implemented using **Frappe Data Import Tool**
- Supported CSV fields:
  - Event Title
  - Description
  - Event Date
  - Location
  - Capacity
  - Ticket Price

---

## Project Structure
event_management/
├── event_management/
│ ├── doctype/
│ │ ├── event/
│ │ ├── attendee/
│ │ └── ticket/
│ ├── report/
│ │ └── event_sales_report/
│ ├── hooks.py
│ └── init.py
└── README.md


---

## Setup Instructions (Local)
```bash
bench init frappe-bench
cd frappe-bench
bench new-site event.local
bench get-app event_management
bench --site event.local install-app event_management
bench start
---
```
## access
http://localhost:8000

## Design Decisions

Used separate DocTypes for Event, Attendee, and Ticket for better normalization

Business rules enforced using validate() and on_submit() hooks

Report implemented as a Script Report for flexibility

CSV import handled using Frappe’s built-in Data Import feature

## Future Enhancements

Role-based access control

Payment gateway integration

Dashboard with charts

Email notifications

### Author

Priya Bharathi B