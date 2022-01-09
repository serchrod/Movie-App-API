from rest_framework import viewsets
from rest_framework import filters
from .serializer import MovieModelSerializer
from main.models import Movie
from rest_framework.permissions import AllowAny


#from django_filters.rest_framework import DjangoFilterBackend

class MovieViewSet(viewsets.ModelViewSet):
    
    permission_classes_by_action = {'list': [AllowAny]}
    
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title','plot']
    ordering_fields = ['title', 'release_date']
    

    def list(self, request, *args, **kwargs):
         return super(MovieViewSet, self).list(request, *args, **kwargs)
        #return Response([],status=status.HTTP_200_OK)
    
    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]