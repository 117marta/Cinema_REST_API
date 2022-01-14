from django.core.management.base import BaseCommand
from cinema_app.models import Movie, Person


class Command(BaseCommand):
    def handle(self, *args, **options):
        Movie.objects.create(title="No Time To Die", description="Movie starring James Bond", year=2021)
        Movie.objects.create(title="Skyfall", description="Movie starring James Bond", year=2012, director_id=5)
        Movie.objects.create(title="The Green Mile", year=1999, description="Movie starring Paul Edgecomb")
        Movie.objects.create(title="Forrest Gump", year=1994, description="Movie starring Forrest Gump")

        PA = Person.objects.get(id=12)
        Movie.objects.create(title="Resident Evil", year=2002, director=PA, description="Horror film about a virus in a secret research complex")
