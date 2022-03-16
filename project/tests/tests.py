import pytest
from cinema_app.models import Movie, Person, Cinema
from .utils import random_person, fake_movie_data, fake_cinema_data
from django.contrib.auth.models import User


# GET method - lista filmów
@pytest.mark.django_db
def test_get_movie_list(client, set_up):
    response = client.get('/movies/', {}, format='json')
    assert response.status_code == 200  # OK
    # assert Movie.objects.count() == len(response.data)   # 4 (bo tak jest w ustawieniach paginacji)
    assert Movie.objects.count() == response.data['count']


# POST method - dodaj nowy film
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


# GET method - szczegóły danego filmu
@pytest.mark.django_db
def test_get_movie_detail(client, set_up):
    movie = Movie.objects.first()
    response = client.get(f'/movies/{movie.pk}/', {}, format='json')
    assert response.status_code == 200  # OK

    for field in ('title', 'year', 'description', 'director', 'actor'):
        assert field in response.data  # czy powyższe pola znajdują się w response.data


# DELETE method - skasuj dany film
@pytest.mark.django_db
def test_delete_movie(client, set_up):
    movie = Movie.objects.first()
    user = User.objects.create(username='test')
    client.force_authenticate(user)
    response = client.delete(f'/movies/{movie.pk}/', {}, format='json')
    assert response.status_code == 204  # no content

    movies_id = [movie.pk for movie in Movie.objects.all()]
    assert movie.pk not in movies_id  # czy movie się usunęło i nie ma go w zbiorze aktualnych filmów


# PUT method - uaktualnij dany film
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


########################################################################################################################


# POST method - dodaj nowe kino
@pytest.mark.django_db
def test_add_cinema(client, set_up):
    cinemas_before = Cinema.objects.count()
    new_cinema = fake_cinema_data()
    response = client.post('/cinemas/', new_cinema, format='json')
    assert response.status_code == 403  # forbidden

    user = User.objects.create(username='test')
    client.force_authenticate(user)
    response = client.post('/cinemas/', new_cinema, format='json')
    assert response.status_code == 201  # created
    assert Cinema.objects.count() == cinemas_before + 1

    # print(response.data)  # {'name': 'Kino Myśliwska', 'city': 'Czechowice-Dziedzice', 'movies': []}

    for key, value in new_cinema.items():  # dict_items([('name', 'Kino Myśliwska'), ('city', 'Czechowice-Dziedzice')])
        assert key in response.data
        assert response.data[key] == value


# GET method - wyświetlenie listy kin
@pytest.mark.django_db
def test_get_cinema_list(client, set_up):

    response = client.get('/cinemas/', {}, format='json')
    assert response.status_code == 200  # OK
    assert Cinema.objects.count() == response.data['count']


# GET method - szczegóły danego kina
@pytest.mark.django_db
def test_get_cinema_detail(client, set_up):
    cinema = Cinema.objects.first()
    response = client.get(f'/cinemas/{cinema.pk}/', {}, format='json')
    assert response.status_code == 200

    # print(response.data)  # {'name': 'Kino Lazurowa', 'city': 'Chojnice', 'movies': ['http://testserver/movies/62/', 'http://testserver/movies/64/', 'http://testserver/movies/69/']}

    for field in ('name', 'city', 'movies'):
        assert field in response.data


# DELETE method - usunięcie danego kina
@pytest.mark.django_db
def test_delete_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.delete(f'/cinemas/{cinema.pk}/', {}, format='json')
    assert response.status_code == 403  # forbidden

    user = User.objects.create(username='test')
    client.force_authenticate(user)
    response = client.delete(f'/cinemas/{cinema.pk}/', {}, format='json')
    assert response.status_code == 204  # no content

    cinemas_id = [c.id for c in Cinema.objects.all()]
    assert cinema.pk not in cinemas_id  # czy danego kina już nie ma w bazie danych


# PUT method - uaktualnienie danego kina
@pytest.mark.django_db
def test_update_cinema(client, set_up):
    cinema = Cinema.objects.first()
    response = client.patch(f'/cinemas/{cinema.pk}/', {}, format='json')
    cinema_data = response.data
    new_name = 'New Name'
    cinema_data['name'] = new_name
    response = client.patch(f'/cinemas/{cinema.pk}/', cinema_data, format='json')
    assert response.status_code == 403  # forbidden

    user = User.objects.create(username='test')
    client.force_authenticate(user)
    response = client.patch(f'/cinemas/{cinema.pk}/', cinema_data, format='json')
    assert response.status_code == 200  # OK

    cinema_obj = Cinema.objects.get(pk=cinema.pk)
    assert cinema_obj.name == new_name  # czy zmieniła się nazwa kina
