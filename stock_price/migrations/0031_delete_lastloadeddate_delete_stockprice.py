# Generated by Django 4.2.6 on 2023-11-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0030_lastloadeddate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LastLoadedDate',
        ),
        migrations.DeleteModel(
            name='StockPrice',
        ),
    ]