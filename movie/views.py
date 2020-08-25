from django.shortcuts import render
from .models import Movie


def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)
