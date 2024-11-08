# Generated by Django 3.1.8 on 2021-05-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("due_diligence", "0005_auto_20210518_0733"),
    ]

    operations = [
        migrations.AlterField(
            model_name="duediligencecallout",
            name="call_out_status",
            field=models.CharField(
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
                max_length=250,
            ),
        ),
        migrations.AlterField(
            model_name="duediligencecallout",
            name="initial_due_diligence_status",
            field=models.CharField(
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
                max_length=250,
            ),
        ),
    ]
