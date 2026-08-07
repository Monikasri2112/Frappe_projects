import frappe
from frappe.model.document import Document

class employee_request(Document):

    @frappe.whitelist()
    def show_employee(self):

        doc = frappe.get_doc(
            "employee_request",
            self.name
        )

        frappe.msgprint(doc.employee_name)