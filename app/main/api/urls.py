from django.urls import include, path
from rest_framework import routers
from .views.Movie.views import MovieViewSet
from .views.Rating.views import RatingViewSet


router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet )
router.register(r'rating', RatingViewSet )


urlpatterns = [
    path('', include(router.urls)),
]