# Generated by Django 3.2.9 on 2023-01-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0043_auto_20230120_1811"),
    ]

    operations = [
        migrations.AddField(
            model_name="propertydetail",
            name="property_complete_address",
            field=models.TextField(blank=True),
        ),
    ]
