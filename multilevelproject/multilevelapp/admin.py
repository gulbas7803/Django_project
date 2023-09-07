from django.contrib import admin
from .models import Person,Student,Employee

# Register your models here.

class AdminPerson(admin.ModelAdmin):
    list_display = ['name','location']

class AdminStudent(admin.ModelAdmin):
    list_display = ['email','mobile']

class AdminEmployee(admin.ModelAdmin):
    list_display = ['name','email','mobile','location','salary','company','company_location']

admin.site.register(Person,AdminPerson)
admin.site.register(Student,AdminStudent)
admin.site.register(Employee,AdminEmployee)
