# import frappe

# def event_registration_query(user):
#     return "`tabEvent Registration`.`seats_available` > 0"

import frappe

def event_registration_has_permission(doc, user=None, permission_type=None):

    # Anyone can read events in Public Hall
    if permission_type == "read" and doc.venue == "Public Hall":
        return True

    # Only owner can edit the event
    if permission_type == "write" and doc.owner == user:
        return True

    return False