from . import views
from django.urls import path
from django.contrib import admin
from .views import RegisterUserApiView

urlpatterns = [
    path('register/', RegisterUserApiView.as_view(), name='register')
]