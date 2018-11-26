from __future__ import unicode_literals

from django.db import models
from babysitters.models import Babysitter
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(User)
    babysitter = models.ForeignKey(Babysitter)
    quantity = models.IntegerField()

    def __str__(self):
        return "{0} ({1})".format(self.babysitter.firstName, self.quantity)