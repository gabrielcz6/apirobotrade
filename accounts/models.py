# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
     name = models.CharField(null=True, blank=True, max_length=100)
     license_key = models.CharField(max_length=100, blank=True, null=True)
     license_expiry_date = models.DateField(blank=True, null=True)
     hdd=models.CharField(null=True, blank=True, max_length=100)
   

