from . import views
from django.urls import path


urlpatterns = [
    path('', views.Moviesview.as_view()),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>", views.AddReview.as_view(), name='add_review'),
]