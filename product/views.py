from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
