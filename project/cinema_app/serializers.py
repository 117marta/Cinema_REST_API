from rest_framework import serializers
from .models import Person, Movie


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
