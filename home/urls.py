from django.contrib import admin
from django.urls import path

from home.views import home, index

urlpatterns = [
    path('', home, name="home"),
    path('index', index, name="index"),


]
