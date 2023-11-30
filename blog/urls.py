from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('articles/', views.articles, name='articles'),

    # update the article url
    path('<slug:article>/', views.article, name='article'),
]
