# Generated by Django 5.0 on 2023-12-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webAPIs', '0002_alter_product_data_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_data',
            name='available_price',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='product_data',
            name='stock',
            field=models.CharField(),
        ),
    ]
