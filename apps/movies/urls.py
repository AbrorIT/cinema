from django.urls import path 
from apps.home.views import index,about
from apps.movies.views import movie_detail

urlpatterns = [
    path('', index, name = 'index'),
    path('userprofile_light/', about, name = 'about'), 
]

