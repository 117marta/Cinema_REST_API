from random import sample, choice, randint
from cinema_app.models import Person, Movie, Cinema, Screening
from faker import Faker
import pytz
from project.settings import TIME_ZONE

faker = Faker('pl_PL')
TZ = pytz.timezone(TIME_ZONE)


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


########################################################################################################################


# Zwraca 3 losowe kina z bazy danych
def random_movies():
    movies = list(Movie.objects.all())
    return sample(movies, 3)  # lista 3 kin


# Tworzy fake dane dla kina
def fake_cinema_data():
    return {
        'name': f'Kino {faker.street_name()}',
        'city': faker.city(),
    }


# Dodaje seanse dla konkretnego kina
def add_screenings(cinema):
    movies = random_movies()
    for m in movies:
        Screening.objects.create(cinema=cinema, movie=m, date=faker.date_time(tzinfo=TZ))


# Tworzy fake kino z fake seansami
def create_fake_cinema():
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screenings(cinema)
