from django.shortcuts import render
from .serializer import UpcomingEventSerializer,BlogSerializer,UserDetialSerializer,EmailSerializer,RegistrationSerializer
from .models import UpcomingEvent,Blog,UserDetailTesting,Email
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# User section views
class upcomingEventList(generics.ListAPIView):
    queryset = UpcomingEvent.objects.all()
    serializer_class = UpcomingEventSerializer


class blogList(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



# admin section views

@api_view(['POST'])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            # token, created = Token.objects.get_or_create(user=account)
            # data['token'] = token.key

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# logout user
        
@api_view(['POST',])
def logout_user(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

# --------------------------------admin work blog---------------------------------
class AdminupcomingEventList(generics.ListCreateAPIView):
    queryset = UpcomingEvent.objects.all()
    serializer_class  = UpcomingEventSerializer
    permission_classes =[IsAuthenticated]
    
class AdminupcomingEventDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = UpcomingEvent.objects.all()
    serializer_class  = UpcomingEventSerializer

    permission_classes =[IsAuthenticated]

class AdminblogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer
    permission_classes =[IsAuthenticated]

    
class AdminblogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class  = BlogSerializer
    permission_classes =[IsAuthenticated]



class UserList(generics.ListCreateAPIView):
    queryset = UserDetailTesting.objects.all()
    serializer_class = UserDetialSerializer
    
    def  get_queryset(self,email):
        email = self.kwargs['pk']
        return UserDetailTesting.objects.get(userdetails = email)
    
    
class EmailList(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
