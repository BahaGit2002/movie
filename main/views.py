from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Movie
from .forms import ReviewForm


# def moviesview(request):
#     movie = Movie.objects.all()
#     return render(request, 'pages/movie_list.html', context={'movie_list': movie})


class Moviesview(ListView):
    '''Список фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'pages/movie_list.html'


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

