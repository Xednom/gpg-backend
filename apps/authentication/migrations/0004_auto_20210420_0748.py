# Generated by Django 3.1.8 on 2021-04-20 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0003_auto_20210419_1042"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="staff",
            options={"ordering": ["user"]},
        ),
    ]
