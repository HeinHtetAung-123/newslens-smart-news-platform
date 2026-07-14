from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.category_articles, name="category_articles"),
]