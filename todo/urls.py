# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.addTask, name='addTask'),
    path('delete/<str:pk>', views.deleteTask, name='deleteTask'),
]