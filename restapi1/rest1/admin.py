from django.contrib import admin
from rest1.models import Employees

# Register your models here.
class Adminemployees(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eaddr']

admin.site.register(Employees,Adminemployees)