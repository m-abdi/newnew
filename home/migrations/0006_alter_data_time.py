# Generated by Django 4.0.2 on 2022-02-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_data_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.FloatField(default=1645628692.887641),
        ),
    ]
