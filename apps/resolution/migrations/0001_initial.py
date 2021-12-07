# Generated by Django 3.2.9 on 2021-12-07 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0013_auto_20211111_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_submitted', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('resolution_provided_by_management', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In progress'), ('on_hold', 'On hold'), ('closed', 'Closed'), ('resolution_provided', 'Resolution provided')], default='pending', max_length=255)),
                ('additional_notes', models.TextField(blank=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.staff')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='resolution.category')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.client')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
