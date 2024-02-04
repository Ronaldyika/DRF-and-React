from rest_framework import serializers

from .model import Movie

class MovieSerializer(serializers.ModelSerializer):
	len_name = serializers.SerializerMethodField()
	class Meta:
		model = Movie
		fields = "__all__"


		def get_len_name(self,object):
			length = len(object.name)

			return length