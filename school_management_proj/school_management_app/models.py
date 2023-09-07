from django.db import models

class Register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.EmailField()
    date_of_birth=models.DateField(auto_now=True)
    image=models.ImageField(upload_to="static/img/")
    status=models.BooleanField(default=True)
    password=models.CharField(max_length=20)


class Login(models.Model):
    phone_no=models.BigIntegerField()
    password=models.CharField(max_length=20)
