# webquicky/serializers.py
from rest_framework import serializers
from .models import Product
from .models import ProductImage
from .models  import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = [ "id", "name"]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "id","name", "price", "color", "Description1", "Description2", "offer", "offerFrom", "category"]
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = [ "id", "product", "imageSrc", "name"]