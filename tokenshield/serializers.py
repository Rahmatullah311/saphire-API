from .models import User
from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
      raise serializers.ValidationError({'detail': 'Email and password are required'})

    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      raise serializers.ValidationError({'email': 'Email not found'})

    if not user.check_password(password):
      raise serializers.ValidationError({'password': 'Incorrect password'})

    return {'user': user}

class UserRegisterSerializer(serializers.ModelSerializer):
  repeat_password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = ['fullname', 'email', 'password', 'repeat_password']
    extra_kwargs = {
      'password': {'write_only': True}
    }

  def validate(self, data):
    email = data.get('email')
    password = data.get('password')
    repeat_password = data.get('repeat_password')

    if User.objects.filter(email=email).exists():
      raise serializers.ValidationError({'email': 'Email already exists'})

    if password != repeat_password:
      raise serializers.ValidationError({'password': 'Both passwords must be the same'})
    
    return data

  def create(self, validated_data):
    validated_data.pop('repeat_password')
    return User.objects.create_user(**validated_data)
