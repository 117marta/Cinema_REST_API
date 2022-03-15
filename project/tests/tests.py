import pytest
from cinema_app.models import Movie, Person
from .utils import random_person, fake_movie_data
from django.contrib.auth.models import User


# GET method
@pytest.mark.django_db
def test_get_movie_list(client, set_up):
    response = client.get('/movies/', {}, format='json')
    assert response.status_code == 200  # OK
    # assert Movie.objects.count() == len(response.data)   # 4 (bo tak jest w ustawieniach paginacji)
    assert Movie.objects.count() == response.data['count']


# POST method
@pytest.mark.django_db
def test_post_movie(client, set_up):
    movies_before = Movie.objects.count()
    new_movie = fake_movie_data()
    response = client.post('/movies/', new_movie, format='json')
    assert response.status_code == 403  # forbidden

    user = User.objects.create(username='test')
    client.force_authenticate(user)
    response = client.post('/movies/', new_movie, format='json')
    assert response.status_code == 201  # created
    assert Movie.objects.count() == movies_before + 1

    for key, value in new_movie.items():  # lista tupli [(key, value),]
        assert key in response.data
        if isinstance(value, list):  # czy value jest listą
            assert len(response.data[key]) == len(value)  # porównuje zawartość bez uwzględnienia kolejności
        else:
            assert response.data[key] == value


# GET method - movie.id
@pytest.mark.django_db
def test_get_movie_detail(client, set_up):
    movie = Movie.objects.first()
    response = client.get(f'/movies/{movie.pk}/', {}, format='json')
    assert response.status_code == 200  # OK

    for field in ('title', 'year', 'description', 'director', 'actor'):
        assert field in response.data  # czy powyższe pola znajdują się w response.data


# DELETE method
@pytest.mark.django_db
def test_delete_movie(client, set_up):
    movie = Movie.objects.first()
    user = User.objects.create(username='test')
    client.force_authenticate(user)
    response = client.delete(f'/movies/{movie.pk}/', {}, format='json')
    assert response.status_code == 204  # no content

    movies_id = [movie.pk for movie in Movie.objects.all()]
    assert movie.pk not in movies_id  # czy movie się usunęło i nie ma go w zbiorze aktualnych filmów


# PUT method
@pytest.mark.django_db
def test_update_movie(client, set_up):
    movie = Movie.objects.first()
    response = client.get(f'/movies/{movie.pk}/', {}, format='json')
    assert response.status_code == 200

    movie_data = response.data
    new_year = 2022
    movie_data['year'] = new_year
    new_actors = [random_person().name]
    movie_data['actor'] = new_actors
    user = User.objects.create(username='test')
    client.force_authenticate(user)
    response = client.patch(f'/movies/{movie.pk}/', movie_data, format='json')
    assert response.status_code == 200

    movie_obj = Movie.objects.get(pk=movie.pk)
    assert movie_obj.year == new_year  # czy uaktualnił się rok

    db_actor_names = [a.name for a in movie_obj.actor.all()]
    assert len(db_actor_names) == len(new_actors)  # czy uaktualnili się aktorzy
