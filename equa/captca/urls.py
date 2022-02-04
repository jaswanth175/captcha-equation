from .views import home
# config/urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
   path('',home, name='home'),
]