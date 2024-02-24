from .models import Liberian,Borrowed_Book
from django.contrib.auth.models import User
from rest_framework import serializers

class LiberianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Liberian
        fields = '__all__'


class BorrowedBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrowed_Book
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        # fields = ['username', 'email', 'password', 'password2']
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        password = self.validated_data['password']
        # password2 = self.validated_data['password2']

        # if password != password2:
        #     raise serializers.ValidationError({'error': 'password1 and password2 should be the same'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email already exists'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account