from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('registration/', views.user_registration, name='registration'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]