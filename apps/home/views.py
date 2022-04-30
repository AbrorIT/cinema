from django.shortcuts import render
from apps.home.models import Home
# Create your views here.

def index(request):
    home = Home.objects.latest('id')

    context = {
        'home': home,

    }
    return render(request, 'index.html', context)