# Generated by Django 3.1.8 on 2021-05-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0015_auto_20210429_1318"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobordergeneral",
            name="staff_email",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
