from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=7, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    dob = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=1, blank=True)





class KidProfile(models.Model):
    parent = models.ForeignKey(User, related_name='kids')
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)

    def __str__ (self):
        return self.name