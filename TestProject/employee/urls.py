from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("dept/", views.add_dept, name="dept"),
    path("delete/<int:id>", views.delete, name="delete_emp"),
    path("<int:id>", views.update, name="update"),
]