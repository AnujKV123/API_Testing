from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('SaveOTPContact', views.SaveOTPContact, name='SaveOTPContact'),
    path('VerifyOTP', views.VerifyOTP, name='VerifyOTP'),
]