# Generated by Django 3.1.8 on 2021-04-22 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210420_0748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['user__first_name']},
        ),
    ]
