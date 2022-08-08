from . import views
from django.urls import path


urlpatterns = [
    path('/', views.Moviesview.as_view()),
    path('moviesearch/', views.moviesearch, name='moviesearch'),
    path('category/<int:pk>', views.filtercategory, name='category'),
    path('addmovie/', views.addmovie, name='addmovie'),
    path('filter/', views.filteryear, name='filter'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>", views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>', views.ActorDetail.as_view(), name='actor_detail'),
]
