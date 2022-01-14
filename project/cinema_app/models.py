from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='movies_directed', null=True)
    year = models.SmallIntegerField()
    actor = models.ManyToManyField(Person, related_name='movies_cast')

    def __str__(self):
        return self.title


class Cinema(models.Model):
    name = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    movies = models.ManyToManyField(Movie, through='Screening')  # łączy kino z filmem


class Screening(models.Model):  # łączy kina z filmami + data seansu
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()
