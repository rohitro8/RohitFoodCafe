from django.contrib import admin
from .models import item, supplier, Role, Employee

admin.site.register(item)
admin.site.register(supplier)
admin.site.register(Role)
admin.site.register(Employee)
