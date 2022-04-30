from django.contrib import admin
from apps.movies.models import Film, Genre, Actor, Rating, MovieShots, RatingStar, Reviews

# from apps.category.models import Category

admin.site.register(Film)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Reviews)