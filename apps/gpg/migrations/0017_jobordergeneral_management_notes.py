# Generated by Django 3.1.8 on 2021-05-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpg', '0016_auto_20210504_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobordergeneral',
            name='management_notes',
            field=models.TextField(blank=True),
        ),
    ]
