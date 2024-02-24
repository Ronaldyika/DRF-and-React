from django.shortcuts import render
from .models import Liberian,Borrowed_Book
from rest_framework.response import Response
from .serializer import LiberianSerializer,BorrowedBookSerializer,RegistrationSerializer
from rest_framework import status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import generics
from rest_framework.decorators import api_view

# this field is for liberian registration
class createliberian(generics.CreateAPIView):
    queryset = Liberian.objects.all()
    serializer_class = LiberianSerializer
    permission_classes = [IsAdminUser]

#this field will be seen and controlled only by a super user
    
class liberianDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Liberian.objects.all()
    serializer_class = LiberianSerializer
    permission_classes = [IsAdminUser]

class listliberian(generics.ListCreateAPIView):
    queryset = Liberian.objects.all()
    serializer_class = LiberianSerializer
    permission_classes = [IsAdminUser]


# this field is for the borrowed books
    
class ListBorrowed(generics.ListCreateAPIView):
    queryset = Borrowed_Book.objects.all()
    serializer_class = BorrowedBookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DetailBorrowed(generics.RetrieveDestroyAPIView):
    queryset = Borrowed_Book.objects.all()
    serializer_class = BorrowedBookSerializer
    permission_classes = [IsAdminUser]

@api_view(['POST',])
def logout_user(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            liberian = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = liberian.username
            data['email'] = liberian.email
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
