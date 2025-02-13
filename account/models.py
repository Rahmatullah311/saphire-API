from django.db import models
from django.contrib.auth import get_user_model
from parler.models import TranslatableModel, TranslatedFields

User = get_user_model()


class AccountFormTemplate(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, unique=True),
        description=models.TextField(blank=True, null=True),
    )
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="created_forms"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)


class AccountFormField(TranslatableModel):
    FIELD_TYPES = [
        ("text", "Text"),
        ("email", "Email"),
        ("number", "Number"),
        ("date", "Date"),
        ("boolean", "Boolean"),
        ("select", "Select"),
        ("checkbox", "Checkbox"),
        ("radio", "Radio"),
    ]

    form = models.ForeignKey(
        AccountFormTemplate, on_delete=models.CASCADE, related_name="fields"
    )
    translations = TranslatedFields(label=models.CharField(max_length=255))
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    is_required = models.BooleanField(default=True)
    options = models.JSONField(
        blank=True, null=True
    )  # Store select, checkbox, radio options
    order = models.PositiveIntegerField(default=0)  # Allows ordering of form fields


    def __str__(self):
        return self.safe_translation_getter("label", any_language=True)


class AccountFormSubmission(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="form_submissions"
    )
    form = models.ForeignKey(
        AccountFormTemplate, on_delete=models.CASCADE, related_name="submissions"
    )
    data = models.JSONField()  # Store user-submitted data dynamically
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.user} for {self.form.safe_translation_getter('name', any_language=True)}"
