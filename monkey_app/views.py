
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from monkey_app.models import Article, Profile
from django.db.models import Sum, Max, Min, Count, Avg, Value
from .forms import ArticleForm, RegisterUserForm, ProfileForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def main(request):
    articles = Article.objects.filter(publication=True)
    if len(articles) <= 11:
        sorted_articles = articles.order_by(
            '-article_views', '-title').exclude(article_views=0)
    else:
        sorted_articles = articles.order_by(
            '-article_views', '-title').exclude(article_views=0)[:11]

    context = {
        'sorted_articles': sorted_articles,
    }

    return render(request, 'monkey_app/main.html', context=context)


def about_us(request):
    return render(request, 'monkey_app/about-us.html')


def articles_view(request):
    articles = Article.objects.order_by('-pub_date').filter(publication=True)
    agg = articles.aggregate(Count('pk'))
    context = {
        'articles': articles,
        'agg': agg
    }
    return render(request, 'monkey_app/articles.html', context=context)


def show_article(request, id_article):
    article = get_object_or_404(
        Article, id=id_article)
    article.article_views += 1
    article.save()

    context = {
        'article': article,
    }
    return render(request, 'monkey_app/show_article.html', context=context)


def create_article(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            article_kind = form.cleaned_data['article_kind']
            Article.objects.create(
                author=author,
                title=title,
                text=text,
                image=image,
                article_kind=article_kind
            )
            return HttpResponseRedirect(reverse('articles'))
    else:
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, 'monkey_app/create_article.html', context=context)


def show_my_profile(request, profile_username):
    profile = User.objects.get(username=profile_username)
    context = {
        'profile_username': profile_username,
    }
    return render(request, 'monkey_app/show_my_profile.html', context=context)


def edit_article(request, id_article):
    article = Article.objects.get(pk=id_article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("show-article", kwargs={"id_article": article.pk}))

    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
        'article': article
    }
    return render(request, 'monkey_app/create_article.html', context=context)


class LoginUser(LoginView):
    form = AuthenticationForm
    template_name = 'monkey_app/login.html'


def register(request):

    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('login'))

    else:
        user_form = RegisterUserForm()
        profile_form = ProfileForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'monkey_app/register.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


def show_profile(request, profile_username):
    profile = User.objects.get(username=profile_username)
    if profile == request.user:
        return HttpResponseRedirect(reverse('show-my-profile', kwargs={"profile_username": profile_username}))
    context = {
        'profile': profile
    }
    return render(request, 'monkey_app/show_profile.html', context=context)

