# Generated by Django 3.1.8 on 2021-10-22 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0027_jobordercategoryanalytics"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobordercategoryanalytics",
            old_name="date",
            new_name="month",
        ),
        migrations.AddField(
            model_name="jobordercategoryanalytics",
            name="month_year",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
