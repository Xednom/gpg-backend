# Generated by Django 3.1.8 on 2021-04-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210415_0213'),
        ('gpg', '0003_county_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'Counties'},
        ),
        migrations.AlterModelOptions(
            name='jobordercategory',
            options={'verbose_name_plural': 'Job Order Categories'},
        ),
        migrations.RemoveField(
            model_name='jobordercategory',
            name='staff',
        ),
        migrations.AddField(
            model_name='jobordercategory',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='staff_job_orders_by_categories', to='authentication.Staff'),
        ),
        migrations.RemoveField(
            model_name='jobordergeneral',
            name='va_assigned',
        ),
        migrations.AddField(
            model_name='jobordergeneral',
            name='va_assigned',
            field=models.ManyToManyField(blank=True, related_name='vas_job_orders', to='authentication.Staff'),
        ),
        migrations.RemoveField(
            model_name='propertydetail',
            name='staff',
        ),
        migrations.AddField(
            model_name='propertydetail',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='staff_assigned_properties', to='authentication.Staff'),
        ),
    ]