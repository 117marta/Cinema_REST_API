from cinema_app.models import Person, Movie
import pytest
from rest_framework.test import APIClient
from .utils import faker, create_fake_movie, create_fake_cinema
from django.contrib.auth.models import User


# Fikstura zwracająca klienta API
@pytest.fixture
def client():
    client = APIClient()
    return client


# Fikstura tworząca kilka obiektów w BD
@pytest.fixture
def set_up():
    for _ in range(15):
        Person.objects.create(name=faker.name())
    for _ in range(10):
        create_fake_movie()
    for _ in range(5):
        create_fake_cinema()


# Fikstura tworząca użytkownika
@pytest.fixture()
def register_user():
    u = {
        'username': faker.email().split('@')[0],
        'email': faker.email(),
        'password': '!@#PASSword123',
        'password2': '!@#PASSword123',
        'first_name': faker.first_name(),
        'last_name': faker.last_name(),
    }
    return u


# Fikstura tworząca użytkownika
@pytest.fixture()
def login_user():
    user = User.objects.create_user(
        username='jan_kowalski',
        password='pass1',
        email='jan@email.com',
        first_name='Jan',
        last_name='Kowalski',
    )
    return user
