# Generated by Django 3.1.8 on 2021-05-14 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0010_remove_client_email"),
        ("due_diligence", "0002_phonelineextension_original_extension_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="DueDiligenceCallOut",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("ticket_number", models.CharField(blank=True, max_length=250)),
                ("dd_link", models.CharField(blank=True, max_length=500)),
                (
                    "assessor_website",
                    models.TextField(
                        blank=True,
                        help_text="For Assessed Value & Market Value of the property",
                    ),
                ),
                (
                    "assessor_contact",
                    models.TextField(
                        blank=True,
                        help_text="For Assessed Value & Market Value of the property",
                    ),
                ),
                (
                    "treasurer_website",
                    models.TextField(blank=True, help_text="For Tax Data Collection"),
                ),
                (
                    "treasurer_contact",
                    models.TextField(blank=True, help_text="For Tax Data Collection"),
                ),
                (
                    "recorder_clerk_website",
                    models.TextField(
                        blank=True, help_text="For Covenance , Restriction & Deeds"
                    ),
                ),
                (
                    "recorder_clerk_contact",
                    models.TextField(
                        blank=True, help_text="For Covenance , Restriction & Deeds"
                    ),
                ),
                (
                    "zoning_or_planning_department_website",
                    models.TextField(
                        blank=True, help_text="For Zoning Data Collection"
                    ),
                ),
                (
                    "zoning_or_planning_department_contact",
                    models.TextField(
                        blank=True, help_text="For Zoning Data Collection"
                    ),
                ),
                (
                    "county_environmental_health_department_website",
                    models.TextField(
                        blank=True,
                        help_text="For Utilities - Septic, Sewer and Water Data Collection",
                    ),
                ),
                (
                    "county_environmental_health_department_contact",
                    models.TextField(
                        blank=True,
                        help_text="For Utilities - Septic, Sewer and Water Data Collection",
                    ),
                ),
                (
                    "gis_website",
                    models.TextField(blank=True, help_text="For property map viewing"),
                ),
                (
                    "cad_website",
                    models.TextField(blank=True, help_text="For property map viewing"),
                ),
                (
                    "electricity_company_name_and_phone_number",
                    models.TextField(
                        blank=True,
                        help_text="For Utilities - Electricity Data Collection",
                    ),
                ),
                (
                    "water_company_name_and_phone_number",
                    models.TextField(
                        blank=True,
                        help_text="For Utilities - Septic, Sewer and Water Data Collection",
                    ),
                ),
                (
                    "sewer_company_name_and_phone_number",
                    models.TextField(
                        blank=True,
                        help_text="For Utilities - Septic, Sewer and Water Data Collection",
                    ),
                ),
                (
                    "gas_company_name_and_phone_number",
                    models.TextField(
                        blank=True,
                        help_text="For Utilities - Septic, Sewer and Water Data Collection",
                    ),
                ),
                (
                    "waste_company_name_and_phone_number",
                    models.TextField(
                        blank=True,
                        help_text="For Utilities - Septic, Sewer and Water Data Collection",
                    ),
                ),
                ("apn", models.CharField(max_length=250)),
                ("county", models.CharField(blank=True, max_length=250)),
                ("state", models.CharField(blank=True, max_length=250)),
                ("memo_call_notes", models.TextField(blank=True)),
                ("dd_specialists_additional_info", models.TextField(blank=True)),
                (
                    "initial_due_diligence_status",
                    models.CharField(
                        choices=[
                            ("complete", "Complete"),
                            ("pending", "Pending"),
                            ("on_hold", "On Hold"),
                            ("cancelled", "Cancelled"),
                            ("for_follow_up", "For Follow Up"),
                            ("processing", "Processing"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        max_length=250,
                    ),
                ),
                ("initial_dd_date_complete", models.DateField(blank=True, null=True)),
                (
                    "call_out_status",
                    models.CharField(
                        choices=[
                            ("complete", "Complete"),
                            ("pending", "Pending"),
                            ("on_hold", "On Hold"),
                            ("cancelled", "Cancelled"),
                            ("for_follow_up", "For Follow Up"),
                            ("processing", "Processing"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        max_length=250,
                    ),
                ),
                ("call_out_dd_date_complete", models.DateField(blank=True, null=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="call_out_clients",
                        to="authentication.client",
                    ),
                ),
                (
                    "staff_assigned_for_call_out",
                    models.ManyToManyField(
                        related_name="staff_assigned_call_out_due_diligences",
                        to="authentication.Staff",
                    ),
                ),
                (
                    "staff_initial_dd",
                    models.ManyToManyField(
                        related_name="staff_initial_due_diligences",
                        to="authentication.Staff",
                    ),
                ),
            ],
            options={
                "ordering": ["-ticket_number"],
            },
        ),
    ]
