app_name = "practice_app"
app_title = "Practice app"
app_publisher = "Monika"
app_description = "practice"
app_email = "monika@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "practice_app",
# 		"logo": "/assets/practice_app/logo.png",
# 		"title": "Practice app",
# 		"route": "/practice_app",
# 		"has_permission": "practice_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/practice_app/css/practice_app.css"
app_include_js = "/assets/practice_app/js/practice_app.js"
#app_include_js = "custom_desk.bundle.js"
# include js, css files in header of web template
web_include_css = "/assets/practice_app/css/practice_app.css"
web_include_js = "/assets/practice_app/js/practice_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "practice_app/public/scss/website"

# include js, css files in header of web form
#webform_include_js = {"Event Registration": "public/js/practice_app.js"}
webform_include_css = {"Event Registration": "public/css/practice_app.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "practice_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "practice_app.utils.jinja_methods",
# 	"filters": "practice_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "practice_app.install.before_install"
# after_install = "practice_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "practice_app.uninstall.before_uninstall"
# after_uninstall = "practice_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "practice_app.utils.before_app_install"
# after_app_install = "practice_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "practice_app.utils.before_app_uninstall"
# after_app_uninstall = "practice_app.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "practice_app.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "practice_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"practice_app.tasks.all"
# 	],
# 	"daily": [
# 		"practice_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"practice_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"practice_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"practice_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "practice_app.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "practice_app.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "practice_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "practice_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["practice_app.utils.before_request"]
# after_request = ["practice_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["practice_app.utils.before_job"]
# after_job = ["practice_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"practice_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

bench_commands=[
    "practice_app.commands::commands"
]
webform_include_css = {
   "webform1": "public/css/practice_app.css"
}
web_include_js="/assets/practice_app/js/app-web.js"
web_include_css="/assets/practice_app/css/practice_app.css"
web_include_css="/assets/practice_app/css/app-web.css"
web_include_js="/assets/practice_app/js/webform.js"

# page_js = {
#     "book-dashboard": "public/js/book-dashboard.js"
# }

sounds = [
    {
        "name": "ping",
        "src": "/assets/practice_app/sounds/ping.mp3",
        "volume": 0.3
    }
]

before_install = "practice_app.setup.install.before_install"

after_install = "practice_app.setup.install.after_install"

after_sync = "practice_app.setup.install.after_sync"

before_uninstall = "practice_app.setup.uninstall.before_uninstall"

after_uninstall = "practice_app.setup.uninstall.after_uninstall"

before_migrate = "practice_app.migrate.before_migrate"
after_migrate = "practice_app.migrate.after_migrate"
before_tests = "practice_app.test_setup.before_tests"


# before_write_file = "practice_app.overrides.file.before_write"
# write_file = "practice_app.overrides.file.write_file"
# delete_file = "practice_app.overrides.file.delete_file"

# extend_bootinfo = "practice_app.boot.boot_session"
# update_website_context = "practice_app.overrides.website_context.website_context"
# extend_website_page_controller_context = {
#     "frappe.www.404": "practice_app.pages.context.context_404"
# }
# website_catch_all = "not_found"
# website_path_resolver = "practice_app.www.resolver.custom_resolver"
# website_clear_cache = "practice_app.www.resolver.clear_website_cache"

# website_redirects = [
#     {
#         "source": "/old-test",
#         "target": "/test"
#     }
# ]

# website_route_rules = [
#     {"from_route": "/project/<name>", 
#      "to_route": "practice_app/projects/project"},
# ]

get_web_pages_with_dynamic_routes = "practice_app.script.get_web_pages_with_dynamic_routes"


# home_page="index"
# brand_html = '<div><h1>BRUSH</h1></div>'

portal_menu_items = [
    {
        "title": "IT Requests",
        "route": "/it-requests",
        "role": "IT Executive"
    }
]

base_template_map = {
    r"one.*": "app/templates/basetemplate.html"
}

braintree_success_page = "practice_app.integrations.braintree_success_page"


calendars = ["Appointment"]

clear_cache = "practice_app.cache.clear_cache"

default_mail_footer = """
<div>
    Sent via <b>Practice App</b>
</div>
"""

# on_login = "practice_app.override.successful_login"
# on_session_creation = "practice_app.override.allocate_free_credits"
# on_logout = "practice_app.override.clear_user_cache"

auth_hooks = ["practice_app.override.validate_custom_jwt"]


permission_query_conditions = {
    "Event Registration": "practice_app.permissions.event_registration_query"
}


has_permission = {
    "Event Registration": "practice_app.permissions.event_registration_has_permission"
}

extend_doctype_class = {
    "student": [
        "practice_app.extensions.student.StudentMixin",
        "practice_app.extensions.common.ValidationMixin"
    ]
}


override_doctype_class = {
    "student": "practice_app.overrides.student.CustomStudent"
}


doctype_js = {
    "student": "public/js/student.js"
}



doc_events = {
    "student": {
        "after_insert": "practice_app.crud_events.after_insert_student",
        "before_insert": "practice_app.crud_events.before_insert_student"
    }
}
# http://127.0.0.1:8000/api/method/frappe.client.get_count?doctype=student
# override_whitelisted_methods = {
#     "frappe.client.get_count": "practice_app.whitelisted.custom_get_count"
# }

ignore_links_on_delete = ["Vehicle"]

additional_timeline_content = {
    "student": ["practice_app.timeline.student_timeline"]
}
app_include_js = ["practice_app.bundle.js"]

# scheduler_events = {
#     "cron": {
#         "*/1 * * * *": [
#             "practice_app.scheduled_tasks.send_hourly_email"
#         ]

#     }
# }


jinja = {
    "methods": [
        "practice_app.jinja.methods"
    ],
    "filters": [
        "practice_app.jinja.filters"
    ]
}

auto_cancel_exempted_doctypes = ["Payment"]

user_data_fields = [
    {
        "doctype": "Student",
        "filter_by": "email",
        "redact_fields": ["phone"]
    }
]

signup_form_template = "practice_app/templates/signup-form.html"

send_sms = "practice_app.overrides.sms.send_sms"

fixtures = [
    "Category"
]


from frappe.model.document import Document


doc_events = {
    "ToDo": {
        "validate": "practice_app.api.custom_logic"
    }
}