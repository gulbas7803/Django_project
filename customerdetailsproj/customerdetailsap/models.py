from django.db import models


# Create your models here.

class CustomerData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    sales = models.IntegerField()
