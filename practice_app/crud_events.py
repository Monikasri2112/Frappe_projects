def after_insert_student(doc, method=None):
    print("NEW STUDENT CREATED")
    print("Student Name:", doc.student_name)


def before_insert_student(doc, method=None):
    print("BEFORE STUDENT IS INSERTED")
    print("Student Name:", doc.student_name)