from django.db import models


class Company(models.Model):
    objects = True
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('it', 'it'),
                                                     ('non it', 'non it'),
                                                     ('mobiles phones', 'mobiles phones')
                                                     ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    objects = True
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=64)
    phone = models.BigIntegerField()
    about = models.TextField(max_length=64)
    position = models.CharField(max_length=64, choices=(('manager', 'manager'),
                                ('software_developer', 'software_developer'),
                                                        ('trainer', 'trainer'),
                                                        ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
