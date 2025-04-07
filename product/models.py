# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Category(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name="subcategories")
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     stock_quantity = models.PositiveIntegerField(default=0)
#     seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
#     slug = models.SlugField(unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


# class ProductVariant(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
#     attribute_name = models.CharField(max_length=100)  # e.g., "Size"
#     attribute_value = models.CharField(max_length=100)  # e.g., "M"

#     def __str__(self):
#         return f"{self.product.name} - {self.attribute_name}: {self.attribute_value}"


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
#     image = models.ImageField(upload_to="product_images/")
#     is_primary = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Image for {self.product.name}"


# class Stock(models.Model):
#     product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="stock")
#     quantity = models.PositiveIntegerField(default=0)
#     low_stock_threshold = models.PositiveIntegerField(default=5)  # Notify when stock is low

#     def is_low_stock(self):
#         return self.quantity <= self.low_stock_threshold

#     def __str__(self):
#         return f"Stock for {self.product.name}: {self.quantity}"


# class Review(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
#     rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 star rating
#     comment = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review by {self.user.username} for {self.product.name}"


# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
#     quantity = models.PositiveIntegerField()
#     price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
#     order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="items")

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name}"



# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
#     quantity = models.PositiveIntegerField()
#     price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
#     order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name="items")

#     def __str__(self):
#         return f"{self.quantity} x {self.product.name}"
