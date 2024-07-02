from django.db import models
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, blank=True)
    imageAlt= models.CharField(max_length=50, blank=True)
    price = models.IntegerField(null=True)
    color = models.CharField(max_length=20, blank=True)
    Description1 = models.CharField(max_length=200, blank=True)
    Description2 = models.CharField(max_length=200, blank=True)

    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    imageSrc = models.URLField(max_length=255, blank=True)

