from django.core.management.base import BaseCommand
from cinema_app.models import Person


class Command(BaseCommand):
    def handle(self, *args, **options):
        p1 = Person.objects.create()
        p1.name = 'Jan Kowalski'
        p1.save()

        Person.objects.create(name='Daniel Craig')
        Person.objects.create(name='Cary Joji Fukunaga')
        Person.objects.create(name='Neal Purvis')
        Person.objects.create(name='Sam Mendes')
        Person.objects.create(name='Tom Hanks')
        Person.objects.create(name='Frank Darabont')
        Person.objects.create(name='Robert Zemeckis')
        Person.objects.create(name='Eric Roth')
        Person.objects.create(name='Lea Seydoux')
        Person.objects.create(name='Milla Jovovich')
        Person.objects.create(name='Paul W.S. Anderson')
