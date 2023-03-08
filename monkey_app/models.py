from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female')
    }

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(150)], null=True, blank=True)
    about_me = models.TextField(max_length=500, null=True, blank=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES, 
        null=True, blank=True
        )
    photo = models.ImageField(
        upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"profile_name": self.user.username})

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Article(models.Model):

    ARTICLES_KINDS = {
        (1, 'Scientific'),
        (2, 'Review'),
        (3, 'Informational')
    }

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)  # article's author
    title = models.CharField(max_length=100, validators={
                             MinLengthValidator: 10}, null=True, blank=True)
    text = models.TextField(max_length=2000, null=True, blank=True)
    publication = models.BooleanField(default=True, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    change_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    article_views = models.IntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    article_kind = models.SmallIntegerField(
        choices=ARTICLES_KINDS
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show-article", kwargs={"id_article": self.pk})
