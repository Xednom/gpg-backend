# Generated by Django 3.1.8 on 2021-10-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0007_accountbalance_billing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbalance',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='accountcharge',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='paymentportal',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='staffaccountbalance',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='staffpaymenthistory',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]