# Generated by Django 3.1.8 on 2021-05-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('due_diligence', '0004_phonelineextension_allocation_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duediligencecallout',
            name='call_out_status',
            field=models.CharField(choices=[('complete', 'Complete'), ('pending', 'Pending'), ('on_hold', 'On Hold'), ('cancelled', 'Cancelled'), ('for_follow_up', 'For Follow Up'), ('processing', 'Processing'), ('not_applicable', 'Not Applicable'), ('job_request', 'Job order request')], max_length=250),
        ),
        migrations.AlterField(
            model_name='duediligencecallout',
            name='initial_due_diligence_status',
            field=models.CharField(choices=[('complete', 'Complete'), ('pending', 'Pending'), ('on_hold', 'On Hold'), ('cancelled', 'Cancelled'), ('for_follow_up', 'For Follow Up'), ('processing', 'Processing'), ('not_applicable', 'Not Applicable'), ('job_request', 'Job order request')], max_length=250),
        ),
    ]