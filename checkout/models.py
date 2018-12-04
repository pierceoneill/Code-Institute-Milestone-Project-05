from django.db import models
from babysitters.models import Babysitter
from accounts.models import UserProfile

class Order(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=20, null=True)
    county = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=7, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return "{0}".format(self.user)
        
        
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    babysitter = models.ForeignKey(Babysitter, null=False)
    quantity = models.IntegerField(blank=False)
    def __str__(self):
        return "{0} {1} {2} @ {3}".format(self.quantity, self.babysitter.firstName, self.babysitter.quantity, self.babysitter.price)
        