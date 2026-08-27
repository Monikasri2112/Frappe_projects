# from apps.frappe.frappe.core import doctype
import frappe


# http://127.0.0.1:8000/api/method/practice_app.api.get_projects
@frappe.whitelist()
def get_projects():
    projects = frappe.db.get_list(
        "Project",
        filters={
        "description": ["like", "%important%"]
    },
        fields=["project_name", "description"]
    )

    return projects
# http://127.0.0.1:8000/api/method/practice_app.api.get_all_projects
@frappe.whitelist()
def get_all_projects():
    projects = frappe.db.get_all(
        "Project",
        fields=["name","project_name", "description"]
    )

    return projects


# http://127.0.0.1:8000/api/method/practice_app.api.get_task_subject
@frappe.whitelist()
def get_task_subject():
    projects = frappe.db.get_value(
        "Project",
        "specsmakers",
        ["project_name", "description"],
    )

    return projects


# http://127.0.0.1:8000/api/method/practice_app.api.get_company_name
@frappe.whitelist()
def get_company_name():

    company_name = frappe.db.get_single_value(
        "Company Settings",
        "company_name"
    )

    return company_name


@frappe.whitelist()
def update_value():
    update=frappe.set_value('Project','specsmakers','description','Updated description')

    return update

@frappe.whitelist()
def db_exists():
    exist=frappe.db.exists('Project','asdf')
    cached=True
    return exist

@frappe.whitelist()
def db_count():
    count=frappe.db.count('Project', filters={'description': 'good one'})
    cached=True
    return count

@frappe.whitelist()
def db_delete():
    frappe.db.delete('Project', filters={'description': 'good one'})
    cached=True
    return "Project deleted successfully"
before = frappe.db.get_list(
    "Project",
    fields=["name", "project_name", "description"]
)


import frappe


@frappe.whitelist()
def test_savepoint():

    # --------------------------------------------------
    # 1. Create Project A
    # --------------------------------------------------

    project_a = frappe.get_doc({
        "doctype": "Project",
        "project_name": "Savepoint Test c",
        "description": "Created before savepoint"
    })

    project_a.insert()

    # Permanently save Project A
    frappe.db.commit()


    # --------------------------------------------------
    # 2. Create SAVEPOINT
    # --------------------------------------------------

    frappe.db.savepoint("project_checkpoint")


    # --------------------------------------------------
    # 3. Create Project B
    # --------------------------------------------------

    project_b = frappe.get_doc({
        "doctype": "Project",
        "project_name": "Savepoint Test D",
        "description": "Created after savepoint"
    })

    project_b.insert()


    # --------------------------------------------------
    # 4. Check database BEFORE rollback
    # --------------------------------------------------

    before_rollback = frappe.get_all(
        "Project",
        filters={
            "name": ["in", ["Savepoint Test c", "Savepoint Test D"]]
        },
        fields=["name", "project_name", "description"]
    )


    # --------------------------------------------------
    # 5. Rollback to SAVEPOINT
    # --------------------------------------------------

    frappe.db.rollback(save_point="project_checkpoint")


    # --------------------------------------------------
    # 6. Check database AFTER rollback
    # --------------------------------------------------

    after_rollback = frappe.get_all(
        "Project",
        filters={
            "name": ["in", ["Savepoint Test c", "Savepoint Test D"]]
        },
        fields=["name", "project_name", "description"]
    )


    # --------------------------------------------------
    # 7. Commit final state
    # --------------------------------------------------

    frappe.db.commit()


    return {
        "before_rollback": before_rollback,
        "after_rollback": after_rollback
    }






@frappe.whitelist()
def test_sql():

    data = frappe.db.sql("""
        SELECT
            project_name,
            description
        FROM `tabProject`
    """, as_dict=True)

    return data




@frappe.whitelist()
def test_multisql():

    data = frappe.db.multisql({
        "mariadb": """
            SELECT
                project_name,
                description
            FROM `tabProject`
        """,

        "postgres": """
            SELECT
                project_name,
                description
            FROM "tabProject"
        """
    })

    return data


@frappe.whitelist()
def describe():
    a = frappe.db.describe("Project")
    return a





@frappe.whitelist()
def change_project_description_type():

    frappe.db.change_column_type(
        "Project",
        "description",
        "TEXT"
    )

    return "Project description column type changed successfully"





@frappe.whitelist()
def get_projects_qb():

    Project = frappe.qb.DocType("Project")

    result = (
        frappe.qb.from_(Project)
        .select(
            Project.project_name,
            Project.description
        )
    ).run(as_dict=True)

    return result


import frappe


