
from django.contrib import admin
from .models import Article, Profile
from django.db.models import QuerySet
# Register your models here.




@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # list_display = ['title', 'publication', 'article_kind', 'text',
    #                 'pub_date', 'change_date', 'article_views', 'article_likes', 'article_dislikes']
    # list_editable = ['text', 'publication', 'article_kind']
    # ordering = ['-pub_date', 'title']
    # list_per_page = 10
    # search_fields = ['title__startwith']
    # actions = ['set_publication_on', 'set_publication_off']
    # list_filter = ['article_kind']  
    # exclude = ['article_views', 'article_likes', 'article_dislikes', 'profile']

    @admin.action(description='скрыть все записи')
    def set_publication_on(self, request, queryset: QuerySet):
        queryset.update(publication=0)

    @admin.action(description='Вывести все записи')
    def set_publication_off(self, request, queryset: QuerySet):
        queryset.update(publication=1)


admin.site.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'sex', 'last_name', 'mail',
#                     'age', 'about_me', 'photo', 'registration_date']
#     list_editable = ['last_name', 'sex', 'mail', 'age', 'about_me', 'photo']
#     ordering = ['first_name']
#     list_per_page = 10
