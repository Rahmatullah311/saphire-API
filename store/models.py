from django.db import models
from django.contrib.auth import get_user_model
from tokenshield.models import User
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Store(TranslatableModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stores')
    translations = TranslatedFields(
      name = models.CharField(_('Name'), max_length=255, unique=True),
      description = models.TextField(_('Description'), blank=True, null=True),
      address = models.CharField(max_length=500, blank=True, null=True),
    )
    logo = models.ImageField(upload_to='store_logos/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


# class StoreStaff(models.Model):
#   class Role(models.TextChoices):
#       OWNER = 'owner', _('Owner')
#       CO_OWNER = 'co_owner', _('Co-Owner')
#       GENERAL_MANAGER = 'general_manager', _('General Manager')
#       SALES_MANAGER = 'sales_manager', _('Sales Manager')
#       PRODUCT_MANAGER = 'product_manager', _('Product Manager')
#       INVENTORY_MANAGER = 'inventory_manager', _('Inventory Manager')
#       ORDER_MANAGER = 'order_manager', _('Order Manager')
#       MARKETING_MANAGER = 'marketing_manager', _('Marketing Manager')
#       CUSTOMER_SUPPORT_MANAGER = 'customer_support_manager', _('Customer Support Manager')
#       FINANCE_MANAGER = 'finance_manager', _('Finance Manager')
#       CASHIER = 'cashier', _('Cashier')
#       SALESPERSON = 'salesperson', _('Salesperson')
#       SUPPORT_AGENT = 'support_agent', _('Support Agent')
#       CONTENT_CREATOR = 'content_creator', _('Content Creator')
#       DESIGNER = 'designer', _('Designer')
#       DEVELOPER = 'developer', _('Developer')
#       COURIER = 'courier', _('Courier')
#       AUDITOR = 'auditor', _('Auditor')
#       HR_MANAGER = 'hr_manager', _('HR Manager')
#       SECURITY_OFFICER = 'security_officer', _('Security Officer')

#   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_staff')
#   store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='staff')
#   role = models.CharField(max_length=30, choices=Role.choices, default=Role.SALESPERSON)
#   is_active = models.BooleanField(default=True)
#   created_at = models.DateTimeField(auto_now_add=True)

#   class Meta:
#       unique_together = ('user', 'store')

#   def __str__(self):
#       return f"{self.user.username} at {self.store.name} as {self.get_role_display()}"
