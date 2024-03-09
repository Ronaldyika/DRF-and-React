from django.shortcuts import render
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


# --------------------------start of communication view ----------------------------------------

class CommunicationView(generics.ListCreateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer

    def perform_create(self, serializer):
        # Automatically set the user based on the authenticated user
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Limit queryset to messages related to the authenticated user
        return Communication.objects.filter(user=self.request.user)
    
class AdminReplyView(generics.UpdateAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAdminUser]

class DeleteCommunicationView(generics.DestroyAPIView):
    queryset = Communication.objects.all()
    serializer_class = CommunicationSerializer
    permission_classes = [permissions.IsAdminUser]


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
    authentication_classes = [TokenAuthentication]

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