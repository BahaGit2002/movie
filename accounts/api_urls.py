from django.urls import path, include
from . import api_view

urlpatterns = [
    # path('user/', api_view.UserView.as_view(), name='api_user'),
    path('user/', api_view.UserDetailView.as_view()),
    path('register/', api_view.RegistrUserView.as_view()),
]