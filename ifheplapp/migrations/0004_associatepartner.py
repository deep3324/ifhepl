# Generated by Django 3.2.7 on 2021-12-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifheplapp', '0003_alter_attendance_uploaded_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssociatePartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partnerName', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
