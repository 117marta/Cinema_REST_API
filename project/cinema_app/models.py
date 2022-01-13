from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='movies_directed')
    year = models.SmallIntegerField()
    actor = models.ManyToManyField(Person, related_name='movies_cast')
