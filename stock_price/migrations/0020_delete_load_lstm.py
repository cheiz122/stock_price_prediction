# Generated by Django 4.2.6 on 2023-11-01 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0019_rename_close_price_stockprice_close_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='load_lstm',
        ),
    ]