from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer


# APIView zwracają obiekt klasy Response, który automatycznie zwróci dane w postaci JSON


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
