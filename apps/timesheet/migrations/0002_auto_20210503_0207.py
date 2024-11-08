# Generated by Django 3.1.8 on 2021-05-03 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("timesheet", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="accountcharge",
            options={"ordering": ["-id"]},
        ),
        migrations.RenameField(
            model_name="accountbalance",
            old_name="amount_due",
            new_name="account_charges",
        ),
        migrations.RenameField(
            model_name="accountbalance",
            old_name="amount_due_currency",
            new_name="account_charges_currency",
        ),
    ]
