from django.db import models
from django.conf import settings

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    plot = models.TextField()
    
class Rating(models.Model):
    rating = models.IntegerField()
    comment = models.TextField(default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL,related_name='movie_data', blank=True, null=True)