from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from store.models import Store
from tokenshield.models import User

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('Name'), max_length=255)
    )
    
    
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

class Brand(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('Name'), max_length=255)
    )
    slug = models.SlugField(unique=True)
    
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)
    def __str__(self):
        return self.name

class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(_("Name"), max_length=255),
        description=models.TextField(_("Description"), blank=True),
    )
    slug=models.SlugField(unique=False)
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, verbose_name=_('Brand'), on_delete=models.SET_NULL, null=True, blank=True)
    store = models.ForeignKey(Store, verbose_name=_('Store'), on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='products')
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    is_featured = models.BooleanField(default=False)

class Attribute(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(_('Name'), max_length=255)
    )

    def __str__(self):
        return self.name

class AttributeValue(TranslatableModel):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='values')
    translations = TranslatedFields(
        value = models.CharField(_('Value'), max_length=255)
    )

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attributes = models.ManyToManyField(AttributeValue, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.sku}"

class ProductStock(models.Model):
    variant = models.OneToOneField(ProductVariant, on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.variant.sku} - {self.quantity} in stock"
