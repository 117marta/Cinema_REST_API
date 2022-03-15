from cinema_app.models import Person, Movie
import pytest
from rest_framework.test import APIClient
from .utils import faker, create_fake_movie


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
