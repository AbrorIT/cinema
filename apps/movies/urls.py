from django.urls import path 
from apps.home.views import index,about
from apps.movies.views import movie_detail
from .models import Movie

urlpatterns = [
    path('', Movie, name = 'index'),
    path('movie-detail/<int:id>', movie_detail , name = 'movie_detail'), 
]

