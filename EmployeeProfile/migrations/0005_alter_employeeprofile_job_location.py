# Generated by Django 3.2.7 on 2022-02-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeProfile', '0004_auto_20211229_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='job_location',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
