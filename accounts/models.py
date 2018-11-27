from __future__ import unicode_literals
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to='images', default='Upload Picture')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=20, null=True)
    county = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=7, null=True)
    biography = models.TextField(max_length=280,blank=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True)
    dob = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)

class KidProfile(models.Model):
    parent = models.ForeignKey(User, related_name='kids')
    name = models.CharField(max_length=255, null=True, blank=True)
    dob = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    needs = models.CharField(max_length=3, null=True, blank=True)

    def __str__ (self):
        return self.name