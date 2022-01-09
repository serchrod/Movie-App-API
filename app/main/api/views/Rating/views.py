from rest_framework import viewsets

from .serializer import RatingModelSerializer
from main.models import Rating


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingModelSerializer
