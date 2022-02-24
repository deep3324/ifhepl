from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class EmployeeProfile(models.Model):
    emmloyeeid = models.CharField(max_length=14, default="", unique=True,)
    email = models.CharField(max_length=100, unique=True,)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(
        max_length=10, unique=True, null=False, blank=False)
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
        ('Vendor', 'Vendor'),
    )
    designation = models.CharField(max_length=32, choices=JOB_CHOICES)
    job_location = models.CharField(max_length=100, default="", blank=True)
    bloodgroup = models.CharField(max_length=10, default="")
    dob = models.DateField()
    can_accept_cash = models.BooleanField(default=False)
    Address = models.CharField(max_length=500, default="")
    image = models.ImageField(upload_to="Employee", blank=True, null=True)
    total_health_card_created = models.IntegerField(default=0)
    total_kisan_card_created = models.IntegerField(default=0)
    total_membership_card_created = models.IntegerField(default=0)
    current_month_health_card_created = models.IntegerField(default=0)
    current_month_kisan_card_created = models.IntegerField(default=0)
    current_month_membership_card_created = models.IntegerField(default=0)
    previous_month_health_card_created = models.IntegerField(default=0)
    previous_month_kisan_card_created = models.IntegerField(default=0)
    previous_month_membership_card_created = models.IntegerField(default=0)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"
        verbose_name_plural = "Employee Profiles"

    def __str__(self):
        return self.name + " (" + self.emmloyeeid + ")"
