# Generated by Django 4.2.6 on 2023-10-31 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0017_load_lstm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockprice',
            old_name='timestamp',
            new_name='date',
        ),
    ]