from django.contrib import admin
from .models import Student,Trainer,Course,Book

# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display = ['name','location','email']

class AdminTrainer(admin.ModelAdmin):
    list_display = ['trainer','salary','company']

class AdminCourse(admin.ModelAdmin):
    list_display = ['course','fee','duration']

class AdminBook(admin.ModelAdmin):
    list_display = ['book_name','cost','author']

admin.site.register(Student,AdminStudent)
admin.site.register(Trainer,AdminTrainer)
admin.site.register(Course,AdminCourse)
admin.site.register(Book,AdminBook)
