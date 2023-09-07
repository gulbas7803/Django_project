from django.contrib import admin
from .models import Company, Employee


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'name', 'location', 'about', 'type', 'added_date', 'active']
    search_fields = ['name', ]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'phone', 'about', 'position', 'company', ]
    list_filter = ['company', ]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
