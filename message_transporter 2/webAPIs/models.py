from django.db import models
from webAPIs.database_connection import DatabaseHandler


class Product_Data(models.Model):
    id = models.AutoField(primary_key=True)
    meta_info = models.TextField()
    available_price = models.CharField(max_length=255)
    stock = models.CharField(max_length=255)
    source = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'product_data'
