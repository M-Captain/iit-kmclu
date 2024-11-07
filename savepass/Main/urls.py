from django.contrib import admin
from django.urls import path
from Main import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.login, name="login"),
    
]