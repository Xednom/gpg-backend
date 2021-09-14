# Generated by Django 3.1.8 on 2021-08-27 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_remove_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='category',
            field=models.CharField(blank=True, choices=[('office_based', 'Office Based'), ('part_timers', 'Part-timers'), ('home_based', 'Home Based'), ('office_project_based_contract', 'Office Project Based Contract'), ('homebase_project_based_contract', 'Homebase - Project Based Contract'), ('part_time_job', 'Part-time Job')], default='office_based', max_length=50),
        ),
    ]