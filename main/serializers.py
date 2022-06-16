from rest_framework import serializers

from main.models import Movie, Reviews, Actor, Genre


class MovieSerializers(serializers.ModelSerializer):
    '''Список фильмов'''
    class Meta:
        model = Movie
        fields = ('id', 'title', 'tagline', 'Category',)


class ReviewCreateSerializers(serializers.ModelSerializer):
    '''Добавдение одзывов'''
    class Meta:
        model = Reviews
        fields = '__all__'


class FilterReviewListSerializers(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializers = self.parent.parent.__class__(value, context=self.context)
        return serializers.data


class ReviewSerializers(serializers.ModelSerializer):
    '''Вывод отзывов'''
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializers_class = FilterReviewListSerializers
        model = Reviews
        fields = ('name', 'text', 'children',)


class MovieDetaillSerializers(serializers.ModelSerializer):
    '''Вывод фильмов'''
    Category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerializers(many=True)

    class Meta:
        model = Movie
        exclude = ('draft', )


class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name', 'id']


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'id']


class AddMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'tagline', 'discriptions', 'poster',
                  'year', 'country', 'directors', 'actors',
                  'genres', 'world_premiere', 'budget', 'fees_in_world',
                  'fees_in_usa', 'Category', 'url']

    # actors = ActorSerializers(read_only=False, many=True)
    # directors = ActorSerializers(read_only=False, many=True)
    # genres = GenreSerializers(read_only=False, many=True)

    def save(self, *args, **kwargs):
        movie = Movie(
            title=self.validated_data['title'],
            tagline=self.validated_data['tagline'],
            discriptions=self.validated_data['discriptions'],
            poster=self.validated_data['poster'],
            year=self.validated_data['year'],
            country=self.validated_data['country'],
            # directors=self.validated_data['directors'],
            # actors=self.validated_data['actors'],
            # genres=self.validated_data['genres'],
            world_premiere=self.validated_data['world_premiere'],
            budget=self.validated_data['budget'],
            fees_in_world=self.validated_data['fees_in_world'],
            fees_in_usa=self.validated_data['fees_in_usa'],
            Category=self.validated_data['Category'],
            url=self.validated_data['url'],
        )
        movie.save()
        actors = self.validated_data['actors']
        directors = self.validated_data['directors']
        genres = self.validated_data['genres']
        for i in actors:
            movie.actors.add(i)
        for i in directors:
            movie.directors.add(i)
        for i in genres:
            movie.genres.add(i)

        return movie

