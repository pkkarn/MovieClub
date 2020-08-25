from django.urls import path
from movie import views

urlpatterns = [
    path('', views.home, name="home"),
]
