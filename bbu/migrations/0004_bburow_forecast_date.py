# Generated by Django 4.1.2 on 2022-10-09 07:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bbu', '0003_project_addendum'),
    ]

    operations = [
        migrations.AddField(
            model_name='bburow',
            name='forecast_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
