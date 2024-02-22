# Generated by Django 4.2.6 on 2023-11-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0029_delete_lastloadeddate'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastLoadedDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('last_loaded_date', models.DateTimeField(default='2023-10-10 00:00:00')),
            ],
        ),
    ]