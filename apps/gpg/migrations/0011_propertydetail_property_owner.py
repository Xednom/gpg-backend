# Generated by Django 3.1.8 on 2021-04-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpg', '0010_auto_20210421_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetail',
            name='property_owner',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]