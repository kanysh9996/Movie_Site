from rest_framework import serializers
from .models import *

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class RatingSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['movie_rating']


class DirectorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']


class DirectorPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorPhoto
        fields  = ['director_image']

class DirectorSerializer(serializers.ModelSerializer):
    director_image = DirectorPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Director
        fields = ['id', 'director_name', 'bio', 'age', 'director_image']


class ActorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorImage
        fields = ['actor_images']


class ActorSerializer(serializers.ModelSerializer):
    actor_images = ActorImageSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['id', 'actor_name', 'bio', 'age', 'actor_images']


class ActorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']



class RatingSerializer(serializers.ModelSerializer):
    user = ProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%y %H:%M'))
    class Meta:
        model = Rating
        fields  = ['user', 'movie_rating', 'stars', 'text', 'created_date']


class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'


class MovieLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']


class MovieSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    class Meta:
        model = Movie
        fields = ['movie_name', 'year', 'country']


class MovieListSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    rating = RatingSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country', 'genre', 'rating']



class CountryListSerializer(serializers.ModelSerializer):
    country = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'country_name', 'country']



class GenreListSerializer(serializers.ModelSerializer):
    genre = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['genre']


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    director = DirectorSimpleSerializer(many=True)
    actor = ActorSimpleSerializer(many=True)
    rating = RatingSerializer(many=True, read_only=True)
    moments = MomentsSerializer(many=True, read_only=True)
    movie_languages = MovieLanguagesSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country', 'director', 'genre', 'types',  'movie_time',
                  'movie_trailer',  'movie_image', 'status_movie', 'actor', 'description', 'movie_languages',
                  'rating', 'moments' ]


class CountryDetailSerializer(serializers.ModelSerializer):
    country = MovieDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['country_name', 'country']


class GenreDetailSerializer(serializers.ModelSerializer):
    genre = MovieDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['genre']

class FavoriteMovieSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True, source='movie')

    class Meta:
        model = FavoriteMovie
        fields = ['id', 'cart', 'movie_favorite', 'movie_id']


class FavoriteSerializer(serializers.ModelSerializer):
    movie_favorite = FavoriteMovieSerializer(many=True, read_only=True)
    class Meta:
        model = Favorite
        fields = ['id', 'movie_favorite']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['id', '']