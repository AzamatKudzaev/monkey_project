from django.urls import path
from monkey_app import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about-us/', views.about_us, name='about-us'),
    path('articles/', views.articles_view, name='articles'),
    path('articles/add_new_article/', views.create_article, name='create_article'),
    path('articles/<int:id_article>/', views.show_article, name='show-article'),
    path('articles/<int:id_article>/edit/', views.edit_article, name='edit-article'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('me/<str:profile_username>/', views.show_profile, name='show_profile')
]

