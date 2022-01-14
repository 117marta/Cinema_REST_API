from django.core.management.base import BaseCommand
from cinema_app.models import Cinema


class Command(BaseCommand):
    def handle(self, *args, **options):
        c1 = Cinema.objects.create()
        c1.name = 'Lublin Cinema'
        c1.city = 'Lublin'
        c1.save()

        Cinema.objects.create(name='Warsaw Cinema', city='Warsaw')
        Cinema.objects.create(name='Helios', city='Warsaw')
        Cinema.objects.create(name='Luna', city='Warsaw')
        Cinema.objects.create(name='Cracow Cinema', city='Cracow')
        Cinema.objects.create(name='Kino Studio', city='Cracow')
        Cinema.objects.create(name='Ars', city='Cracow')
        Cinema.objects.create(name='Danzig Cinema', city='Danzig')
        Cinema.objects.create(name='MultiKino', city='Danzig')
        Cinema.objects.create(name='Wrocław Cinema', city='Wrocław')
