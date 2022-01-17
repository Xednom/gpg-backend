# Generated by Django 3.2.9 on 2022-01-13 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField()),
                ('email_template_title', models.CharField(max_length=255)),
                ('url_link', models.TextField()),
                ('email_template_description', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('created_by', models.CharField(max_length=255)),
                ('company_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_email_templates', to='core.company')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]