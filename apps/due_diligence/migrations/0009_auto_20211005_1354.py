# Generated by Django 3.1.8 on 2021-10-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("due_diligence", "0008_auto_20210607_1905"),
    ]

    operations = [
        migrations.AddField(
            model_name="duediligencecallout",
            name="tax_data_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("complete", "Complete"),
                    ("pending", "Pending"),
                    ("on_hold", "On Hold"),
                    ("cancelled", "Cancelled"),
                    ("for_follow_up", "For Follow Up"),
                    ("processing", "Processing"),
                    ("not_applicable", "Not Applicable"),
                    ("job_request", "Job order request"),
                    ("tax_data_complete", "Tax Data- Complete"),
                    ("zoning_data_complete", "Zoning Data - Complete"),
                    ("utilities_data_complete", "Utilities Data - Complete"),
                    ("tax_zoning_data_complete", "Tax/Zoning Data- Complete"),
                    ("tax_utlities_data_complete", "Tax/Utilies Data - Complete "),
                    (
                        "zoning_utilities_data_complete",
                        "Zoning/Utilities Data- Complete",
                    ),
                ],
                default="processing",
                max_length=250,
            ),
        ),
        migrations.AddField(
            model_name="duediligencecallout",
            name="utilities_data_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("complete", "Complete"),
                    ("pending", "Pending"),
                    ("on_hold", "On Hold"),
                    ("cancelled", "Cancelled"),
                    ("for_follow_up", "For Follow Up"),
                    ("processing", "Processing"),
                    ("not_applicable", "Not Applicable"),
                    ("job_request", "Job order request"),
                    ("tax_data_complete", "Tax Data- Complete"),
                    ("zoning_data_complete", "Zoning Data - Complete"),
                    ("utilities_data_complete", "Utilities Data - Complete"),
                    ("tax_zoning_data_complete", "Tax/Zoning Data- Complete"),
                    ("tax_utlities_data_complete", "Tax/Utilies Data - Complete "),
                    (
                        "zoning_utilities_data_complete",
                        "Zoning/Utilities Data- Complete",
                    ),
                ],
                default="processing",
                max_length=250,
            ),
        ),
        migrations.AddField(
            model_name="duediligencecallout",
            name="zoning_data_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("complete", "Complete"),
                    ("pending", "Pending"),
                    ("on_hold", "On Hold"),
                    ("cancelled", "Cancelled"),
                    ("for_follow_up", "For Follow Up"),
                    ("processing", "Processing"),
                    ("not_applicable", "Not Applicable"),
                    ("job_request", "Job order request"),
                    ("tax_data_complete", "Tax Data- Complete"),
                    ("zoning_data_complete", "Zoning Data - Complete"),
                    ("utilities_data_complete", "Utilities Data - Complete"),
                    ("tax_zoning_data_complete", "Tax/Zoning Data- Complete"),
                    ("tax_utlities_data_complete", "Tax/Utilies Data - Complete "),
                    (
                        "zoning_utilities_data_complete",
                        "Zoning/Utilities Data- Complete",
                    ),
                ],
                default="processing",
                max_length=250,
            ),
        ),
    ]
