from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from .models import Category, Brand, Category       

# Create your views here.

class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self,request):
        serializer = CategorySerializer(self.queryset)
        return Response(serializer.data)
