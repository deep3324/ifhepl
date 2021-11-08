from django.db import models

# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

class EmployeeProfile(models.Model):
    emmloyeeid = models.CharField(max_length=14, default="",unique=True,)
    email = models.CharField(max_length=100, unique=True,)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    JOB_CHOICES = (
        ('DISTRICT DEVELOPMENT MANAGER', 'DISTRICT DEVELOPMENT MANAGER'),
        ('BLOCK DEVELOPMENT MANAGER', 'BLOCK DEVELOPMENT MANAGER'),
        ('FIELD EXECUTIVE', 'FIELD EXECUTIVE'),
        ('AGRICULTURAL ADVISOR', 'AGRICULTURAL ADVISOR'),
        ('COMPUTER TRAINER', 'COMPUTER TRAINER'),
        ('BEAUTICIAN', 'BEAUTICIAN'),
        ('TAILORING', 'TAILORING'),
        ('Office Boy/Peon', 'Office Boy/Peon'),
        ('Banking Trainer', 'Banking Trainer'),
        ('Regional Manager', 'Regional Manager'),
        ('Accountant/Cashier', 'Accountant/Cashier'),
        ('Receptionist', 'Receptionist'),
    )
    designation = models.CharField(max_length=32, choices=JOB_CHOICES)
    job_location = models.CharField(max_length=100, default="")
    bloodgroup = models.CharField(max_length=10, default="")
    dob = models.DateField()
    Address = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="Employee", blank=True, null=True)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"
