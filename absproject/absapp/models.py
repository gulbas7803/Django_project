from django.db import models

# Create your models here.
class CommanData(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    class Meta:
        abstract = True

class Student( CommanData):
    marks = models.IntegerField()

class Empolyees( CommanData):
    salary = models.IntegerField()

class Customers( CommanData):
    sales = models.IntegerField()
