from django.urls import path
from .views import upcomingEventList,blogList,registration_view,logout_user,AdminupcomingEventList,AdminupcomingEventDetails,AdminblogList,AdminblogDetails,UserList,EmailList
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # users paths
    path('gallery/',upcomingEventList.as_view(),name='gallery'),
    path('blog/',blogList.as_view(),name='blog'),



    # admin section
    path('login/', obtain_auth_token,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',registration_view,name='registration'),


    # admin detailsitelinks
    path('admingallery/',AdminupcomingEventList.as_view(),name="upcomingtask"),
    path('admingallery/<int:pk>/',AdminupcomingEventDetails.as_view(),name="details"),
    path('adminblog/',AdminblogList.as_view(),name="blog"),
    path('adminblog/<int:pk>/',AdminblogDetails.as_view(),name="blog-details"),
    path('userlist/',UserList.as_view(),name="userlist"),
    path('emailist/',EmailList.as_view(),name="email"),
]
