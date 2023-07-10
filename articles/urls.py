from django.urls import path
from articles import views


app_name = 'articles'

urlpatterns = [
    path('', views.articles, name='home'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:pk>', views.article, name='article'),
    path('newsletter/', views.newsletter, name='newsletter'),

]
