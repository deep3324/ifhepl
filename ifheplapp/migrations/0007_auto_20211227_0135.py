# Generated by Django 3.2.9 on 2021-12-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifheplapp', '0006_alter_membership_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcard',
            name='created',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kisancard',
            name='created',
            field=models.BooleanField(default=False),
        ),
    ]
