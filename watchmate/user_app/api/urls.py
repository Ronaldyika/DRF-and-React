from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from user_app.api.views import registration_view,logout_user

urlpatterns = [
    path('login/', obtain_auth_token,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',registration_view,name='registration')
]

