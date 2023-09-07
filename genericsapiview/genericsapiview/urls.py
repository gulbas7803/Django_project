from django.contrib import admin
from django.urls import path
from apiview import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    path('studentapi/', views.StudentListCreateApiView.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroyApiView.as_view()),
]
