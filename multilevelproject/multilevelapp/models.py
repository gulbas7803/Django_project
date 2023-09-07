from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

class Student(Person):
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()

class Employee(Student):
    salary = models.FloatField()
    company = models.CharField(max_length=30)
    company_location = models.CharField(max_length=30)

