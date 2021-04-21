# Generated by Django 3.1.8 on 2021-04-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpg', '0009_auto_20210420_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyprice',
            name='asking_price',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='propertyprice',
            name='cash_terms',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='propertyprice',
            name='finance_terms',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='propertyprice',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='propertyprice',
            name='other_terms',
            field=models.TextField(blank=True),
        ),
    ]