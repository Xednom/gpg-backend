# Generated by Django 3.1.8 on 2021-04-23 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0012_jobordergeneral_url_of_the_completed_jo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jobordercategory",
            options={
                "ordering": ["-id"],
                "verbose_name_plural": "Job Order Categories",
            },
        ),
        migrations.AlterModelOptions(
            name="jobordergeneral",
            options={"ordering": ["-id"]},
        ),
    ]
