from django.shortcuts import render
from rest_framework import generics
from .models import Movie, Cinema, Screening
from .serializers import MovieSerializer, CinemaSerializer, ScreeningSerializer, RegisterSerializer
from rest_framework import permissions
from django.contrib.auth.models import User


# APIView zwracają obiekt klasy Response, który automatycznie zwróci dane w postaci JSON


# Widoki filmu
class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all().order_by('year')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Widoki kina
class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all().order_by('city', 'name')
    serializer_class = CinemaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Widoki seansu
class ScreeningListView(generics.ListCreateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Rejestracja użytkownika
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
