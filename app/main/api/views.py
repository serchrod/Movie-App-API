from rest_framework import viewsets

from .serializer import MovieModelSerializer
from main.models import Movie


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer