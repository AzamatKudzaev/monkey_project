from django import forms
from .models import Article, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

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
        title = self.cleaned_data['title']
        if len(title) < 10:
            raise ValidationError('Заголовок должен быть не менее 10 символов')
        if title.isalpha():
            first_letter = title[0]
            title = first_letter.upper() + self.cleaned_data['title'][1:]
            return title
        raise ValidationError('Заголовок должен начинаться со слова')


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


