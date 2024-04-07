# Import required modules
from django.http import JsonResponse
import uuid
import base64
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
import requests
from .configs import momo_subscriptionKey,momo_host,momo_token_url,momo_request_to_pay_url,callback_host

import json

# Define constants
MOMO_SUBSCRIPTION_KEY = momo_subscriptionKey
momo_host = momo_host
momo_token_url = momo_token_url
momo_request_to_pay_url = momo_request_to_pay_url
callback_host = callback_host 


# Endpoint for creating MoMo API User
@csrf_exempt
def create_api_user(request):
    if request.method == 'POST':
        api_url = f'https://{momo_host}/v1_0/apiuser'
        uuid_v4 = str(uuid.uuid4())  # Generate UUID v4 for X-Reference-Id
        headers = {
            'X-Reference-Id': uuid_v4,
            'Ocp-Apim-Subscription-Key': MOMO_SUBSCRIPTION_KEY,
            'Content-Type': 'application/json'
        }
        data = {
            'providerCallbackHost': 'your_callback_host'  # Replace 'your_callback_host' with your actual callback host
        }
        try:
            response = requests.post(api_url, headers=headers, json=data)
            if response.status_code == 201:  # Check if user creation was successful
                return JsonResponse({'response': response.json(), 'userId': uuid_v4}, status=response.status_code)
            else:
                return JsonResponse({'message': 'Error creating API user', 'error': response.text}, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'message': 'Error creating API user', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
# Endpoint for retrieving created user by User ID
@csrf_exempt
def get_created_user(request, user_id):
    if request.method == 'GET':
        api_url = f'https://{momo_host}/v1_0/apiuser/{user_id}'
        headers = {
            'Ocp-Apim-Subscription-Key': momo_subscriptionKey
        }
        try:
            response = requests.get(api_url, headers=headers)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({'message': 'Error retrieving created user', 'error': str(e)}, status=500)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////
# Endpoint for retrieving API key for a specific user
@csrf_exempt
def retrieve_api_key(request, user_id):
    if request.method == 'GET':  # Use 'GET' for retrieving data
        api_url = f'https://{momo_host}/v1_0/apiuser/{user_id}/apikey'
        headers = {
            'Ocp-Apim-Subscription-Key': momo_subscriptionKey
        }
        try:
            response = requests.get(api_url, headers=headers)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({'message': 'Error retrieving API key', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
# Endpoint for generating MoMo API token
@csrf_exempt
def generate_api_token(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userId')
        password = data.get('apiKey')
        basic_auth = 'Basic ' + base64.b64encode((username + ':' + password).encode()).decode()
        headers = {
            'Authorization': basic_auth,
            'Ocp-Apim-Subscription-Key': momo_subscriptionKey
        }
        try:
            response = requests.post(momo_token_url, headers=headers)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({'message': 'Error generating API token', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
# Endpoint for initiating a payment request
@csrf_exempt
def request_to_pay(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total')
        phone = data.get('phone')
        momo_token_id = data.get('momoTokenId')

        if not momo_token_id:
            return JsonResponse({'error': 'MoMo token not available'}, status=400)

        external_id = get_random_string(length=12)
        body = {
            'amount': total,
            'currency': 'EUR',
            'externalId': external_id,
            'payer': {
                'partyIdType': 'MSISDN',
                'partyId': phone
            },
            'payerMessage': 'Payment for order',
            'payeeNote': 'Payment for order'
        }
        headers = {
            'X-Target-Environment': 'sandbox',
            'Ocp-Apim-Subscription-Key': momo_subscriptionKey,
            'Authorization': f'Bearer {momo_token_id}',
            'Content-Type': 'application/json'
        }
        try:
            response = requests.post(momo_request_to_pay_url, json=body, headers=headers)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({'message': 'Error processing payment request', 'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# Endpoint for getting payment status
@csrf_exempt
def payment_status(request, transaction_id, momo_token_id):
    if request.method == 'GET':
        api_url = f'https://{momo_host}/collection/v1_0/requesttopay/{transaction_id}'
        headers = {
            'Ocp-Apim-Subscription-Key': momo_subscriptionKey,
            'Authorization': f'Bearer {momo_token_id}',
            'X-Target-Environment': 'sandbox'
        }
        try:
            response = requests.get(api_url, headers=headers)
            return JsonResponse(response.json(), status=response.status_code)
        except Exception as e:
            return JsonResponse({'message': 'Error retrieving payment status', 'error': str(e)}, status=500)
