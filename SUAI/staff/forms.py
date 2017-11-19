from django.contrib.auth.models import User
from django import forms
from ..models import Image, News


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['source', 'name', 'description']


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'content']


class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
