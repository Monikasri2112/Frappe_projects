# Copyright (c) 2026, Monika and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Task(Document):
	pass
import frappe
@frappe.whitelist()
def create_task(task_subject):
	task=frappe.new_doc("Task")
	task.task_subject=task_subject
	task.save()
	return task.name