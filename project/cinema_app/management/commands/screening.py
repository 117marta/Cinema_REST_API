from django.core.management.base import BaseCommand
from cinema_app.models import Screening, Cinema, Movie
import datetime
import pytz


class Command(BaseCommand):
    def handle(self, *args, **options):
        notimetodie = Movie.objects.get(id=3)
        skyfall = Movie.objects.get(id=4)
        greenmile = Movie.objects.get(id=5)
        forrestgump = Movie.objects.get(id=6)
        residentevil = Movie.objects.get(id=7)

        lublincinema = Cinema.objects.get(id=1)
        warsawcinema = Cinema.objects.get(id=2)
        helios = Cinema.objects.get(id=3)
        luna = Cinema.objects.get(id=4)
        cracowcinema = Cinema.objects.get(id=5)
        kinostudio = Cinema.objects.get(id=6)
        ars = Cinema.objects.get(id=7)
        danzigcinema = Cinema.objects.get(id=8)
        multikino = Cinema.objects.get(id=9)
        wroclawcinema = Cinema.objects.get(id=10)

        Screening.objects.create(date=datetime.datetime(2022, 1, 14, 18, 30, 00000, tzinfo=pytz.UTC), cinema=lublincinema, movie=notimetodie)
        Screening.objects.create(date=datetime.datetime(2022, 1, 15, 16, 30, 00000, tzinfo=pytz.UTC), cinema=lublincinema, movie=forrestgump)
        Screening.objects.create(date=datetime.datetime(2022, 1, 14, 16, 00, 00000, tzinfo=pytz.UTC), cinema=warsawcinema, movie=skyfall)
        Screening.objects.create(date=datetime.datetime(2022, 1, 15, 16, 00, 00000, tzinfo=pytz.UTC), cinema=warsawcinema, movie=residentevil)
        Screening.objects.create(date=datetime.datetime(2022, 1, 16, 19, 00, 00000, tzinfo=pytz.UTC), cinema=helios, movie=greenmile)
        Screening.objects.create(date=datetime.datetime(2022, 1, 17, 21, 00, 00000, tzinfo=pytz.UTC), cinema=helios, movie=notimetodie)
        Screening.objects.create(date=datetime.datetime(2022, 1, 14, 21, 00, 00000, tzinfo=pytz.UTC), cinema=luna, movie=forrestgump)
        Screening.objects.create(date=datetime.datetime(2022, 1, 16, 21, 00, 00000, tzinfo=pytz.UTC), cinema=luna, movie=residentevil)
        Screening.objects.create(date=datetime.datetime(2022, 1, 15, 20, 00, 00000, tzinfo=pytz.UTC), cinema=cracowcinema, movie=greenmile)
        Screening.objects.create(date=datetime.datetime(2022, 1, 16, 17, 30, 00000, tzinfo=pytz.UTC), cinema=cracowcinema, movie=skyfall)
        Screening.objects.create(date=datetime.datetime(2022, 1, 15, 19, 30, 00000, tzinfo=pytz.UTC), cinema=kinostudio, movie=forrestgump)
        Screening.objects.create(date=datetime.datetime(2022, 1, 17, 18, 00, 00000, tzinfo=pytz.UTC), cinema=kinostudio, movie=greenmile)
        Screening.objects.create(date=datetime.datetime(2022, 1, 17, 20, 00, 00000, tzinfo=pytz.UTC), cinema=ars, movie=residentevil)
        Screening.objects.create(date=datetime.datetime(2022, 1, 14, 19, 00, 00000, tzinfo=pytz.UTC), cinema=ars, movie=forrestgump)
        Screening.objects.create(date=datetime.datetime(2022, 1, 15, 15, 30, 00000, tzinfo=pytz.UTC), cinema=danzigcinema, movie=skyfall)
        Screening.objects.create(date=datetime.datetime(2022, 1, 15, 21, 00, 00000, tzinfo=pytz.UTC), cinema=danzigcinema, movie=notimetodie)
        Screening.objects.create(date=datetime.datetime(2022, 1, 16, 17, 00, 00000, tzinfo=pytz.UTC), cinema=multikino, movie=forrestgump)
        Screening.objects.create(date=datetime.datetime(2022, 1, 17, 19, 00, 00000, tzinfo=pytz.UTC), cinema=multikino, movie=residentevil)
        Screening.objects.create(date=datetime.datetime(2022, 1, 15, 17, 30, 00000, tzinfo=pytz.UTC), cinema=wroclawcinema, movie=greenmile)
        Screening.objects.create(date=datetime.datetime(2022, 1, 14, 20, 00, 00000, tzinfo=pytz.UTC), cinema=wroclawcinema, movie=skyfall)
