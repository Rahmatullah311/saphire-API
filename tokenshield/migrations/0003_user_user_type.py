# Generated by Django 5.1.4 on 2025-01-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokenshield', '0002_alter_user_options_alter_user_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('buyer', 'Buyer'), ('seller', 'Seller'), ('admin', 'Admin'), ('moderator', 'Moderator'), ('delivery_agent', 'Delivery Agent'), ('guest_user', 'Guest User'), ('advertiser', 'Advertiser'), ('support_staff', 'Support Staff'), ('affiliate', 'Affiliate/Partner'), ('third_party_service', 'Third-party Service Provider'), ('owner', 'Marketplace Owner'), ('developer', 'Developer')], default='buyer', max_length=255),
        ),
    ]