@frappe.whitelist()
def test_walk():

    Project = frappe.qb.DocType("Project")

    query = (
        frappe.qb.from_(Project)
        .select(
            Project.project_name,
            Project.description
        )
        .where(Project.project_name == "Website")
    )

    query_string, values = query.walk()

    return {
        "query": query_string,
        "values": values
    }

from frappe.query_builder.functions import Count


@frappe.whitelist()
def count_projects():

    Project = frappe.qb.DocType("Project")

    total = Count("*").as_("total_projects")

    result = (
        frappe.qb.from_(Project)
        .select(total)
    ).run(as_dict=True)

    return result


import frappe


@frappe.whitelist()
def library_book_join():

    Book = frappe.qb.DocType("LBook")
    Shelf = frappe.qb.DocType("Library Shelf")

    query = (
        frappe.qb.from_(Book)
        .inner_join(Shelf)
        .on(Book.shelf == Shelf.shelf_name)
        .select(
            Book.book_title,
            Book.author,
            Shelf.shelf_name,
            Shelf.location
        )
    )

    return query.run(as_dict=True)


import frappe
from frappe.query_builder.functions import JSONValue


@frappe.whitelist()
def get_customer_language():

    CustomerProfile = frappe.qb.DocType("Customer Profile")

    query = (
        frappe.qb.from_(CustomerProfile)
        .select(
            CustomerProfile.customer_name,
            JSONValue(
                CustomerProfile.preferences_json,
                "$.language"
            ).as_("language")
        )
    )

    return query.run(as_dict=True)




from pypika import CustomFunction


@frappe.whitelist()
def test_upper():

    CustomerProfile = frappe.qb.DocType("Customer Profile")

    UpperCase = CustomFunction(
        "UPPER",
        ["value"]
    )

    query = (
        frappe.qb.from_(CustomerProfile)
        .select(
            UpperCase(
                CustomerProfile.customer_name
            ).as_("uppercase_name")
        )
    )

    return str(query)



frappe.utils.logger.set_log_level("INFO")

logger = frappe.logger("my_test", allow_site=True)

@frappe.whitelist()
def test_logging():
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")

    return "Logging test completed"




# @frappe.whitelist()
# def get_children():
#     return [
#         {
#             "value": "Company 1",
#             "title": "Company 1",
#             "expandable": 1
#         },
#         {
#             "value": "Company 2",
#             "title": "Company 2",
#             "expandable": 1
#         }
#     ]

from frappe.utils import now
@frappe.whitelist()
def get_current_datetime():
    return now()

import frappe
from frappe.utils import getdate

@frappe.whitelist()
def test_getdate():
    today = getdate()
    old_date = getdate("2000-03-18")

    return {
        "today": str(today),
        "old_date": str(old_date)
    }


import frappe
from frappe.utils import today
@frappe.whitelist()
def today_date():
    td = today()
    return {"today's date": td}

import frappe
from datetime import datetime
from frappe.utils import add_to_date

@frappe.whitelist()
def after_10_days():
    result = add_to_date(datetime.now(), days=10, as_string=True)
    return result


import frappe
from frappe.utils import add_to_date, today, date_diff

@frappe.whitelist()
def test_date_diff():
    date_1 = today()
    date_2 = add_to_date(date_1, days=34)

    difference = date_diff(date_2, date_1)

    return difference



from frappe.utils import add_to_date, today, days_diff
@frappe.whitelist()
def test_day_diff():
    date_1 = today()
    date_2 = add_to_date(date_1, days=10)

    return(days_diff(date_2, date_1)) 


from frappe.utils import add_to_date, month_diff
@frappe.whitelist()
def test_month_diff():
    date_1 = "2024-07-01"
    date_2 = add_to_date(date_1, days=120)

    return(month_diff(date_2, date_1))


import frappe
from frappe.utils import pretty_date, now, add_to_date

@frappe.whitelist()
def test_pretty_date():
    old_time = add_to_date(now(), days=-4)

    result = pretty_date(old_time)

    return result



import frappe
from frappe.utils import format_duration

@frappe.whitelist()
def test_duration():
    return {
        "50_seconds": format_duration(50),
        "10000_seconds": format_duration(10000),
        "1000000_seconds": format_duration(1000000),
        "hide_days": format_duration(1000000, hide_days=True)
    }

import frappe
from frappe.utils import comma_and

@frappe.whitelist()
def test_comma_and():
    return {
        "with_quotes": comma_and([1, 2, 3]),
        "without_quotes": comma_and(
            ["Apple", "Ball", "Cat"],
            add_quotes=False
        )
    }


import frappe
from frappe.utils import money_in_words

