from frappe.model.document import Document

class ValidationMixin(Document):

    def check_student(self):
        return f"Checking {self.student_name}"