# Generated by Django 4.2.6 on 2023-11-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0026_alter_lastloadeddate_last_loaded_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastloadeddate',
            name='last_loaded_date',
            field=models.DateTimeField(default='2023-07-07 00:00:00'),
        ),
    ]
