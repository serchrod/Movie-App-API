from rest_framework import serializers

from main.models import Rating


class RatingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'