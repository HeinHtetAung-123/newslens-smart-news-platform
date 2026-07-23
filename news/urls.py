from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.home, name="home"),
    path("category/<slug:slug>/", views.category_articles, name="category_articles"),
    path("article/<int:article_id>/", views.article_detail, name="article_detail"),
    path("search/", views.search_articles, name="search_articles"),
    path("register/", views.register, name="register"),
    path("article/<int:article_id>/save/", views.save_article, name="save_article"),
    path("article/<int:article_id>/remove/", views.remove_saved_article, name="remove_saved_article"),
    path("saved/", views.saved_articles, name="saved_articles"),
    path("article/<int:article_id>/compare/", views.compare_sources, name="compare_sources"),
    path("preferences/", views.user_preferences, name="user_preferences"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
]
