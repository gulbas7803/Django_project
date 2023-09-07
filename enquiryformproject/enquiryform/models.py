from django.db import models
from multiselectfield import multiselectfield

# Create your models here.

class EnquiryFormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    mobile = models.BigIntegerField()
    courses_choices = (
        ('py','python'),
        ('dj','django'),
        ('fk','flask'),
        ('my','mysql')
    )
    courses = multiselectfield(choices=courses_choices, Max_length=200)

    location_choices = (
        ('hyd','hyderabad'),
        ('bang','bengluru'),
        ('mumb','mumbai'),
        ('delhi','delhi')
    )
    location = multiselectfield(choices=location_choices,Max_lenght=200)

    shift_choices = (
        ('mrg', 'morging'),
        ('aftr', 'afternoon'),
        ('evng', 'evening'),
        ('ngt', 'night')
    )
    shift = multiselectfield(choices=shift_choices, Max_lenght=200)

    start_date = models.DateField(max_length=100)
    gender = models.CharField(max_length=100)   



