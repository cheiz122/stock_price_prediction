# Generated by Django 4.2.6 on 2023-10-31 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0013_stockprice_delete_datasets'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockPrice',
        ),
    ]