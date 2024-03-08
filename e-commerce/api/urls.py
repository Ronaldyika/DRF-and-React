from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProductListView, ProductDetailView, CartItemView, CommunicationView, AdminReplyView

urlpatterns = [
    path(),
    path(),
    path(),
    path(),
    path('communication/', CommunicationView.as_view(), name='communication-list-create'),
    path('communication/<int:pk>/', CommunicationView.as_view(), name='communication-detail'),
    path('admin-reply/<int:pk>/', AdminReplyView.as_view(), name='admin-reply'),

]
