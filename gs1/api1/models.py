from django.db import models


# Create your models here.

class Student(models.Model):
    objects = True
    name = models.CharField(max_length=64)
    roll = models.IntegerField()
    city = models.CharField(max_length=30)