@frappe.whitelist()
def test_money():
    return {
        "inr_900": money_in_words(900),
        "inr_900_50": money_in_words(900.50),
        "usd_900_50": money_in_words(900.50, "USD"),
        "usd_cents": money_in_words(900.50, "USD", "Cents")
    }


import frappe
from frappe.utils import validate_json_string

@frappe.whitelist()
def test_json_validation():

    valid_json = '[{"player": "one", "score": 199}]'
    
    try:
        validate_json_string(valid_json)
        return "Valid JSON"

    except frappe.ValidationError:
        return "Invalid JSON"


import frappe
from frappe.utils import random_string

@frappe.whitelist()
def test_random_string():
    return random_string(90)


# import frappe
# from frappe.utils import mask_string

# @frappe.whitelist()
# def test_mask():
#     return mask_string("1234567890")

import frappe
from frappe.utils import unique

@frappe.whitelist()
def test_unique():
    numbers = [1, 2, 3, 1, 2, 4, 3]

    result = unique(numbers)

    return result

import frappe
from frappe.utils.pdf import get_pdf

@frappe.whitelist()
def test_pdf():

    html = """
    <html>
        <body>
            <h1>Vehicle Service Report</h1>

            <p>Vehicle: TN38AB1234</p>
            <p>Service Type: General Service</p>
            <p>Status: Completed</p>
            <p>Amount: 1500</p>
        </body>
    </html>
    """

    pdf = get_pdf(html)

    frappe.local.response.filename = "vehicle_service.pdf"
    frappe.local.response.filecontent = pdf
    frappe.local.response.type = "download"


from frappe.utils import get_abbr

@frappe.whitelist()
def test_abbr():
    return {
        "name1": get_abbr("Gavin"),
        "name2": get_abbr("Coca Cola Company"),
        "name3": get_abbr("Mohammad Hussain Nagaria", max_len=8)
    }


import frappe
from frappe.utils import validate_url

@frappe.whitelist()
def test_url():
    return {
        "valid_url": validate_url("https://google.com"),
        "invalid_url": validate_url("google"),
        "https_only": validate_url(
            "https://google.com",
            valid_schemes=["http"]
        )
    }

import frappe
from frappe.utils import validate_email_address

@frappe.whitelist()
def test_email():
    return {
        "single": validate_email_address(
            "rushabh@erpnext.com"
        ),

        "multiple": validate_email_address(
            "rushabh@erpnext.com, juiok"
        ),

        "invalid": validate_email_address(
            "Hello everyone"
        )
    }


import frappe
from frappe.utils import validate_phone_number

@frappe.whitelist()
def test_phone():
    return {
        "valid": validate_phone_number("753858375"),
        "country_code": validate_phone_number("+8998-75385837"),
        "invalid": validate_phone_number("invalid")
    }


import frappe

@frappe.whitelist()
def test_cache():

    cache = frappe.cache()

    cache.set("student_name", "Monika")

    result = cache.get("student_name")

    return result.decode()






import frappe
from frappe.utils import get_filtered_list_url


@frappe.whitelist()
def get_vehicle_url():

    
    url = get_filtered_list_url(
        "Event Registration",
            "C Workshop"
    )

    return url


import frappe
from frappe.utils import get_filtered_list_url


@frappe.whitelist()
def get_vehicle():

    url = get_filtered_list_url("Event Registration", [
        "C Workshop",
        "node js"
    ])

    return url




import frappe


@frappe.whitelist()
def download():

    frappe.response.filename = "event.txt"
    frappe.response.filecontent = "C Workshop"
    frappe.response.type = "download"
    frappe.response.display_content_as = "inline"



import frappe


class EventRegistrationSearch:

    # 1. Get all records that we want to search
    def get_items_to_index(self):

        records = frappe.get_all(
            "Event Registration",
            fields=["name"]
        )

        docs = []

        for record in records:
            docs.append(
                self.get_document_to_index(record.name)
            )

        return docs


    # 2. Prepare each record for searching
    def get_document_to_index(self, name):

        doc = frappe.get_doc("Event Registration", name)

        return frappe._dict(
            name=doc.name,
            content=doc.name
        )


    # 3. Decide what to return from the search result
    def parse_result(self, result):

        return result["name"]


@frappe.whitelist()
def test_search():

    search = EventRegistrationSearch()

    # Get records to index
    documents = search.get_items_to_index()

    # Parse each result
    results = []

    for document in documents:
        results.append(
            search.parse_result(document)
        )

    return results



import frappe

@frappe.whitelist()
def make_project_unique():
    frappe.db.add_unique(
        "Project",
        ["description"]
    )

    return "Unique constraint added successfully"

