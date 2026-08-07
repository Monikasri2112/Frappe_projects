import frappe
from frappe.model.document import Document

class EventRegistration(Document):
    pass


'''@frappe.whitelist()
def create_event():

    event = frappe.new_doc("Event Registration")

    event.event_name = "Java Workshop"
    event.organizer = "OpenAI Club"
    event.event_date = "2026-08-05"
    event.venue = "Seminar Hall"
    event.registration_fee = 500
    event.seats_available = 100
    event.status = "Open"

    event.insert()

    return f"Created : {event.name}"'''

'''@frappe.whitelist()
def show_documents(docname):

    # Current document (always fetched from DB)
    current_doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    # Current document from cache
    cached_doc = frappe.get_cached_doc(
        "Event Registration",
        docname
    )

    # Last created document
    last_doc = frappe.get_last_doc("Event Registration")

    return {
        "current_document": current_doc.name,
        "current_event": current_doc.event_name,

        "cached_document": cached_doc.name,
        "cached_event": cached_doc.event_name,

        "last_document": last_doc.name,
        "last_event": last_doc.event_name
    }'''

# rename records
'''@frappe.whitelist()
def rename_event(docname):

    new_name = docname + " Updated"

    frappe.rename_doc(
        "Event Registration",
        docname,
        new_name
    )

    return "Renamed Successfully"'''


#delete records
'''@frappe.whitelist()
def delete_event(docname):

    frappe.delete_doc(
        "Event Registration",
        docname
    )

    return "Deleted Successfully"'''

#frappe.get_meta
'''@frappe.whitelist()
def show_meta():

    meta = frappe.get_meta("Event Registration")

    fields = []

    for field in meta.fields:

        fields.append(field.fieldname)

    return fields'''

#frappe.only_for()
'''@frappe.whitelist()
def manager_only():

    frappe.only_for("Manager")

    return "Welcome System Manager!"'''

#doc.save()
'''@frappe.whitelist()
def update_event(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    doc.status = "Closed"

    doc.save()

    return "Event Closed Successfully"'''

#doc.get_doc_before_save

# class EventRegistration(Document):

#     def before_save(self):

#         old_doc = self.get_doc_before_save()

#         if old_doc:

#             frappe.msgprint(
#                 f"""
# Old Status : {old_doc.status}

# New Status : {self.status}
# """
#             )


#has_value_changed()

'''class EventRegistration(Document):

    def before_save(self):

        if self.has_value_changed("status"):

            frappe.msgprint(
                f"Status Changed Successfully!\nCurrent Status: {self.status}"
            )'''


#doc.reload()
'''@frappe.whitelist()
def reload_event(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    #frappe.msgprint(f"Before Reload: {doc.status}")

    doc.reload()

    frappe.msgprint(f"After Reload: {doc.status}")

    return "Document Reloaded"'''

#doc.check_permission()
# @frappe.whitelist()
# def check_permission(docname):

#     doc = frappe.get_doc(
#         "Event Registration",
#         docname
#     )

#     doc.check_permission("read")

#     return "You have Read Permission"

#doc.gettitle()
'''@frappe.whitelist()
def get_event_title(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    return doc.get_title()'''

#doc.notify_update
'''import frappe
from frappe.model.document import Document

class EventRegistration(Document):

    def before_save(self):

        old_doc = self.get_doc_before_save()

        # Skip for new documents
        if not old_doc:
            return

        changes = []

        # Check every field in the DocType
        for field in self.meta.fields:

            fieldname = field.fieldname

            old_value = old_doc.get(fieldname)
            new_value = self.get(fieldname)

            if old_value != new_value:
                changes.append(
                    f"{field.label}\nOld: {old_value}\nNew: {new_value}"
                )

        if changes:
            frappe.msgprint("<br><br>".join(changes))'''

#db_set()
'''@frappe.whitelist()
def update_status(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    doc.db_set("status", "Closed")

    return "Status Updated Successfully"'''

#doc.append
'''import frappe

@frappe.whitelist()
def add_participant(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    doc.append(
        "participants",
        {
            "participant_name": "Rahul",
            "age": 22
        }
    )

    doc.save()

    return "Participant Added Successfully"'''

#doc.get_url()
'''import frappe

@frappe.whitelist()
def show_document_url(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    url = doc.get_url()

    return url'''

#doc.add_comment()
'''@frappe.whitelist()
def add_comment(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    doc.add_comment(
        "Comment",
        "This is my first comment."
    )

    return "Comment Added Successfully"'''

#doc.add_tag()
'''import frappe

@frappe.whitelist()
def add_event_tag(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    doc.add_tag("Workshop")

    return "Tag Added Successfully"'''

#doc.db_insert()
'''@frappe.whitelist()
def db_insert_demo(event_name, organizer, status):

    doc = frappe.new_doc("Event Registration")

    doc.event_name = event_name
    doc.organizer = organizer
    doc.status = status

    doc.db_insert()

    return f"Document Created : {doc.name}"'''

#doc.db_update()
'''import frappe

@frappe.whitelist()
def db_update_demo(docname):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    doc.status = "Completed"
    doc.venue = "Conference Hall"

    doc.db_update()

    return "Document Updated Successfully"'''

#doc.db.update()
'''import frappe

@frappe.whitelist()
def update_status(docname, status):

    doc = frappe.get_doc(
        "Event Registration",
        docname
    )

    doc.status = status

    doc.db_update()

    return "Status Updated Successfully"'''

#doc.get_children()
import frappe

@frappe.whitelist()
def show_children(docname):

    doc = frappe.get_doc("Event Registration", docname)

    for row in doc.get_children():

        frappe.msgprint(
            f"Name: {row.name}<br>"
            f"Event: {row.event_name}<br>"
            f"Status: {row.status}"
        )

    return "Done"

#doc.get_children()
'''import frappe

@frappe.whitelist()
def show_participants(docname):

    doc = frappe.get_doc("Event Registration", docname)

    for row in doc.participants:
        frappe.msgprint(row.participant_name)

    return "Done"'''

#doc.get_parent_doc()
'''import frappe

@frappe.whitelist()
def show_parent(child_name):

    child = frappe.get_doc("Participant", child_name)

    parent = frappe.get_doc(
        child.parenttype,
        child.parent
    )

    return parent.event_name'''

#get_doc():
'''import frappe

@frappe.whitelist()
def create_c_workshop():

    doc = frappe.get_doc({

        "doctype": "Event Registration",

        "event_name": "C Workshop",

        "organizer": "Ragu",

        "status": "Open"

    })

    doc.insert()

    return f"Event Created Successfully : {doc.name}"'''




