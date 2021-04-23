# Generated by Django 3.1.8 on 2021-04-23 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0005_auto_20210422_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(blank=True, max_length=250)),
                ('url', models.URLField(blank=True, max_length=500)),
                ('username', models.CharField(blank=True, max_length=250)),
                ('password', models.CharField(blank=True, max_length=250)),
                ('notes', models.TextField(blank=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_logins', to='authentication.client')),
                ('staff', models.ManyToManyField(blank=True, related_name='login_assigned_staffs', to='authentication.Staff')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
