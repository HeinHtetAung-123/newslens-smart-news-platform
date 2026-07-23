from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, SavedArticle, BreakingNewsAlert, UserPreference
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .services import generate_bias_insight
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    articles = Article.objects.select_related("source", "category").all()
    categories = Category.objects.all()
    breaking_alerts = BreakingNewsAlert.objects.select_related(
        "article",
        "article__source",
        "article__category"
    ).filter(is_active=True)[:3]

    recommended_articles = []

    if request.user.is_authenticated:
        preference = UserPreference.objects.filter(user=request.user).first()

        if preference:
            preferred_categories = preference.preferred_categories.all()

            recommended_articles = Article.objects.select_related(
                "source",
                "category"
            ).filter(
                category__in=preferred_categories
            ).order_by("-published_at")[:4]

    return render(
        request,
        "news/home.html",
        {
            "articles": articles,
            "categories": categories,
            "active_category": None,
            "breaking_alerts": breaking_alerts,
            "recommended_articles": recommended_articles,
        }
    )

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
    bias_insight = generate_bias_insight(article)

    return render(
        request,
        "news/article_detail.html",
        {
            "article": article,
            "categories": categories,
            "is_saved": is_saved,
            "related_articles": related_articles,
            "bias_insight": bias_insight,
        }
    )

def compare_sources(request, article_id):
    main_article = get_object_or_404(
        Article.objects.select_related("source", "category"),
        id=article_id
    )

    related_articles = Article.objects.select_related("source", "category").filter(
        category=main_article.category
    ).exclude(
        id=main_article.id
    ).order_by("-published_at")[:6]

    categories = Category.objects.all()

    return render(
        request,
        "news/compare_sources.html",
        {
            "main_article": main_article,
            "related_articles": related_articles,
            "categories": categories,
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

@login_required
def user_preferences(request):
    categories = Category.objects.all()

    preference, created = UserPreference.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        selected_category_ids = request.POST.getlist("categories")

        preference.preferred_categories.set(selected_category_ids)

        return redirect("news:home")

    selected_categories = preference.preferred_categories.all()

    return render(
        request,
        "news/user_preferences.html",
        {
            "categories": categories,
            "selected_categories": selected_categories,
        }
    )

@staff_member_required
def admin_dashboard(request):
    total_articles = Article.objects.count()
    total_categories = Category.objects.count()
    total_saved_articles = SavedArticle.objects.count()
    total_breaking_alerts = BreakingNewsAlert.objects.count()
    active_breaking_alerts = BreakingNewsAlert.objects.filter(is_active=True).count()

    latest_articles = Article.objects.select_related(
        "source",
        "category"
    ).order_by("-published_at")[:5]

    latest_alerts = BreakingNewsAlert.objects.select_related(
        "article",
        "article__source"
    ).order_by("-created_at")[:5]

    categories = Category.objects.all()

    return render(
        request,
        "news/admin_dashboard.html",
        {
            "total_articles": total_articles,
            "total_categories": total_categories,
            "total_saved_articles": total_saved_articles,
            "total_breaking_alerts": total_breaking_alerts,
            "active_breaking_alerts": active_breaking_alerts,
            "latest_articles": latest_articles,
            "latest_alerts": latest_alerts,
            "categories": categories,
        }
    )