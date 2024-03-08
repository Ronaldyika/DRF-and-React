from django.urls import path
from .views import UserRegistrationView,AdminProductImageView,AdminProductImageViewDetail, UserLoginView, ProductListView, ProductDetailView, CartItemView, CommunicationView, AdminReplyView,DeleteCommunicationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartItemView.as_view(), name='cart-item'),

    # ------------------handling the user and admin communication------------------------------
    path('communication/', CommunicationView.as_view(), name='communication-list-create'),
    path('communication/<int:pk>/', CommunicationView.as_view(), name='communication-detail'),
    path('adminreply/<int:pk>/', AdminReplyView.as_view(), name='admin-reply'),
    path('adminreply/<int:pk>/delete/', DeleteCommunicationView.as_view(), name='delete-communication'),
    path('adminproductimages/', AdminProductImageView.as_view(), name='adminproductimage'),
    path('adminproductimages/<int:pk>/delete/', AdminProductImageViewDetail.as_view(), name='adminproductimagedelete'),
]
