# from django.db import models

# Create your models here.
from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.DateField()




class Account(models.Model):
    UserName = models.CharField(max_length=100)
    RealName = models.CharField(max_length=100)
    accountNumber = models.IntegerField()
    balance = models.IntegerField()
