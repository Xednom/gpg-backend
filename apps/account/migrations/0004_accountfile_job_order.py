# Generated by Django 3.1.8 on 2021-09-10 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0011_auto_20210827_2001"),
        ("account", "0003_accountfile"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountfile",
            name="job_order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="job_order_account_files",
                to="authentication.client",
            ),
        ),
    ]
