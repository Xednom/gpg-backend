# Generated by Django 3.1.8 on 2021-10-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("due_diligence", "0009_auto_20211005_1354"),
    ]

    operations = [
        migrations.AlterField(
            model_name="duediligencecallout",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="phonelineextension",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
