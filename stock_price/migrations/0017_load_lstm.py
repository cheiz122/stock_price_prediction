# Generated by Django 4.2.6 on 2023-10-31 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0016_delete_load_lstm'),
    ]

    operations = [
        migrations.CreateModel(
            name='load_lstm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('model_path', models.CharField(max_length=255)),
            ],
        ),
    ]
