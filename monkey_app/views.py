
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from monkey_app.models import Article, Profile
from django.db.models import Sum, Max, Min, Count, Avg, Value
from .forms import ArticleForm, RegisterUserForm
from django.urls import reverse


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
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('articles'))
    else:
        form = ArticleForm()

    context = {
        'form': form
    }
    return render(request, 'monkey_app/create_article.html', context=context)


def show_profile(request, profile_name):
    return HttpResponse('profile -', profile_name)


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


def login(request):
    
    return render(request, 'monkey_app/login.html')

    
def register(request):
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else: 
        form = RegisterUserForm

    context = {
        'form': form,
    }
    return render(request, 'monkey_app/register.html', context=context)
