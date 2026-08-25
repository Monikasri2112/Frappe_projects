import frappe

def clear_cache():
    frappe.cache().delete_value("app_specific_cache")

