# Generated by Django 3.2.9 on 2021-12-17 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gpg", "0032_jobordercategoryrating_jobordergeneralrating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobordercategoryrating",
            name="job_order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="job_category_ratings",
                to="gpg.jobordercategory",
            ),
        ),
    ]
