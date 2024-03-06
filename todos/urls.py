from django.contrib import admin
from django.urls import path

from .views import index_page, todo_details, delete_todos

urlpatterns = [
    path('', index_page),
    path('<int:pk>', todo_details),
    path('<int:pk>/delete', delete_todos)
]