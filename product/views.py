from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers
from core.pagination import StandardResultSetPagination


class CategoryListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.Category.objects.all()
  serializer_class = serializers.ProductCategorySerializer
  pagination_class = StandardResultSetPagination
  

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Category.objects.all()
  serializer_class = serializers.ProductCategorySerializer
  
  
class BrandListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.Brand.objects.all()
  serializer_class = serializers.ProductBrandSerializer
  pagination_class = StandardResultSetPagination
  
  
class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Brand.objects.all()
  serializer_class = serializers.ProductBrandSerializer
  

class ProductImageListCreateAPIView(generics.ListCreateAPIView):
  queryset = models.ProductImage.objects.all()
  serializer_class = serializers.ProductImageSerializer
  

class ProductImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.ProductImage.objects.all()
  serializer_class = serializers.ProductImageSerializer
  



class ProductListCreateAPIView (generics.ListCreateAPIView):
  queryset = models.Product.objects.all()
  serializer_class = serializers.ProductSerializer
  pagination_class = StandardResultSetPagination
  def perform_create(self, serializer):
    # serializer.save(created_by = self.request.user)
    serializer.save(created_by = 1)
  
  
  
class ProductRetrieveUpdateDestroyAPIView (generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Product.objects.all()
  serializer_class = serializers.ProductSerializer
  permission_classes = [IsAuthenticated]
  authentication_classes = [IsAuthenticated]
  
  
