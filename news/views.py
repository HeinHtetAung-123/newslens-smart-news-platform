from django.shortcuts import render
from .models import Article, Category


def home(request):
    articles = Article.objects.select_related("source", "category").all()
    categories = Category.objects.all()

    context = {
        "articles": articles,
        "categories": categories,
    }

    return render(request, "news/home.html", context)