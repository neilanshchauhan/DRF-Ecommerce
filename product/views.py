from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from .models import Category, Brand, Product     
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
