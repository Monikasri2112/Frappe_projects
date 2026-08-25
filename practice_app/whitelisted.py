import frappe

@frappe.whitelist()
def custom_get_count(doctype, filters=None, debug=False, cache=False):
    return "OVERRIDE IS WORKING!"