# Generated by Django 3.2.9 on 2023-02-11 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0015_alter_user_designation_category"),
        ("gpg", "0047_buyerlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Acquisition",
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
                ("possible_offer", models.CharField(blank=True, max_length=250)),
                (
                    "approved_amount_from_client",
                    models.CharField(
                        blank=True,
                        choices=[("yes", "Yes"), ("no", "No")],
                        max_length=25,
                    ),
                ),
                ("minimum_amount", models.CharField(blank=True, max_length=250)),
                ("maximum_amount", models.CharField(blank=True, max_length=250)),
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
                        max_length=250,
                    ),
                ),
                ("notes", models.TextField(blank=True)),
                (
                    "assigned_sales_team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="assigned_sales_team_acquistion",
                        to="authentication.staff",
                    ),
                ),
                (
                    "property_detail",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="property_detail_acquisition",
                        to="gpg.propertydetail",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
