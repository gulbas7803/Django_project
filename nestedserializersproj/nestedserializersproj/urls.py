from django.contrib import admin
from django.urls import path
from testap import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author-api/', views.AuthorListView.as_view()),
    path('author-api/<int:pk>/', views.AuthorView.as_view()),
    path('book-api/', views.BookListView.as_view()),
    path('book-api/<int:pk>/', views.BookView.as_view()),
]
