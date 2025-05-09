from rest_framework import serializers
from . import models
from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer


class ProductCategorySerializer (TranslatableModelSerializer):
  translations = TranslatedFieldsField(shared_model = models.Category)
  class Meta:
    model = models.Category
    fields = ['translations', 'slug', 'parent']
    
class ProductBrandSerializer (TranslatableModelSerializer):
  translations = TranslatedFieldsField(shared_model = models.Brand)
  class Meta:
    model = models.Brand
    fields = ['translations', 'slug', 'logo']
    

class ProductImageSerializer (serializers.ModelSerializer):
  class Meta:
    model = models.ProductImage
    fields = '__all__'


class ProductAttributeSerializer (TranslatableModelSerializer):
  translations = TranslatedFieldsField(shared_model = models.Attribute)
  class Meta:
    model = models.Attribute
    fields = ['translations']


class ProductAttributeValueSerializer (TranslatableModelSerializer):
  translations = TranslatedFieldsField(shared_model = models.AttributeValue)
  class Meta:
    model = models.AttributeValue
    fields = ['attribute', 'translations']

class ProductVariantSerializer (serializers.ModelSerializer):
  class Meta:
    model = models.ProductVariant
    fields = '__all__'


class ProductStockSerializer (serializers.ModelSerializer):
  class Meta:
    modele = models.ProductStock
    fields = '__all__'


class ProductSerializer(TranslatableModelSerializer):  
  translations = TranslatedFieldsField(shared_model = models.Product)
  variants = ProductVariantSerializer(many = True, read_only = True)
  images = ProductImageSerializer(many = True)
  class Meta:
    model = models.Product
    fields = ['id', 'translations', 'slug', 'category', 'brand', 'variants', 'images', 'store', 'is_active', 'created_at', 'created_by']
    read_only_fields = ['created_by']