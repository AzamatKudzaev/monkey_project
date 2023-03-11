from django import forms
from .models import Article, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'image', 'article_kind']
        labels = {
            'title': 'Заголовок',
            'text': 'Основной текст',
            'image': 'Картинка',
            'article_kind': 'Тип статьи'
        }
        error_messages = {
            'name': {
                'required': 'Поле обязательно'
            },
            'text': {
                'required': 'Поле обязательно'
            }
        }

    def clean_title(self):
        first_letter = self.cleaned_data['title'][0]
        if first_letter.isalpha():
            title = first_letter.upper() + self.cleaned_data['title'][1:]
            return title
        return self.cleaned_data['title']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('age', 'about_me', 'gender', 'photo')
        labels = {
            'age': 'Возраст',
            'about_me': 'Обо мне',
            'gender': 'Пол',
            'photo': 'Фото профиля',
        }   


