# Generated by Django 3.1.8 on 2021-04-29 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210422_0842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['user__first_name']},
        ),
    ]