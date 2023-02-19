# Generated by Django 3.1.8 on 2021-05-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentication", "0010_remove_client_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="PhoneLineExtension",
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
                ("user_id", models.CharField(max_length=250)),
                ("code_name", models.CharField(max_length=250)),
                ("allocation_company", models.CharField(max_length=250)),
                (
                    "allocated_extension_staff",
                    models.ManyToManyField(
                        related_name="allocated_extension_staffs",
                        to="authentication.Staff",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]
