from django.contrib import admin
from school_management_app.models import Register,Login

# Register your models here.


@admin.register(Register)
class StudentAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","phone","email","date_of_birth","image","status","password"]

@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display=['phone_no','password']





