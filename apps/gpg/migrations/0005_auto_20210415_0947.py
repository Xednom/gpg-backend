# Generated by Django 3.1.8 on 2021-04-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0004_auto_20210415_0213"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobordergeneral",
            name="staff_email",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
