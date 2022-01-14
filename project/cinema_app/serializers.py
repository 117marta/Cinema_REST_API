from rest_framework import serializers
from .models import Person, Movie, Cinema


# Serializacja danych z modelu do JSONa


class MovieSerializer(serializers.ModelSerializer):
    # actor = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     # read_only=True,
    #     queryset=Person.objects.all(),
    #     view_name='movies-detail',
    # )

    actor = serializers.SlugRelatedField(
        many=True,
        queryset=Person.objects.all(),
        slug_field='full_name',
    )
    director = serializers.SlugRelatedField(
        queryset=Person.objects.all(),
        slug_field='full_name',
    )

    class Meta:
        model = Movie
        fields = '__all__'


# Serializator kina
class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(  # filmy jako linki (a nie jako klucze główne - id)
        many=True,  # kina i filmy połączone są relacją wiele:wielu
        read_only=True,
        view_name='movies-detail',
    )

    class Meta:  # w tej podklasie definiujemy model, który będzie serializowany przez serializator + pola
        model = Cinema
        fields = ['name', 'city', 'movies']
