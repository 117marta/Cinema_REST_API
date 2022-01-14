from django.core.management.base import BaseCommand
from cinema_app.models import Person


class Command(BaseCommand):
    def handle(self, *args, **options):
        p1 = Person.objects.create()
        p1.first_name = 'Jan'
        p1.last_name = 'Kowalski'
        p1.save()

        Person.objects.create(first_name='Daniel', last_name='Craig')
        Person.objects.create(first_name='Cary Joji', last_name='Fukunaga')
        Person.objects.create(first_name='Neal', last_name='Purvis')
        Person.objects.create(first_name='Sam', last_name='Mendes')
        Person.objects.create(first_name='Tom', last_name='Hanks')
        Person.objects.create(first_name='Frank', last_name='Darabont')
        Person.objects.create(first_name='Robert', last_name='Zemeckis')
        Person.objects.create(first_name='Eric', last_name='Roth')
        Person.objects.create(first_name='Lea', last_name='Seydoux')
        Person.objects.create(first_name='Milla', last_name='Jovovich')
        Person.objects.create(first_name='Paul W.S.', last_name='Anderson')
