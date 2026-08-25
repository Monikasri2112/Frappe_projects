# Copyright (c) 2026, Monika and contributors
# For license information, please see license.txt

from frappe.model.document import Document

class student(Document):

    def say_hello(self):
        return "Hello from original Student"