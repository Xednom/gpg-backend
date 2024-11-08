# Generated by Django 3.2.9 on 2022-01-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0013_auto_20211111_2146"),
        ("gpg", "0034_jobordercategoryagentscoring_jobordergeneralagentscoring"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobordergeneralagentscoring",
            name="staff",
        ),
        migrations.AddField(
            model_name="jobordergeneralagentscoring",
            name="staff",
            field=models.ManyToManyField(
                blank=True,
                related_name="job_order_general_staff_scorings",
                to="authentication.Staff",
            ),
        ),
    ]
