from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, SavedArticle, BreakingNewsAlert
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    articles = Article.objects.select_related("source", "category").all()
    categories = Category.objects.all()
    breaking_alerts = BreakingNewsAlert.objects.select_related(
        "article",
        "article__source",
        "article__category"
    ).filter(is_active=True)[:3]

    context = {
        "articles": articles,
        "categories": categories,
        "active_category": None,
        "breaking_alerts": breaking_alerts,
    }

    return render(request, "news/home.html", context)

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.select_related("source", "category").filter(category=category)
    categories = Category.objects.all()
    breaking_alerts = BreakingNewsAlert.objects.select_related(
        "article",
        "article__source",
        "article__category"
    ).filter(is_active=True)[:3]

    context = {
        "articles": articles,
        "categories": categories,
        "active_category": category,
        "breaking_alerts": breaking_alerts,
    }

    return render(request, "news/home.html", context)

def article_detail(request, article_id):
    article = get_object_or_404(
        Article.objects.select_related("source", "category"),
        id=article_id
    )

    is_saved = False

    if request.user.is_authenticated:
        is_saved = SavedArticle.objects.filter(
            user=request.user,
            article=article
        ).exists()

    related_articles = Article.objects.select_related("source", "category").filter(
        category=article.category
    ).exclude(
        id=article.id
    ).order_by("-published_at")[:4]

    categories = Category.objects.all()

    return render(
        request,
        "news/article_detail.html",
        {
            "article": article,
            "categories": categories,
            "is_saved": is_saved,
            "related_articles": related_articles,
        }
    )

def search_articles(request):
    query = request.GET.get("q", "").strip()
    categories = Category.objects.all()
    articles = Article.objects.none()

    if query:
        articles = Article.objects.select_related("source", "category").filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(summary__icontains=query) |
            Q(content__icontains=query) |
            Q(source__name__icontains=query) |
            Q(category__name__icontains=query)
        )

    context = {
        "query": query,
        "articles": articles,
        "categories": categories,
    }

    return render(request, "news/search_results.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("news:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form,
        "categories": Category.objects.all(),
    }

    return render(request, "registration/register.html", context)

@login_required
def save_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    SavedArticle.objects.get_or_create(
        user=request.user,
        article=article
    )

    return redirect("news:article_detail", article_id=article.id)

@login_required
def remove_saved_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    SavedArticle.objects.filter(
        user=request.user,
        article=article
    ).delete()

    return redirect("news:saved_articles")

@login_required
def saved_articles(request):
    saved_items = SavedArticle.objects.select_related(
        "article",
        "article__source",
        "article__category"
    ).filter(user=request.user)

    categories = Category.objects.all()

    context = {
        "saved_items": saved_items,
        "categories": categories,
    }

    return render(request, "news/saved_articles.html", context)