# Generated by Django 3.1.8 on 2021-11-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0009_staffpaymenthistory_company_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenthistory',
            name='client_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
