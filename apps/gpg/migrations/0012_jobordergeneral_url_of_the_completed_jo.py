# Generated by Django 3.1.8 on 2021-04-22 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0011_propertydetail_property_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobordergeneral",
            name="url_of_the_completed_jo",
            field=models.TextField(blank=True),
        ),
    ]
