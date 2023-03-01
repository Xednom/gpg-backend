# Generated by Django 3.2.9 on 2022-10-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0040_remove_jobordergeneral_updated_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobordergeneral",
            name="days_after_due_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="jobordergeneral",
            name="days_before_due_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]