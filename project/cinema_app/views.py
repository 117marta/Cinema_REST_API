from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Cinema
from .serializers import MovieSerializer, CinemaSerializer


# APIView zwracają obiekt klasy Response, który automatycznie zwróci dane w postaci JSON


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all().order_by('year')
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Widoki kina
class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all().order_by('city', 'name')
    serializer_class = CinemaSerializer


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
