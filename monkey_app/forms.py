from django import forms
from .models import Article, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class ArticleForm(forms.Form):

#     NOT_SELECTED = 'not selected'
#     SCINEFIC = 'scinefic'
#     REVIEW = 'review'
#     INFORMATIONAL = 'informational'

#     ARTICLES_KINDS = {
#         (NOT_SELECTED, 'Not selected'),
#         (SCINEFIC, 'Scientific'),
#         (REVIEW, 'Review'),
#         (INFORMATIONAL, 'Informational')
#     }

#     title = forms.CharField(label="Заголовок",min_length=10, max_length=50, error_messages={
#         'min_lenght': 'Слишком мало символов',
#         'required': 'поле обязательное'
#     })
#     text = forms.CharField(label="Основной текст", max_length=500, min_length=50,widget=forms.Textarea(attrs={'rows':20, 'cols':150}))
#     image = forms.ImageField(label="Фото", required=False)
#     article_kind = forms.ChoiceField(label="Тип статьи", choices=ARTICLES_KINDS)


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


