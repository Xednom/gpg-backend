# Generated by Django 3.1.8 on 2021-11-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0008_auto_20211021_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffpaymenthistory',
            name='company_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