@frappe.whitelist()
def bulk_update():
    frappe.db.bulk_update(
        "Project",
        {
            "Cibin": {
                "project_name": "Cibin",
                "description": "good"
            },
            "MONIKA": {
                "project_name": "MONIKA",
                "description": "good girl"
            }
        }
    )
    frappe.db.commit()
    return "Projects updated successfully"



import frappe

@frappe.whitelist()
def get_projects():
    query = frappe.qb.get_query(
        "Project",
        fields=["name", "project_name", "description"]
    )

    projects = query.run(as_dict=True)

    return projects




import frappe

@frappe.whitelist()
def get_fields():
    query = frappe.qb.get_query(
        "Project",
        fields="*"
    )
    good=query.run(as_dict=True)
    return good

import frappe

@frappe.whitelist()
def get_as():
    query = frappe.qb.get_query(
        "Project",
        fields=["project_name as First","description as Describe"]

    )
    good=query.run(as_dict=True)
    return good


import frappe

@frappe.whitelist()
def get_payment_details():
    query = frappe.qb.get_query(
        "Payment",
        fields=[
            "name",
            "order",
            "order.customer",
            "order.amount",

        ]
    )

    return query.run(as_dict=True)

import frappe

@frappe.whitelist()
def get_order_items():

    query = frappe.qb.get_query(
        "purchase order",
        fields=[
            "name as empname",
            "items.product",
            "items.quantity",
            "items.rate"
        ]
    )

    return query.run(as_dict=True)

import frappe


import frappe


@frappe.whitelist()
def get_purchase_orders():

    query = frappe.qb.get_query(
        "purchase order",
        fields=[
            "name",
            "supplier",
            {
                "items": ["product", "quantity", "rate"]
            }
        ],
        limit=5
    )

    results = query.run(as_dict=True)

    return results



import frappe


@frappe.whitelist()
def employee_salary_functions():

    query = frappe.qb.get_query(
        "Employee qb",
        fields=[
            # Normal fields
            "employee_name",
            "department",
            "salary",

            # Aggregation functions
            {"COUNT": "name", "as": "total_employees"},
            {"SUM": "salary", "as": "total_salary"},
            {"AVG": "salary", "as": "average_salary"},
            {"MAX": "salary", "as": "highest_salary"},
            {"MIN": "salary", "as": "lowest_salary"},

            # Scalar functions
            {"ABS": "salary", "as": "absolute_salary"},

            {"IFNULL": ["last_name", "'Unknown'"], "as": "last_name_value"},

            {"CONCAT": ["first_name", "' '", "last_name"], "as": "full_name"},

            {"EXTRACT": ["'YEAR'", "joining_date"], "as": "joining_year"},

            {"NOW": None, "as": "current_time"}
        ]
    )

    return query.run(as_dict=True)

import frappe


@frappe.whitelist()
def test_all_filters():

    # 1. Equality (=)
    equality_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name", "department"],
        filters={
            "department": "Development"
        }
    )

    equality_result = equality_query.run(as_dict=True)


    # 2. Greater than (>)
    greater_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name", "salary"],
        filters={
            "salary": [">", 30000]
        }
    )

    greater_result = greater_query.run(as_dict=True)


    # 3. Less than (<)
    less_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name", "salary"],
        filters={
            "salary": ["<", 40000]
        }
    )

    less_result = less_query.run(as_dict=True)


    # 4. Greater than or equal (>=)
    greater_equal_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name", "salary"],
        filters={
            "salary": [">=", 30000]
        }
    )

    greater_equal_result = greater_equal_query.run(as_dict=True)


    # 5. Less than or equal (<=)
    less_equal_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name", "salary"],
        filters={
            "salary": ["<=", 40000]
        }
    )

    less_equal_result = less_equal_query.run(as_dict=True)


    # 6. LIKE
    like_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name"],
        filters={
            "employee_name": ["like", "%in%"]
        }
    )

    like_result = like_query.run(as_dict=True)


    # 7. IN
    in_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name", "department"],
        filters={
            "department": [
                "in",
                ["Development", "Testing"]
            ]
        }
    )

    in_result = in_query.run(as_dict=True)


    # 8. NOT IN
    not_in_query = frappe.qb.get_query(
        "Employee qb",
        fields=["name", "employee_name", "department"],
        filters={
            "department": [
                "not in",
                ["Development", "Testing"]
            ]
        }
    )

    not_in_result = not_in_query.run(as_dict=True)


    # 9. Multiple filters using AND
    multiple_query = frappe.qb.get_query(
        "Employee qb",
        fields=[
            "name",
            "employee_name",
            "department",
            "salary"
        ],
        filters=[
            ["department", "=", "Development"],
            ["salary", ">", 30000]
        ]
    )

    multiple_result = multiple_query.run(as_dict=True)


    # Return everything
    return {
        "equality": equality_result,
        "greater_than": greater_result,
        "less_than": less_result,
        "greater_equal": greater_equal_result,
        "less_equal": less_equal_result,
        "like": like_result,
        "in": in_result,
        "not_in": not_in_result,
        "multiple_and": multiple_result
    }

