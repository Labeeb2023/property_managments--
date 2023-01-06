# Copyright (c) 2023, labeeb@gmail.com and contributors
# For license information, please see license.txt
import frappe
#import frappe
from frappe.model.document import Document
import json
class Propertys(Document):
	@frappe.whitelist()
	def set_responsible_person(self , values):
		self.responsible_person = values["responsible_person"]
		self.save()
	
		pass 
@frappe.whitelist()
#@frappe.whitelist()
def set_responsible_person(responsible_person,name):

	res=json.loads(responsible_person)
	doc = frappe.get_doc("Properys", name)
	doc.responsible_person = res["responsible_person"]
	doc.save()
	
	