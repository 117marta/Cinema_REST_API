from random import sample, choice, randint
from cinema_app.models import Person, Movie
from faker import Faker

faker = Faker('pl_PL')


# Zwraca losowy obiekt Person z bazy danych
def random_person():
    people = Person.objects.all()
    return choice(people)


# Zwraca pierwszy obiekt Person, który pasuje do name
def find_person_by_name(name):
    return Person.objects.filter(name=name).first()


# Tworzy słownik z danymi od filmu
def fake_movie_data():
    movie_data = {
        'title': f'{faker.job()} {faker.first_name()}',
        'description': faker.sentence(),
        'year': int(faker.year()),
        'director': random_person().name,
    }
    people = Person.objects.all()
    actors = sample(list(people), randint(1, len(people)))  # lista 'osób' o długości losowej od 1 do liczby 'osób'
    actors_name = [a.name for a in actors]  # z powyższej listy bierzemy tylko imiona osób
    movie_data['actor'] = actors_name
    return movie_data


# Tworzy nowy fake film i zapisuje go do bazy danych
def create_fake_movie():
    movie_data = fake_movie_data()
    movie_data['director'] = find_person_by_name(movie_data['director'])
    actors = movie_data['actor']
    del movie_data['actor']
    new_movie = Movie.objects.create(**movie_data)
    for a in actors:
        new_movie.actor.add(find_person_by_name(a))
