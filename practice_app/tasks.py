import frappe
def daily_maintenance():
    frappe.log_error(
        title="Daily Maintance",
        message="Daily maintenance background job executed successfully."
    )