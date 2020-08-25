import django_filters
from .models import *
from django_filters import CharFilter

class MovieFilter(django_filters.FilterSet):  # Search Form
    movieName = CharFilter(field_name='movieName', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['movieName']
