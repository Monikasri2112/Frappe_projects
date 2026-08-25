import frappe


def get_web_pages_with_dynamic_routes():
    return [
        frappe._dict({
            "doctype": "Web Page",
            "route": "/profile/<name>",
            "name": "profile-page"
        })
    ] 