from rest_framework import serializers

from main.models import Movie , Rating

class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['comment','user','rating','id']

class MovieModelSerializer(serializers.ModelSerializer):
    
    rating= RatingModelSerializer(many=True,source='movie_data')
    
    class Meta:
        model = Movie
        fields = ['title','release_date','plot','rating']