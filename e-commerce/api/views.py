from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics,permissions
from .serializers import CommunicationSerializer,CustomUserSerializer,ProductSerializer,CartItemSerializer,ProductImageSerializer
from .models import Product,ProductImage,CartItem,Communication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User


# --------------------------start of communication view ----------------------------------------
class CommunicationView(generics.ListCreateAPIView):
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow users to see their own messages
        return Communication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Assuming 'product_id' is sent in the request data
        product_id = self.request.data.get('product_id')

        # Attempt to get the Product instance based on the provided product_id
        product = get_object_or_404(Product, pk=product_id)

        # Set the user, product, and other relevant data
        serializer.save(user=self.request.user, product=product)

class AdminReplyView(generics.UpdateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        # Ensure the user making the request is an admin
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

class DeleteCommunicationView(generics.DestroyAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_object(self):
        # Ensure the user making the request is an admin
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj
class AdminProductImageView(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAdminUser]

class AdminProductImageViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAdminUser]

# --------------------------start of userRegistratoin and login--------------------------- 
class UserRegistrationView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Generate a token for the user
        user = get_user_model().objects.get(username=serializer.validated_data['username'])
        Token.objects.create(user=user)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class UserLoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            # Authenticate the user using the provided username and password
            user = authenticate(username=username, password=password)

            if user:
                # If the user is authenticated, generate a token
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_id': user.id, 'username': user.username})

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


#--------------------------------products -----------------------------------------
    
class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class CartItemView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]