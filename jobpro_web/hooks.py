app_name = "jobpro_web"
app_title = "JOBPRO"
app_publisher = "TEAMPRO"
app_description = "TEAMPRO Job Search Portal using VueJS and Frappe UI"
app_email = "erp@groupteampro.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "jobpro_web",
# 		"logo": "/assets/jobpro_web/logo.png",
# 		"title": "JOBPRO",
# 		"route": "/jobpro_web",
# 		"has_permission": "jobpro_web.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/jobpro_web/css/jobpro_web.css"
# app_include_js = "/assets/jobpro_web/js/jobpro_web.js"

# include js, css files in header of web template
# web_include_css = "/assets/jobpro_web/css/jobpro_web.css"
# web_include_js = "/assets/jobpro_web/js/jobpro_web.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "jobpro_web/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
# app_include_icons = "jobpro_web/public/icons.svg"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "jobpro_web.utils.jinja_methods",
# 	"filters": "jobpro_web.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "jobpro_web.install.before_install"
# after_install = "jobpro_web.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "jobpro_web.uninstall.before_uninstall"
# after_uninstall = "jobpro_web.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "jobpro_web.utils.before_app_install"
# after_app_install = "jobpro_web.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "jobpro_web.utils.before_app_uninstall"
# after_app_uninstall = "jobpro_web.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "jobpro_web.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"jobpro_web.tasks.all"
# 	],
# 	"daily": [
# 		"jobpro_web.tasks.daily"
# 	],
# 	"hourly": [
# 		"jobpro_web.tasks.hourly"
# 	],
# 	"weekly": [
# 		"jobpro_web.tasks.weekly"
# 	],
# 	"monthly": [
# 		"jobpro_web.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "jobpro_web.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "jobpro_web.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "jobpro_web.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["jobpro_web.utils.before_request"]
# after_request = ["jobpro_web.utils.after_request"]

# Job Events
# ----------
# before_job = ["jobpro_web.utils.before_job"]
# after_job = ["jobpro_web.utils.after_job"]

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
# 	"jobpro_web.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

