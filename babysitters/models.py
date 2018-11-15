from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Babysitter(models.Model):
    firstName = models.CharField(max_length=50, blank=True, null=True)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    minderType = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    location = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    donator = models.BooleanField(default=False)
    
class Experience(models.Model):
    """This is the model holding the users Experience information"""
    babysitter = models.ForeignKey(Babysitter, related_name='experience')
    jobTitle = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    dateFrom = models.DateField(auto_now=False, auto_now_add=False)
    dateTo = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    current = models.BooleanField(default=False)
    


def __str__(self):
    return self.name