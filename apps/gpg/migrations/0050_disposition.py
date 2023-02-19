# Generated by Django 3.2.9 on 2023-02-11 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0015_alter_user_designation_category"),
        ("gpg", "0049_acquisition_client_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disposition",
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
                ("client_code", models.CharField(max_length=250)),
                ("selling_price", models.CharField(blank=True, max_length=250)),
                ("discounted_cash_price", models.CharField(blank=True, max_length=250)),
                ("selling_price_minimum", models.CharField(blank=True, max_length=250)),
                ("selling_price_maximum", models.CharField(blank=True, max_length=250)),
                ("financed_terms", models.TextField(blank=True)),
                ("amount_closed_deal", models.CharField(blank=True, max_length=250)),
                (
                    "deal_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("pending", "Pending"),
                            ("sold", "Sold"),
                            ("on_hold", "On Hold"),
                            ("on_going_negotiation", "On going negotiation"),
                            ("drop_deal", "Drop Deal"),
                        ],
                        default="pending",
                        max_length=250,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                (
                    "assigned_sales_team",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="disposition_staff",
                        to="authentication.staff",
                    ),
                ),
                (
                    "property_detail",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="property_detail_disposition",
                        to="gpg.propertydetail",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
