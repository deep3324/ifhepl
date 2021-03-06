# Generated by Django 3.2.7 on 2022-02-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifheplapp', '0009_auto_20220113_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_for', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('signature', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='healthcard',
            name='accept_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthcard',
            name='order_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='healthcard',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthcard',
            name='payment_mode',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='healthcard',
            name='payment_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='healthcard',
            name='razorpay_payment_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='healthcard',
            name='razorpay_signature',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='healthcard',
            name='transaction_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='accept_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='order_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='payment_mode',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='payment_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='razorpay_payment_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='razorpay_signature',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='kisancard',
            name='transaction_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='accept_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='membership',
            name='order_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='membership',
            name='payment_mode',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='payment_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='razorpay_payment_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='razorpay_signature',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='membership',
            name='transaction_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='employeeID',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='employeename',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='healthcard',
            name='reference_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='kisancard',
            name='employeeID',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='kisancard',
            name='employeename',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='kisancard',
            name='reference_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='membership',
            name='employeeID',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='membership',
            name='employeename',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='membership',
            name='reference_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]
