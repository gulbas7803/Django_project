from django.contrib import admin
from .models import Student, Empolyees, Customers


class AdminStudent(admin.ModelAdmin):
    list_display = ['name', 'location', 'marks']


class AdminEmployees(admin.ModelAdmin):
    list_display = ['name', 'location', 'salary']


class AdminCustomers(admin.ModelAdmin):
    list_display = ['name', 'location', 'sales']


admin.site.register(Student, AdminStudent)
admin.site.register(Empolyees, AdminEmployees)
admin.site.register(Customers, AdminCustomers)
