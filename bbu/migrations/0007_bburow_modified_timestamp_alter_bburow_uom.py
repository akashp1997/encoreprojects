# Generated by Django 4.1.2 on 2022-10-10 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbu', '0006_alter_bburow_comment_alter_bburow_drawing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bburow',
            name='modified_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bburow',
            name='uom',
            field=models.CharField(default='P', max_length=256),
        ),
    ]
