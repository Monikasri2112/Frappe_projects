# Copyright (c) 2026, Monika and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class MovieTicket(Document):
    pass

import frappe
from frappe.model.document import Document

class MovieTicket(Document):
	pass


@frappe.whitelist()
def book_ticket(movie_name=None, price=None):

	frappe.msgprint(f"""
		<b>Python Method Executed</b><br><br>

		Movie Name : {movie_name}<br>
		Price : {price}
	""")

# No parameter
# import frappe

# @frappe.whitelist()
# def ping():
#     return "Pong from Python!"

# One paramter
# import frappe

# @frappe.whitelist()
# def welcome(movie_name):

#     return f"Welcome to {movie_name}"

# multiple parameters
# import frappe

# @frappe.whitelist()
# def calculate(price, quantity):

#     total = int(price) * int(quantity)

#     return {
#         "price": price,
#         "quantity": quantity,
#         "total": total
#     }