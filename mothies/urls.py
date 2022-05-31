from django.contrib import admin
from django.urls import path

from .views import about, contact, home

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about/', about),
]
