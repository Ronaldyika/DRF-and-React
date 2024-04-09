from django.urls import path
from .views import (CreateAPIUserView,GetCreatedUserView,RetrieveAPIKeyView,GenerateAPITokenView,RequestToPayView,PaymentStatusView,)

urlpatterns = [
    path('create-api-user/', CreateAPIUserView.as_view(), name='create_api_user'),
    path('get-created-user/<str:userId>/', GetCreatedUserView.as_view(), name='get_created_user'),
    path('retrieve-api-key/<str:userId>/', RetrieveAPIKeyView.as_view(), name='retrieve_api_key'),
    path('generate-api-token/', GenerateAPITokenView.as_view(), name='generate_api_token'),
    path('request-to-pay/', RequestToPayView.as_view(), name='request_to_pay'),
    path('payment-status/<str:transaction_id>/', PaymentStatusView.as_view(), name='payment_status'),
]
