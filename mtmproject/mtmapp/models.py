from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    marks = models.IntegerField()
    def __str__(self):
        return self.name

class Course(models.Model):
    student = models.ManyToManyField(Student,related_name=None)
    course = models.CharField(max_length=20)
    fee = models.FloatField()
    def __str__(self):
        return self.course
