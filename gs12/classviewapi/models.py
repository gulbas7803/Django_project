from django.db import models


# Create your models here.
class Student(models.Model):
    objects = True
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    location = models.CharField(max_length=100)
