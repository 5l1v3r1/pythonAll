from django.contrib import admin
from django.urls import path

app_name = "article"

from . import views

urlpatterns = [
    path('create/', views.index),
]