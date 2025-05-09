from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    Category, Brand, Product, ProductImage,
    Attribute, AttributeValue, ProductVariant, ProductStock
)

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name', 'slug', 'parent')
    search_fields = ('translations__name',)

@admin.register(Brand)
class BrandAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('translations__name',)

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('name', 'category', 'brand', 'store', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'brand', 'store')
    search_fields = ('translations__name', 'store__translations__name')
    
    @admin.action(description='Duplicate selected products')
    def duplicate_product(self, request, queryset):
        for obj in queryset:
            obj_copy = obj
            obj_copy.pk = None
            obj_copy.name = f"{obj_copy.name} (Copy)"
            obj_copy.save()

@admin.register(Attribute)
class AttributeAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('translations__name',)

@admin.register(AttributeValue)
class AttributeValueAdmin(TranslatableAdmin):
    list_display = ('value', 'attribute')
    search_fields = ('translations__value', 'attribute__translations__name')

@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('product', 'sku', 'price')
    search_fields = ('sku',)
    filter_horizontal = ('attributes',)

@admin.register(ProductStock)
class ProductStockAdmin(admin.ModelAdmin):
    list_display = ('variant', 'quantity')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image', 'is_featured')
