from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Product(models.Model):
    productname = models.CharField(max_length=100)
    productdescription = models.CharField(max_length=200)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='files/product_images')

