# Generated by Django 3.2.9 on 2023-02-11 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0015_alter_user_designation_category"),
        ("gpg", "0051_assessmentfile"),
    ]

    operations = [
        migrations.CreateModel(
            name="MarketingFile",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("apn", models.CharField(max_length=250)),
                ("client_code", models.CharField(blank=True, max_length=250)),
                ("description", models.TextField(blank=True)),
                ("notes", models.TextField(blank=True)),
                ("description_of_request", models.TextField(blank=True)),
                ("completed_job_order_file", models.TextField(blank=True)),
                ("date_completed", models.DateField(blank=True, null=True)),
                (
                    "status_of_job",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("active", "Active"),
                            ("closed", "Closed"),
                            ("on_hold", "On Hold"),
                            ("canceled", "Canceled"),
                        ],
                        max_length=25,
                    ),
                ),
                (
                    "images",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "ad_content",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "youtube_videos",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "tiktok_videos",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "email_campaign",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "other_graphics",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "other_makerting_files",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "neighbor_list",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("yes", "Yes"),
                            ("no", "No"),
                            ("not_applicable", "Not Applicable"),
                        ],
                        default="not_applicable",
                        max_length=25,
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="marketing_file_assigned_to",
                        to="authentication.staff",
                    ),
                ),
                (
                    "property_detail",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="property_detail_marketing_file",
                        to="gpg.propertydetail",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
