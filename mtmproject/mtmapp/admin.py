from django.contrib import admin
from .models import Student,Course

# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','location','marks']


class AdminCourse(admin.ModelAdmin):
    list_display = ['course','fee']

admin.site.register(Student,AdminStudent)
admin.site.register(Course,AdminCourse)
