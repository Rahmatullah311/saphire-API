from django.contrib import admin
from parler.admin import TranslatableAdmin
from . import models

# Register your models here.

@admin.register(models.Store)
class StoreAdmin(TranslatableAdmin):
  list_display = ('name', 'phone', 'email', 'created_at', 'updated_at')
  list_filter = ('is_active',)
  search_fields = ('translations__name', 'phone', 'email', 'website')