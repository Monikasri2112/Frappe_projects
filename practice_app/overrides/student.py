from practice_app.practice_app.doctype.student.student import student


class CustomStudent(student):

    def say_hello(self):
        return "Hello from Custom Student!"