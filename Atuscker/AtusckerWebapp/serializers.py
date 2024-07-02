# webquicky/serializers.py
from rest_framework import serializers
from .models import Product
from .models import ProductImage

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "id","name", "imageAlt", "price", "color", "Description1", "Description2"]
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [ "id","product", "imageSrc"]