from django.db import models


class Student(models.Model):
    objects = True
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
