from rest_framework import serializers
from .models import Person, Movie


# Serializacja danych z modelu do JSONa
class MovieSerializer(serializers.Serializer):
    actors = serializers.SlugRelatedField(
        many=True,
        queryset=Person.objects.all(),
        slug_field='name',
    )
    directors = serializers.SlugRelatedField(
        queryset=Person.objects.all(),
        slug_field='name',
    )

    class Meta:
        model = Movie
        fields = '__all__'
