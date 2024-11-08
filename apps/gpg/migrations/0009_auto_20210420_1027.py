# Generated by Django 3.1.8 on 2021-04-20 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0008_propertydetailfile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobordercategory",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("na", "N/A"),
                    ("job_order_request", "Job order request"),
                    ("va_processing", "VA Processing"),
                    ("management_processing", "Management Processing"),
                    ("verified_job_order", "Verified Job Order"),
                    ("on_hold", "On Hold"),
                    ("canceled", "Canceled"),
                    ("follow_up", "Follow up"),
                    ("dispute", "Dispute"),
                    ("complete", "Complete"),
                    ("under_quality_review", "Under Quality Review"),
                    ("daily_tasks", "Daily Tasks"),
                    ("weekly_tasks", "Weekly Tasks"),
                    ("monthly_tasks", "Monthly Tasks"),
                    ("redo", "Redo"),
                ],
                default="na",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="jobordergeneral",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("na", "N/A"),
                    ("job_order_request", "Job order request"),
                    ("va_processing", "VA Processing"),
                    ("management_processing", "Management Processing"),
                    ("verified_job_order", "Verified Job Order"),
                    ("on_hold", "On Hold"),
                    ("canceled", "Canceled"),
                    ("follow_up", "Follow up"),
                    ("dispute", "Dispute"),
                    ("complete", "Complete"),
                    ("under_quality_review", "Under Quality Review"),
                    ("daily_tasks", "Daily Tasks"),
                    ("weekly_tasks", "Weekly Tasks"),
                    ("monthly_tasks", "Monthly Tasks"),
                    ("redo", "Redo"),
                ],
                default="na",
                max_length=100,
            ),
        ),
    ]
