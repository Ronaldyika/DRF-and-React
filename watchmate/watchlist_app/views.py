from django.shortcuts import render
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.exceptions import ValidationError
from rest_framework  import generics
from .serializers import ReviewSerializer,WatchlistSerializer,StreamplateformSerializer
from .models import Review,Watchlist,StreamPlateform
# from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsReviewUserOrReadOnly,IsAdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema


class ReviewCreate(generics.CreateAPIView):
    
    # @swagger_auto_schema(operation_summary = "create review")

    serializer_class = ReviewSerializer
    permission_classes =[IsAuthenticated]
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist = watchlist, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("you have reviewed already")
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating +serializer.validated_data['rating'])/2
            watchlist.number_rating  = watchlist.number_rating + 1
            watchlist.save()
        
        serializer.save(watchlist = watchlist,review_user=review_user)

class WatchList(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class  = WatchlistSerializer
    permission_classes =[IsAdminOrReadOnly]
    
class WatchDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class  = WatchlistSerializer

    permission_classes =[IsAdminOrReadOnly]

class StreamplateformList(generics.ListCreateAPIView):
    serializer_class = [IsAdminOrReadOnly]

    queryset = StreamPlateform.objects.all()
    serializer_class  = StreamplateformSerializer

    
class StreamplateformDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = [IsAdminOrReadOnly]
    queryset = StreamPlateform.objects.all()
    serializer_class  = StreamplateformSerializer



class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def  get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)
    
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes =[IsReviewUserOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]