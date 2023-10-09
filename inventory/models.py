from django.db import models

# Create your models here.
class userInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=44,unique=True)
    password = models.CharField(max_length=44)




class inventoryInfo(models.Model):
    item_name      = models.CharField(primary_key=True,max_length=99)
    variation_name = models.CharField(max_length=99)
    barcode        = models.CharField(max_length=99)
    category       = models.CharField(max_length=99)
    price          = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_Tokyo = models.CharField(max_length=99)