@frappe.whitelist()
def get_orders_with_item():

    query = frappe.qb.get_query(
        "purchase order",
        fields=[
            "name",
            "supplier"
        ],
        filters={
            "items.product": "laptop"
        },
        distinct=True
    )

    return query.run(as_dict=True)


import frappe


@frappe.whitelist()
def test_company_tree():

    # Get descendants of Company 1
    descendants_query = frappe.qb.get_query(
        "Company Hierarchy",
        fields=[
            "name",
            "company_name",
            "parent_company_hierarchy"
        ],
        filters={
            "parent_company_hierarchy": [
                "descendants of",
                "Tech company"
            ]
        }
    )

    descendants = descendants_query.run(as_dict=True)


    # Get ancestors of Development
    ancestors_query = frappe.qb.get_query(
        "Company Hierarchy",
        fields=[
            "name",
            "company_name",
            "parent_company_hierarchy"
        ],
        filters={
            "parent_company_hierarchy": [
                "ancestors of",
                "Development"
            ]
        }
    )

    ancestors = ancestors_query.run(as_dict=True)


    return {
        "descendants": descendants,
        "ancestors": ancestors
    }


import frappe


@frappe.whitelist()
def get_employees():
    query = frappe.qb.get_query(
        "Employee qb",
        fields=[
            "name",
            "first_name",
            "last_name",
            "department",
            "salary",
            "bonus",
            "joining_date"
        ]
    )

    employees = []

    with frappe.db.unbuffered_cursor():
        employee_iterator = query.run(
            as_iterator=True,
            as_dict=True
        )

        for employee in employee_iterator:
            employees.append(employee)

    return employees

@frappe.whitelist()
def get_order():
    query = frappe.qb.get_query(
    "Employee qb",
    fields=["name", "first_name", "department", "salary"],
    order_by="salary desc"
    )
    return query.run(as_dict=True)


import frappe

@frappe.whitelist()
def get_employee_count():
    query = frappe.qb.get_query(
        "Employee qb",
        fields=[
            "department",
            {"COUNT": "'*'", "as": "employee_count"}
        ],
        group_by="department"
    )

    return query.run(as_dict=True)


import frappe

@frappe.whitelist()
def get_employees():
    query = frappe.qb.get_query(
        "Employee qb",
        fields=[
            "name",
            "first_name",
            "last_name",
            "salary"
        ],
        limit=2,
        offset=1
    )

    return query.run(as_dict=True)

import frappe
@frappe.whitelist()
def get_distinct():
    query=frappe.qb.get_query(
        "Employee qb",
        fields=[
            "name",
            "first_name",
            "last_name",
        ],
        distinct=True
    )


    import frappe




import frappe

@frappe.whitelist()
def get_perm():
    query = frappe.qb.get_query(
        "Employee qb",
        fields=[
            "name",
            "first_name",
            "last_name",
            "department",
            "salary",
            "bonus",
            "joining_date"
        ],
        ignore_permissions=False
    )

    return query.run(as_dict=True)




import time

def test_job(number):
    print("=" * 40)
    print(f"JOB {number} STARTED")

    time.sleep(10)

    print(f"JOB {number} FINISHED")
    print("=" * 40)

    return f"Job {number} completed"


def custom_logic(doc, method=None):
    frappe.msgprint("Hook executed!")




import frappe
@frappe.whitelist()
def student_employee_api():
    student=frappe.qb.DocType("student")
    Employee=frappe.qb.DocType("Employee qb")

    results=(
        frappe.qb.from_(student)
        .join(Employee)
        .on(student.student_name==Employee.employee_name)
        .select(
            student.name,
            student.student_name,
            student.city,
            student.country,
            Employee.employee_name,
            Employee.first_name,
            Employee.last_name
        )
        .limit(2)
    ).run(as_dict=True)

    if results:
        doc=frappe.get_doc("student",results[0]["name"])
        doc.country="Updated"
        doc.save()

        for row in results:
            frappe.db.set_value(
                "student",
                row["name"],
                "city",
                "chennai"
            )
    return results


    