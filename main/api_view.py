from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Movie, Reviews
from .serializers import MovieSerializers, MovieDetaillSerializers, ReviewCreateSerializers, AddMovieSerializers


class Movieview(APIView):
    '''Список фильмов'''
    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data)


class MovieDetailview(APIView):
    '''Вывод фильмов'''
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetaillSerializers(movie)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    '''Добавление отзывов к фильму'''
    def post(self, request):
        review = ReviewCreateSerializers(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class AddMovieView(CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = AddMovieSerializers

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AddMovieSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)



