from rest_framework import serializers
from .models import Person, Movie, Cinema, Screening
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


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
        view_name='movies-detail',  # w URL 'name=...', żeby przenosiło do szczegółów Movie/pk
    )

    class Meta:  # w tej podklasie definiujemy model, który będzie serializowany przez serializator + pola
        model = Cinema
        fields = ['name', 'city', 'movies']


# Serializator seansu
class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(
        queryset=Cinema.objects.all(),
        slug_field='name',
    )
    movie = serializers.SlugRelatedField(
        queryset=Movie.objects.all(),
        slug_field='title',
    )

    class Meta:
        model = Screening
        exclude = ['id']


# Rejestracja nowego użytkownika
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,  # to pole pojawia się przy tworzeniu/modyfikacji użytkownika. Nie ma go w serializacji
        required=True,
        validators=[validate_password],
        style={'input_type': 'password', 'placeholder': 'Input Password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password', 'placeholder': 'Confirm Password'}
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email']
        extra_kwargs = {
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Password fields must be the same!'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
