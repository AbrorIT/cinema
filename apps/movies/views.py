from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from apps.movies.models import Movie, MovieComment
from apps.home.models import Setting
from apps.categories.models import Category
from django.db.models import Q
from apps.movies.forms import MovieCreateForm, MovieUpdateForm

# Create your views here.
def movie_detail(request, id):
    movie = Movie.objects.get(id = id)
    random_movies = Movie.objects.all().order_by('?')[:20]
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        message = request.POST.get('comment_message')
        comment = MovieComment.objects.create(message=message, movie=movie, user=request.user)
        return redirect('movie_detail', movie.id)

    context = {
        'movie' : movie,
        'random_movies' : random_movies,
        'home' : home,
        'categories' : categories,
        'comment' : comment,
    }
    return render(request, 'movielist.html', context)

def movie_search(request):
    movies = Movie.objects.all()
    qury_obj = request.GET.get('key')
    home = Setting.objects.latest('id')
    if qury_obj:
        products = Movie.objects.filter(Q(title__icontains = qury_obj))
    context = {
        'home' : home, 
        'movies' : movies,
        'products' : products,
    }
    return render(request, 'movielist.html', context)

def movie_create(request):
    form = MovieCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,

    }
    return render(request, 'movielist.html', context)

def movie_update(request, id):
    movie = Movie.objects.get(id = id)
    form = MovieUpdateForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movie_detail', movie.id)
    context = {
        'form' : form,
    }
    return render(request, 'movielist.html', context)


def movie_delete(request, id):
    context ={}
 
    obj = get_object_or_404(Movie, id = id)
    if request.method =="POST":

        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "movielist.html", context)