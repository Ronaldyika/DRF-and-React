from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from base64 import b64encode
# from rest_framework.views import APIView
from .models import MoMoUser, PaymentTransaction
import base64
from .serializer import MoMoUserSerializer, PaymentProcessedSerializer,PaymentTransactionSerializer,CreateAPIUserSerializer,RetrieveAPIKeySerializer
import requests
import uuid
from .configs import momo_Host,momo_subscriptionKey,callback_Host

class CreateAPIUserView(generics.CreateAPIView):
    serializer_class = CreateAPIUserSerializer

    def perform_create(self, serializer):
        momo_host = momo_Host # Replace 'your_momo_host' with your actual MoMo host
        momo_subscription_key = momo_subscriptionKey  # Replace 'your_subscription_key' with your actual subscription key
        callback_host = callback_Host  # Replace 'your_callback_host' with your actual callback host
        api_url = f'https://{momo_host}/v1_0/apiuser'
        uuid_v4 = str(uuid.uuid4())
        headers = {
            'X-Reference-Id': uuid_v4,
            'Ocp-Apim-Subscription-Key': momo_subscription_key,
            'Content-Type': 'application/json'
        }
        data = {
            'providerCallbackHost': callback_host
        }
        try:
            response = requests.post(api_url, headers=headers, json=data)
            if response.status_code == status.HTTP_201_CREATED:
                serializer.save(userId=uuid_v4)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Error creating API user'}, status=response.status_code)
        except requests.RequestException as e:
            return Response({'error': f'Error creating API user: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetCreatedUserView(generics.RetrieveAPIView):
    queryset = MoMoUser.objects.all()
    serializer_class = MoMoUserSerializer
    lookup_field = 'userId'

class RetrieveAPIKeyView(generics.RetrieveAPIView):
    serializer_class = RetrieveAPIKeySerializer
    lookup_field = 'userId'

    def get_queryset(self):
        userId = self.kwargs['userId']
        return MoMoUser.objects.filter(userId=userId)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        self.add_api_key(instance)  # Call the method to add API key
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def add_api_key(self, instance):
        momo_host = momo_Host  # Replace 'your_momo_host' with your actual MoMo host
        momo_subscription_key = momo_subscriptionKey  # Replace 'your_subscription_key' with your actual subscription key
        api_url = f'https://{momo_host}/v1_0/apiuser/{instance.userId}/apikey'
        headers = {
            'Ocp-Apim-Subscription-Key': momo_subscription_key
        }
        try:
            response = requests.post(api_url, headers=headers, json={})
            if response.status_code == status.HTTP_201_CREATED:
                instance.apiKey = response.json().get('apiKey')
                instance.save()
            else:
                raise Exception('Error retrieving API key')
        except requests.RequestException as e:
            raise Exception(f'Error retrieving API key fetch: {str(e)}')
        
class GenerateAPITokenView(generics.CreateAPIView):
    serializer_class = PaymentTransactionSerializer

    def perform_create(self, serializer):
        momo_token_url = 'https://sandbox.momodeveloper.mtn.com/collection/token/'
        momo_subscription_key =momo_subscriptionKey
        data = self.request.data
        username = data.get('userId')
        password = data.get('apiKey')
        basic_auth = 'Basic ' + b64encode(f'{username}:{password}'.encode()).decode()
        headers = {
            'Authorization': basic_auth,
            'Ocp-Apim-Subscription-Key': momo_subscription_key
        }
        try:
            response = requests.post(momo_token_url, headers=headers)  # Changed to GET method
            if response.status_code == 200:
                token = response.json().get('access_token')
                token_data = {'token': token}
                serializer.save(**token_data)  # Save token to database
                return Response({'token': token}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Error generating API token'}, status=response.status_code)
        except requests.RequestException as e:
            return Response({'error': f'Error generating API token: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class RequestToPayView(generics.CreateAPIView):
    serializer_class = PaymentProcessedSerializer

    def perform_create(self, serializer):
        momo_request_to_pay_url = 'https://sandbox.momodeveloper.mtn.com/collection/v1_0/requesttopay'
        momo_subscription_key = momo_subscriptionKey  # Replace with your actual subscription key

        payment_transaction = get_object_or_404(PaymentTransaction, id=self.request.data.get(id))
        momo_token_id = payment_transaction.token  # Access the token from the PaymentTransaction object
        if not momo_token_id:
            raise Exception('MoMo token not available')
        
        external_id = str(uuid.uuid4())
        body = {
            'amount': self.request.data.get('total'),
            'currency': 'EUR',
            'externalId': external_id,
            'payer': {
                'partyIdType': 'MSISDN',
                'partyId': self.request.data.get('phone')
            },
            'payerMessage': 'Payment for order',
            'payeeNote': 'Payment for order'
        }
        headers = {
            'X-Target-Environment': 'sandbox',
            'Ocp-Apim-Subscription-Key': momo_subscription_key,
            'Authorization': f'Bearer {momo_token_id}',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(momo_request_to_pay_url, json=body, headers=headers)
            if response.status_code == 200:
                serializer.save(payment_response=response.json(), success=True, payment_ref_id=external_id)
                return Response({'message': 'Payment request processed successfully'}, status=status.HTTP_201_CREATED)
            else:
                raise Exception('Error processing payment request')
        except Exception as e:
            raise Exception(f'Error processing payment request: {e}')

class PaymentStatusView(generics.RetrieveAPIView):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
    lookup_field = 'transaction_id'

    def get_queryset(self):
        transaction_id = self.kwargs['transaction_id']
        return PaymentTransaction.objects.filter(transaction_id=transaction_id)
