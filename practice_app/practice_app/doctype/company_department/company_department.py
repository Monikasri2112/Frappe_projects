import frappe

'''@frappe.whitelist()
def get_children(parent=None):

    frappe.msgprint(f"""
        <b>Python Function Called</b><br><br>

        Parent Node Clicked : <b>{parent}</b>
    """)

    return frappe.get_all(
        "Company Department",
        filters={
            "parent_company_department": parent
        },
        fields=[
            "name as value",
            "is_group"
        ]
    )'''
