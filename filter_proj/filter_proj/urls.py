from django.contrib import admin
from django.urls import path
from filter_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
]
