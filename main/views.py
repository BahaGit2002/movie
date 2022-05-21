from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie, Actor, Genre, Category
from .forms import ReviewForm
from django.contrib import messages


# def moviesview(request):
#     movie = Movie.objects.all()
#     return render(request, 'pages/movie_list.html', context={'movie_list': movie})


class Moviesview(ListView):
    '''Список фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'pages/movie_list.html'


# class Addmovie(ListView):
#     '''Список фильмов'''
#     model = Movie
#     queryset = Movie.objects.filter(draft=False)
#     template_name = 'pages/addmovie.html'

class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'pages/movie_detail.html'

#
# def moviedetailviews(request):
#     movie = Movie.objects.all()
#     if request.method == 'GET':
#         return render(request, 'pages/movie_detail.html', context={
#             'movie_detail': movie
#         })


class AddReview(View):
    '''Вывод одзывов'''
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))

            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


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
        title = request.POST['title']
        tagline = request.POST['tagline']
        discriptions = request.POST['discriptions']
        year = request.POST['year']
        world_premiere = request.POST['world_premiere']
        country = request.POST['country']
        actors_id = request.POST['actors']
        directors_id = request.POST['directors']
        genre_id = request.POST['genre']
        budget = request.POST['budget']
        category_id = request.POST['category']
        fees_in_world = request.POST['fees_in_world']
        fees_in_usa = request.POST['fees_in_usa']
        url = request.POST['url']
        poster = request.POST['poster']
        new_movie = Movie(title=title, tagline=tagline, discriptions=discriptions, year=year,
                          world_premiere=world_premiere, country=country, actors_id=actors_id,
                          directors_id=directors_id, genre_id=genre_id, budget=budget, category_id=category_id,
                          fees_in_world=fees_in_world, fees_in_usa=fees_in_usa, url=url, poster=poster)
        messages.success(request, 'Фильм добавлена')
        new_movie.save()
        return redirect('addmovie')
