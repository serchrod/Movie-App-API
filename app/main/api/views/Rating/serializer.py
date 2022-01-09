from rest_framework import fields, serializers

from main.models import Rating , Movie
from django.conf import settings
from users.models import NewUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ["email"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id","title")

class RatingModelSerializer(serializers.ModelSerializer):
    
    movie = MovieSerializer(many=False)
    user = UserSerializer(many=False)
    
    class Meta:
        model = Rating
        fields = ('movie','rating','comment','user')