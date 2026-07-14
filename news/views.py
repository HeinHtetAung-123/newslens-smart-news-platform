from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def home(request):
    articles = Article.objects.select_related("source", "category").all()
    categories = Category.objects.all()

    context = {
        "articles": articles,
        "categories": categories,
        "active_category": None,
    }

    return render(request, "news/home.html", context)


def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.select_related("source", "category").filter(category=category)
    categories = Category.objects.all()

    context = {
        "articles": articles,
        "categories": categories,
        "active_category": category,
    }

    return render(request, "news/home.html", context)


def article_detail(request, article_id):
    article = get_object_or_404(
        Article.objects.select_related("source", "category"),
        id=article_id
    )
    categories = Category.objects.all()

    context = {
        "article": article,
        "categories": categories,
    }

    return render(request, "news/article_detail.html", context)