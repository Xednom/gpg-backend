# Generated by Django 3.1.6 on 2021-03-05 18:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=50)),
                (
                    "designation_category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("staff", "Staff"),
                            ("new_client", "New Client"),
                            ("current_client", "Current Client"),
                            ("affiliate_partner", "Affiliate Partner"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "company_category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("gpg_corporation", "GPG Corporation"),
                            ("land_master", "Landmaster.us"),
                            ("call_me_ph", "CallMe.com.ph"),
                            ("psalms_global", "Psalmsglobal.com"),
                            ("affiliate_partner", "Affiliate Partner"),
                        ],
                        max_length=40,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Client",
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
                ("client_code", models.CharField(blank=True, max_length=250)),
                (
                    "affiliate_partner_code",
                    models.CharField(blank=True, max_length=250),
                ),
                (
                    "affiliate_partner_name",
                    models.CharField(blank=True, max_length=250),
                ),
                ("pin", models.CharField(blank=True, max_length=5)),
                (
                    "lead_information",
                    models.TextField(
                        blank=True, help_text="Where did you hear about our company?"
                    ),
                ),
                ("customer_id", models.CharField(blank=True, max_length=250)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("blood_type", models.CharField(blank=True, max_length=50)),
                ("position", models.CharField(blank=True, max_length=250)),
                ("company_id", models.CharField(blank=True, max_length=50)),
                ("staff_id", models.CharField(blank=True, max_length=100)),
                ("phone_number", models.CharField(blank=True, max_length=50)),
                ("company_email", models.EmailField(blank=True, max_length=254)),
                ("start_date_hired", models.DateField(blank=True, null=True)),
                ("date_hired_in_contract", models.DateField(blank=True, null=True)),
                ("base_pay", models.CharField(blank=True, max_length=100)),
                ("hourly_rate", models.CharField(blank=True, max_length=100)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("regular", "Regular"),
                            ("probitionary", "Probitionary"),
                            ("inactive", "Inactive"),
                        ],
                        default="probitionary",
                        max_length=50,
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("office_based", "Office Based"),
                            ("part_timers", "Part-timers"),
                            ("home_based", "Home Based"),
                        ],
                        default="office_based",
                        max_length=50,
                    ),
                ),
                ("residential_address", models.TextField(blank=True)),
                ("tin_number", models.CharField(blank=True, max_length=250)),
                ("sss_number", models.CharField(blank=True, max_length=250)),
                ("pag_ibig_number", models.CharField(blank=True, max_length=250)),
                ("phil_health_number", models.CharField(blank=True, max_length=250)),
                (
                    "emergency_contact_full_name",
                    models.CharField(blank=True, max_length=250),
                ),
                ("relationship", models.CharField(blank=True, max_length=250)),
                (
                    "emergency_contact_number",
                    models.CharField(blank=True, max_length=250),
                ),
                ("mothers_full_name", models.CharField(blank=True, max_length=250)),
                ("mothers_maiden_name", models.CharField(blank=True, max_length=250)),
                ("fathers_full_name", models.CharField(blank=True, max_length=250)),
                ("bank_name", models.CharField(blank=True, max_length=250)),
                ("bank_account_name", models.CharField(blank=True, max_length=250)),
                ("bank_type", models.CharField(blank=True, max_length=250)),
                ("bank_account_number", models.CharField(blank=True, max_length=250)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="InternalFilesStaff",
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
                ("file_name", models.CharField(blank=True, max_length=250)),
                ("url", models.CharField(blank=True, max_length=250, null=True)),
                ("description", models.TextField(blank=True)),
                (
                    "staff",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="staff_files",
                        to="authentication.staff",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="InternalFiles",
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
                ("file_name", models.CharField(blank=True, max_length=250)),
                ("url", models.CharField(blank=True, max_length=250, null=True)),
                ("description", models.TextField(blank=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="client_files",
                        to="authentication.client",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
