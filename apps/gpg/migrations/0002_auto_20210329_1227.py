# Generated by Django 3.1.6 on 2021-03-29 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("authentication", "0001_initial"),
        ("gpg", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CategoryType",
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
                ("category", models.CharField(max_length=250)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Deadline",
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
                ("deadline", models.CharField(max_length=250)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PropertyDetail",
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
                ("ticket_number", models.CharField(blank=True, max_length=150)),
                (
                    "property_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("sold", "Sold"),
                            ("available", "Available"),
                            ("in_escrow", "In Escrow"),
                            ("in_contract", "In Contract"),
                            ("ready_to_purchase", "Ready to Purchase"),
                            ("ready_for_contract", "Ready for Contract"),
                            ("canceled_transaction", "Canceled Transaction"),
                        ],
                        max_length=25,
                    ),
                ),
                ("client_email", models.CharField(blank=True, max_length=100)),
                ("staff_email", models.CharField(blank=True, max_length=100)),
                ("apn", models.CharField(max_length=250, unique=True)),
                ("county", models.CharField(max_length=250)),
                ("state", models.CharField(max_length=250)),
                ("size", models.CharField(max_length=250)),
                ("company_name", models.CharField(blank=True, max_length=250)),
                ("phone", models.CharField(blank=True, max_length=250)),
                ("email", models.CharField(blank=True, max_length=250)),
                ("website_url", models.CharField(blank=True, max_length=250)),
                ("file_storage", models.CharField(blank=True, max_length=500)),
                ("notes_client_side", models.TextField(blank=True)),
                ("notes_va_side", models.TextField(blank=True)),
                ("notes_management_side", models.TextField(blank=True)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_properties",
                        to="authentication.client",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="staff_assigned_properties",
                        to="authentication.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ["created_at"]},
        ),
        migrations.AlterModelOptions(
            name="jobordergeneral",
            options={"ordering": ["-ticket_number"]},
        ),
        migrations.AddField(
            model_name="jobordergeneral",
            name="client_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="jobordergeneral",
            name="staff_email",
            field=models.EmailField(blank=True, max_length=254),
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
                ],
                default="na",
                max_length=100,
            ),
        ),
        migrations.CreateModel(
            name="PropertyPrice",
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
                ("asking_price", models.CharField(max_length=250)),
                ("cash_terms", models.CharField(max_length=250)),
                ("finance_terms", models.TextField()),
                ("other_terms", models.TextField()),
                (
                    "price_status",
                    models.CharField(
                        blank=True,
                        choices=[("deactivate", "Deactivate"), ("active", "Active")],
                        default="active",
                        max_length=30,
                    ),
                ),
                ("notes", models.TextField()),
                ("updated_info", models.TextField(blank=True)),
                (
                    "property_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="property_price_statuses",
                        to="gpg.propertydetail",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_property_prices",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="JobOrderCategory",
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
                ("ticket_number", models.CharField(blank=True, max_length=100)),
                ("client_email", models.EmailField(blank=True, max_length=254)),
                ("staff_email", models.EmailField(blank=True, max_length=254)),
                (
                    "status",
                    models.CharField(
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
                        ],
                        default="na",
                        max_length=100,
                    ),
                ),
                ("due_date", models.DateField()),
                ("date_completed", models.DateField(blank=True, null=True)),
                ("job_description", models.TextField()),
                ("url_of_the_completed_jo", models.TextField(blank=True)),
                ("notes_va", models.TextField(blank=True)),
                ("notes_management", models.TextField(blank=True)),
                (
                    "total_time_consumed",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_order_categories",
                        to="gpg.categorytype",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_jo_by_categories",
                        to="authentication.client",
                    ),
                ),
                (
                    "deadline",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_order_deadline",
                        to="gpg.deadline",
                    ),
                ),
                (
                    "property_detail",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="apn_job_order_categories",
                        to="gpg.propertydetail",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="staff_job_orders_by_categories",
                        to="authentication.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CommentByApn",
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
                ("comment", models.TextField()),
                (
                    "job_order_category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="job_order_category_comments",
                        to="gpg.jobordercategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
    ]
