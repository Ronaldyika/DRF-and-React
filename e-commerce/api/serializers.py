from rest_framework import serializers
from .models import Customer,Product,ProductImage,CartItem,Communication
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
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
