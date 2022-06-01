from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Actor, Genre, Category
from .forms import ReviewForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


# def moviesview(request):
#     movie = Movie.objects.all()
#     return render(request, 'pages/movie_list.html', context={'movie_list': movie})
class GenreYear:

    def get_genres(self):
        return Genre.objects.all()

    def get_year(self):
        return Movie.objects.filter(draft=False).values('year')


class Moviesview(GenreYear, ListView):
    '''Список фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'pages/movie_list.html'


# class Addmovie(ListView):
#     '''Список фильмов'''
#     model = Movie
#     queryset = Movie.objects.filter(draft=False)
#     template_name = 'pages/addmovie.html'

class MovieDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'pages/movie_detail.html'


class ActorDetail(GenreYear, DetailView):
    model = Actor
    slug_field = 'name'
    template_name = 'pages/actor.html'


class AddReview(GenreYear, View):
    '''Вывод одзывов'''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.name = request.user.username
            if request.POST.get("parent", None):
                print(request.POST.get("parent"))
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


def category(request):
    if request.method == 'GET':
        print(request)


def addmovie(request):
    if request.method == 'GET':
        category = Category.objects.all()
        actors = Actor.objects.all()
        genre = Genre.objects.all()
        context = {
            'category': category,
            'actors': actors,
            'genre': genre
        }
        return render(request, 'pages/addmovie.html', context)
    if request.method == 'POST':
        actors_id = request.POST.getlist('actors')
        directors_id = request.POST['directors']
        genre_id = request.POST['genre']
        title = request.POST['title']
        tagline = request.POST['tagline']
        discriptions = request.POST['discriptions']
        year = request.POST['year']
        world_premiere = request.POST['world_premiere']
        country = request.POST['country']
        budget = request.POST['budget']
        category_id = request.POST['category']
        fees_in_world = request.POST['fees_in_world']
        fees_in_usa = request.POST['fees_in_usa']
        url = request.POST['url']
        poster = request.FILES.get('poster')
        print(poster)
        new_movie = Movie(title=title, tagline=tagline, discriptions=discriptions, year=year,
                          world_premiere=world_premiere, country=country,
                          budget=budget, Category_id=category_id,
                          fees_in_world=fees_in_world, fees_in_usa=fees_in_usa, url=url, poster=poster)
        messages.success(request, 'Фильм добавлена')

        new_movie.save()
        for i in actors_id:
            new_movie.actors.add(Actor.objects.get(id=int(i)))
        for i in directors_id:
            new_movie.directors.add(Actor.objects.get(id=int(i)))
        for i in genre_id:
            new_movie.genres.add(Genre.objects.get(id=int(i)))
        return redirect('addmovie')


class FilterMovieView(GenreYear, ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(year__in=self.request.GET.getlist('year'),)
        print(queryset)
        return queryset
