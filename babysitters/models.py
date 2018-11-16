from django.db import models
from datetime import datetime

# Create your models here.
class Babysitter(models.Model):
    list_display = ('firstName', 'lastName', 'minderType')
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    minderType = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='images')
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=20, null=True)
    county = models.CharField(max_length=100, null=True)
    eircode = models.CharField(max_length=7, null=True)
    biography = models.TextField(max_length=280,blank=True)
    def __str__(self):
        return self.firstName + ' ' + self.lastName