from django.urls import path
from apps.home.views import index, about


urlpatterns = [
    path('', index, name = 'index'),
    path('userprofile_light/', about, name = 'about'),
]