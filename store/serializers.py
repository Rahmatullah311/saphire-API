from rest_framework import serializers
from .models import Store
from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer



class StoreSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Store)

    class Meta:
        model = Store
        fields = [
            'owner',
            'translations',
            'logo',
            'phone',
            'email',
            'website',
            'is_active',
            'created_at',
            'updated_at',
        ]

