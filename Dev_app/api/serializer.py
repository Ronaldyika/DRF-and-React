from .models import UpcomingEvent,Blog,UserDetailTesting,Email

from rest_framework import serializers
from django.contrib.auth.models import User

# admin registration and token generation

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'password1 and password2 should be the same'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email already exists'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account


class UpcomingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpcomingEvent
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:

        model = Blog
        fields = '__all__'

class UserDetialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailTesting
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    usedetail = UserDetialSerializer(many = True, read_only = True)

    class Meta:
        model = Email
        fields = '__all__'