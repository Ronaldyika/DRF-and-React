from rest_framework import serializers

from .models import Watchlist,Review,StreamPlateform

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Review
        fields = "__all__"

class WatchlistSerializer(serializers.ModelSerializer):
 
	reviews = ReviewSerializer(many=True,read_only = True)
	class Meta:
		model = Watchlist
		fields = "__all__"



class StreamplateformSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many = True, read_only = True)
    watchlist = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = StreamPlateform
        fields = '__all__'
