from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import AccountFormTemplate, AccountFormField, AccountFormSubmission


@admin.register(AccountFormTemplate)
class AccountFormTemplateAdmin(TranslatableAdmin):
    list_display = ('name', 'created_by', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('translations__name',)
    ordering = ('-created_at',)


@admin.register(AccountFormField)
class AccountFormFieldAdmin(TranslatableAdmin):
    list_display = ('label', 'form', 'field_type', 'is_required', 'order')
    list_filter = ('field_type', 'is_required')
    search_fields = ('translations__label',)
    ordering = ('form', 'order')


@admin.register(AccountFormSubmission)
class AccountFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'form', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('user__username', 'form__translations__name')
    ordering = ('-submitted_at',)
