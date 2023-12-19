# Generated by Django 5.0 on 2023-12-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_info', models.TextField()),
                ('available_price', models.TextField()),
                ('stock', models.TextField()),
            ],
            options={
                'db_table': 'product_data',
            },
        ),
    ]
