from django.core.management.base import BaseCommand
from cinema_app.models import Person, Movie, Cinema


class Command(BaseCommand):
    def handle(self, *args, **options):
        notimetodie = Movie.objects.get(id=3)
        skyfall = Movie.objects.get(id=4)
        greenmile = Movie.objects.get(id=5)
        forrestgump = Movie.objects.get(id=6)
        residentevil = Movie.objects.get(id=7)


        # MOVIES
        CF = Person.objects.get(id=3)
        notimetodie.director = CF
        notimetodie.save()

        greenmile.director = Person.objects.get(id=7)
        greenmile.save()

        forrestgump.director = Person.objects.get(id=8)
        forrestgump.save()


        # ACTORS
        DC = Person.objects.get(id=2)
        TH = Person.objects.get(id=6)
        LS = Person.objects.get(id=10)
        MJ = Person.objects.get(id=11)

        notimetodie.actor.add(DC)
        notimetodie.actor.add(LS)
        skyfall.actor.add(DC)
        greenmile.actor.add(TH)
        forrestgump.actor.add(TH)
        residentevil.actor.add(MJ)

