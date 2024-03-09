from rest_framework import serializers
from .models import Product,ProductImage,CartItem,Communication
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def validate_username(self, value):
        """
        Ensure that the username is unique.
        """
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")
        return value

    def validate_email(self, value):
        """
        Ensure that the email is unique.
        """
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("This email address is already in use.")
        return value

    def validate_password1(self, value):
        """
        Validate the first password.
        """
        validate_password(value)
        return value

    def validate_password2(self, value):
        """
        Validate the second password.
        """
        validate_password(value)
        return value

    def create(self, validated_data):
        """
        Create a new user using the provided validated data.
        """
        password1 = validated_data.pop('password1')
        validated_data.pop('password2')  # Remove password2 from validated data

        user = get_user_model().objects.create_user(**validated_data, password=password1)
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'
