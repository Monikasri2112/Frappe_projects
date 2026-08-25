from frappe.model.document import Document

class StudentMixin(Document):

    @property
    def student_info(self):
        return f"{self.student_name} - {self.city} - {self.country}"