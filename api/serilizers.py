from rest_framework import serializers
from products.models import Category, Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category

