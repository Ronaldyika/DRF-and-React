from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import CommunicationSerializer
from .models import Customer,Product,ProductImage,CartItem,Communication


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