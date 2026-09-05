import frappe


def execute(filters=None):

    filters = filters or {}

    department = filters.get("department")

    columns = [
        {
            "label": "Employee",
            "fieldname": "employee_name",
            "fieldtype": "Data"
        },
        {
            "label": "Department",
            "fieldname": "department",
            "fieldtype": "Data"
        },
        {
            "label": "Average Salary",
            "fieldname": "average_salary",
            "fieldtype": "Currency"
        },
        {
            "label": "Total Bonus",
            "fieldname": "total_bonus",
            "fieldtype": "Currency"
        }
    ]

    data = frappe.db.sql("""
        SELECT
            e.employee_name,
            e.department,
            AVG(es.salary) AS average_salary,
            SUM(es.bonus) AS total_bonus
        FROM `tabEmployee` e
        JOIN `tabEmployee Salary` es
            ON e.name = es.parent
        WHERE e.department = %s
        GROUP BY e.name, e.employee_name, e.department
        HAVING average_salary > 30000
        ORDER BY average_salary DESC
        LIMIT 3
    """, (department,), as_dict=True)

    return columns, data