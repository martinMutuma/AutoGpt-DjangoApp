from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'title', 'description', 'slug', 'price', 'image', 'date_added'
        ]
        read_only_fields = ['date_added']
