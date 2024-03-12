# django_project/urls.py
from django.contrib import admin
from django.urls import path, include # new
from .views import LicenseExpiryDateAPIView,UpdateHddAPIView

urlpatterns = [
path('license-expiry-date/', LicenseExpiryDateAPIView.as_view(), name='license_expiry_date'),
path('update-hdd/', UpdateHddAPIView.as_view(), name='update_hdd'),
]
