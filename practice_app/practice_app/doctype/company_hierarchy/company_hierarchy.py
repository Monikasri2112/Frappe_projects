# Copyright (c) 2026, Monika and contributors
# For license information, please see license.txt

# import frappe
from frappe.utils.nestedset import NestedSet


class CompanyHierarchy(NestedSet):
	pass
import frappe

#get_children()
'''@frappe.whitelist()
def show_children(docname):

    doc = frappe.get_doc(
        "Company Hierarchy",
        docname
    )

    for child in doc.get_children():

        frappe.msgprint(child.name)

    return "Done"'''

#get_parents()
import frappe

@frappe.whitelist()
def show_parent(docname):

    # Get current document
    doc = frappe.get_doc(
        "Company Hierarchy",
        docname
    )

    # Get parent document
    parent = doc.get_parent()

    frappe.msgprint(
        "Parent is : " + parent.name
    )

    return "Done"