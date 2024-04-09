from rest_framework import serializers
from .models import MoMoUser, PaymentTransaction,Payments


class MoMoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoMoUser
        fields = ['userId', 'apiKey']

class CreateAPIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoMoUser
        fields = ['userId']
        read_only_fields = ['userId']  # Make the user_id field read-only


class RetrieveAPIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = MoMoUser
        fields = ['userId', 'apiKey']

        
class PaymentTransactionSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255,read_only=True)

    class Meta:
        model = PaymentTransaction
        fields = ['userId', 'apiKey', 'token']


    def create(self, validated_data):
        token = validated_data.pop('token', None)  
        instance = super().create(validated_data)
        if token:
            instance.token = token  
            instance.save()
        return instance
    



class PaymentProcessedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['amount', 'phone']  # Only include these fields

    def create(self, validated_data):
        return Payments.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.phone = validated_data.get('phone', instance.payer)
        instance.save()
        return instance