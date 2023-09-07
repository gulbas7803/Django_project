from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

class Trainer(models.Model):
    tid = models.AutoField(primary_key=True)
    trainer = models.CharField(max_length=30)
    salary = models.IntegerField()
    company = models.CharField(max_length=30)


class Course(models.Model):
    course = models.CharField(max_length=30)
    fee = models.IntegerField()
    duration = models.CharField(max_length=30)

class Book(Student,Trainer,Course):
    book_name = models.CharField(max_length=30)
    cost = models.IntegerField()
    author = models.CharField(max_length=30)

