from django.contrib import admin
from django.urls import path
from school_management_app.api import views
from rest_framework.authtoken import views as tk

urlpatterns = [
    path("student/",views.StudentListView.as_view()),
    path("student/<int:pk>/",views.StudentDetailView.as_view()),
    path("get_api_token/",tk.obtain_auth_token,name='get_api_token'),
]
