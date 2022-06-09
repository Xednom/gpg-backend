# Generated by Django 3.1.8 on 2021-08-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0023_auto_20210811_2228"),
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
                    ("closed", "Closed"),
                    ("under_quality_review", "Under Quality Review"),
                    ("daily_tasks", "Daily Tasks"),
                    ("weekly_tasks", "Weekly Tasks"),
                    ("monthly_tasks", "Monthly Tasks"),
                    ("redo", "Redo"),
                    ("pending", "Pending"),
                    ("request_for_posting", "Request for Posting"),
                    ("mark_as_sold_request", "Mark as Sold Request"),
                    ("initial_dd_processing", "Initial DD Processing"),
                    ("initial_dd_complete", "Initial DD Complete"),
                    ("dd_call_out_processing", "DD Call Out Processing"),
                    ("dd_call_out_complete", "DD Call Out Complete"),
                    ("duplicate_request", "Duplicate Request"),
                    ("multiple_task", "Multiple Task"),
                    ("va_assigned_multiple_task", "VA assigned Multiple Task"),
                    ("va_processing_multiple_task", "VA processing Multiple Task"),
                    ("va_complete_multiple_task", "VA Complete Multiple Task"),
                    (
                        "for_quality_review_multiple_task",
                        "For Quality Review Multiple Task",
                    ),
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
                    ("closed", "Closed"),
                    ("under_quality_review", "Under Quality Review"),
                    ("daily_tasks", "Daily Tasks"),
                    ("weekly_tasks", "Weekly Tasks"),
                    ("monthly_tasks", "Monthly Tasks"),
                    ("redo", "Redo"),
                    ("pending", "Pending"),
                    ("request_for_posting", "Request for Posting"),
                    ("mark_as_sold_request", "Mark as Sold Request"),
                    ("initial_dd_processing", "Initial DD Processing"),
                    ("initial_dd_complete", "Initial DD Complete"),
                    ("dd_call_out_processing", "DD Call Out Processing"),
                    ("dd_call_out_complete", "DD Call Out Complete"),
                    ("duplicate_request", "Duplicate Request"),
                    ("multiple_task", "Multiple Task"),
                    ("va_assigned_multiple_task", "VA assigned Multiple Task"),
                    ("va_processing_multiple_task", "VA processing Multiple Task"),
                    ("va_complete_multiple_task", "VA Complete Multiple Task"),
                    (
                        "for_quality_review_multiple_task",
                        "For Quality Review Multiple Task",
                    ),
                ],
                default="na",
                max_length=100,
            ),
        ),
    ]
