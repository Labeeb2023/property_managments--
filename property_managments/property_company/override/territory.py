import frappe
from erpnext.setup.doctype.territory.territory import Territory

class CustomTerritory(Territory):

    def save(self, *args,**kwargs):
        print(888888888888)
        super().save(*args, **kwargs)
    pass



    def validate(self):
      if self.terrot== "Country" and self.is_group==0:
          frappe.throw(" Country can not be is_group 1")
      super().validate()