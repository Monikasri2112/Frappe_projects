# import frappe

# def successful_login(login_manager):
#     print("LOGIN SUCCESS:", frappe.session.user)

# def allocate_free_credits(login_manager):
#     print("SESSION CREATED:", frappe.session.user)

# def clear_user_cache(login_manager):
    # print("LOGOUT:", frappe.session.user)


import frappe

def validate_custom_jwt():
    authorization = frappe.request.headers.get("Authorization")

    print("AUTH HOOK CALLED")
    print("Authorization:", authorization)