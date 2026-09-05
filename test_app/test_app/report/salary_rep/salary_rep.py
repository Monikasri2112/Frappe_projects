import frappe


def execute(filters=None):

    filters = filters or {}

    columns = [
        {
            "label": "Employee Name",
            "fieldname": "employee_name",
            "fieldtype": "Data"
        },
        {
            "label": "Department",
            "fieldname": "department",
            "fieldtype": "Data"
        },
        {
            "label": "Salary",
            "fieldname": "salary",
            "fieldtype": "Currency"
        }
    ]

    if filters.get("department"):

        data = frappe.db.sql("""
            SELECT
                employee_name,
                department,
                salary
            FROM `tabEmployee_Now`
            WHERE department = %s
            ORDER BY salary DESC
        """, (filters.get("department"),), as_dict=True)

    else:

        data = frappe.db.sql("""
            SELECT
                employee_name,
                department,
                salary
            FROM `tabEmployee_Now`
            ORDER BY salary DESC
        """, as_dict=True)

    return columns, data