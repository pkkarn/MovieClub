from django.shortcuts import render
from .models import Movie
from .filters import MovieFilter


def home(request):
    movies = Movie.objects.all()
    myFilter = MovieFilter(request.GET,queryset=movies)
    movies = myFilter.qs
    context = {
        'movies': movies,
        'myFilter': myFilter
    }
    return render(request, 'index.html', context)
