from rest_framework import serializers
from .models import MoMoUser,PaymentTransaction

class MoMoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoMoUser
        fields = "__all__"


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = "__all__"
