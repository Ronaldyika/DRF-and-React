from django.urls import path
from .views import ReviewList,ReviewDetails,WatchList,WatchDetails,ReviewCreate,StreamplateformList,StreamplateformDetails
urlpatterns = [
     path('list',WatchList.as_view(),name='movie-list'),
     path('list/<int:pk>/',WatchList.as_view(),name='movie_detail'),
     
     path('stream',StreamplateformList.as_view(),name='stream_list'),
     path('stream/<int:pk>/',StreamplateformDetails.as_view(),name='stream_detail'),
     
    #  path('review',ReviewList.as_view(),name='review_list'),
    #  path('review/<int:pk>/',ReviewDetails.as_view(),name='review_details'),  
        
     path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review_create'),
     path('stream/<int:pk>/review',ReviewList.as_view(),name='review_list'),
     path('stream/review/<int:pk>/',ReviewDetails.as_view(),name='review_details'),
     
     
]
