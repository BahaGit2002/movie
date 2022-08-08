from django.forms import ModelForm
from django import forms
from djoser.conf import User

from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
