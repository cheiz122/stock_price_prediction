# Generated by Django 4.2.6 on 2023-10-18 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasets',
            name='close',
            field=models.FloatField(max_length=255, verbose_name='Close'),
        ),
        migrations.AlterField(
            model_name='datasets',
            name='high',
            field=models.CharField(max_length=255, verbose_name='High'),
        ),
        migrations.AlterField(
            model_name='datasets',
            name='low',
            field=models.FloatField(max_length=255, verbose_name='Low'),
        ),
        migrations.AlterField(
            model_name='datasets',
            name='open',
            field=models.CharField(max_length=255, verbose_name='Open'),
        ),
    ]