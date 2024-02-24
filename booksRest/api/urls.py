from django.urls import path
from .views import createliberian,ListBorrowed,DetailBorrowed,logout_user,registration_view,liberianDetail,listliberian
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('',createliberian.as_view(),name='liberian'),
    path('borrow/',ListBorrowed.as_view(),name='borrowedbook'),
    path('borrow/<int:pk>/',DetailBorrowed.as_view(),name='detailborrowed'),
    path('login/', obtain_auth_token,name='login'),
    path('logout/',logout_user,name='logout'),
    path('register/',registration_view,name='registration'),
    
    path('liberian/',listliberian.as_view(),name='liberains'),
    path('liberian/<int:pk>/',liberianDetail.as_view(),name='liberaindelete')
]
