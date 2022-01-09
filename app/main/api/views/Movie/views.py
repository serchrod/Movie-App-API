from rest_framework import viewsets
from rest_framework import filters

from .serializer import MovieModelSerializer
from main.models import Movie
#from django_filters.rest_framework import DjangoFilterBackend

#class MovieViewSet(viewsets.ModelViewSet):
#    queryset = Movie.objects.all()
#    serializer_class = MovieModelSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title','plot']
    ordering_fields = ['title', 'release_date']