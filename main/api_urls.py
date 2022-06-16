from . import api_view
from django.urls import path


urlpatterns = [
    path('movie/', api_view.Movieview.as_view(), name='api_movie'),
    path('movie/<int:pk>', api_view.MovieDetailview.as_view()),
    path('review/', api_view.ReviewCreateView.as_view(), name='api_review'),
    path('addmovie/', api_view.AddMovieView.as_view(), name='addmovie')
]
