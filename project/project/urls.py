"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cinema_app.views import (MovieListView,
                              MovieView,
                              CinemaListView,
                              CinemaView,
                              ScreeningListView,
                              ScreeningView,
                              RegisterView,
                              UserListView,
                              UserView)
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/', MovieView.as_view(), name='movies-detail'),
    path('cinemas/', CinemaListView.as_view()),
    path('cinemas/<int:pk>/', CinemaView.as_view()),
    path('screenings/', ScreeningListView.as_view()),
    path('screenings/<int:pk>/', ScreeningView.as_view()),
    path('api-auth/', include('rest_framework.urls')),  # logowanie
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
]
