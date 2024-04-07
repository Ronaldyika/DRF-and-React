from django.urls import path
from . import views

urlpatterns = [
    path('create-api-user/', views.create_api_user, name='create_api_user'),
    path('get-created-user/<str:user_id>/', views.get_created_user, name='get_created_user'),
    path('retrieve-api-key/<str:user_id>/', views.retrieve_api_key, name='retrieve_api_key'),
    path('generate-api-token/', views.generate_api_token, name='generate_api_token'),
    path('request-to-pay/', views.request_to_pay, name='request_to_pay'),
    path('payment-status/<str:transaction_id>/<str:momo_token_id>/', views.payment_status, name='payment_status'),
]
