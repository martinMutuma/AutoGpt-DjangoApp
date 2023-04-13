from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
