from django.shortcuts import render
from rest_framework  import generics
from .serializers import ReviewSerializer,WatchlistSerializer,StreamplateformSerializer
from .models import Review,Watchlist,StreamPlateform

class ReviewCreate(generics.CreateAPIView):
    
    serializer_class = ReviewSerializer
    
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        movie = Watchlist.objects.get(pk=pk)
        
        serializer.save(watchlist = movie)

class WatchList(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class  = WatchlistSerializer
    
class WatchDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class  = WatchlistSerializer

class StreamplateformList(generics.ListCreateAPIView):
    queryset = StreamPlateform.objects.all()
    serializer_class  = StreamplateformSerializer
    
class StreamplateformDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlateform.objects.all()
    serializer_class  = StreamplateformSerializer


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def  get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)
    
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer