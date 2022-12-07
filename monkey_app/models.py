from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
# Create your models here.


class Profile(models.Model):
    SEX_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female')
    }

    username = models.CharField(max_length=40, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    mail = models.EmailField(max_length=254, null=True, blank=True)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(150)], null=True, blank=True)
    about_me = models.TextField(max_length=500, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, null=True, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_name": self.first_name})


class Article(models.Model):

    ARTICLES_KINDS = {
        ('Not selected', 'Not selected'),
        ('Scientific', 'Scientific'),
        ('Review', 'Review'),
        ('Informational', 'Informational')
    }
 
    profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)  # article's author
    title = models.CharField(max_length=100, validators={MinLengthValidator: 10}, null=True, blank=True)
    text = models.TextField(max_length=2000, null=True, blank=True)
    publication = models.BooleanField(default=True, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    change_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    article_views = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    article_likes = models.IntegerField(default=0, null=True, blank=True)
    article_dislikes = models.IntegerField(default=0, null=True, blank=True)
    article_kind = models.CharField(
        max_length=25,
        choices=ARTICLES_KINDS,
        default='NS'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show-article", kwargs={"id_article": self.pk})
