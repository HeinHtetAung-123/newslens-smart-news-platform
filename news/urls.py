from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.category_articles, name="category_articles"),
    path("article/<int:article_id>/", views.article_detail, name="article_detail"),
    path("search/", views.search_articles, name="search_articles"),
    path("register/", views.register, name="register"),
]