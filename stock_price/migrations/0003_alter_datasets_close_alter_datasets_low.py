# Generated by Django 4.2.6 on 2023-10-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0002_alter_datasets_close_alter_datasets_high_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='close',
            field=models.CharField(max_length=255, verbose_name='Close'),
        ),
        migrations.AlterField(
            model_name='datasets',
            name='low',
            field=models.CharField(max_length=255, verbose_name='Low'),
        ),
    ]
