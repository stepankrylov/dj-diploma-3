from django.contrib.auth.models import User
from django import forms
from app.models import Review


class UserRegistrationForm(forms.ModelForm):
    email = forms.CharField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)


class ReviewForm(forms.ModelForm):
    name = forms.CharField(label='Имя')
    content = forms.CharField(widget=forms.Textarea, label='Содержание')

    class Meta(object):
        model = Review
        fields = ('name', 'content', )


