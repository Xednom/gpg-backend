# Generated by Django 3.2.9 on 2023-03-01 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="company",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Company",
                "verbose_name_plural": "Companies",
            },
        ),
    ]
