# Generated by Django 3.1.8 on 2021-10-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_accountfile_job_order_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountfile',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='logincredential',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
