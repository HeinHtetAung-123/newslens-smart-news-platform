from django.contrib import admin
from .models import Category, NewsSource, Article


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(NewsSource)
class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ("name", "website_url")
    search_fields = ("name",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "category", "published_at")
    list_filter = ("source", "category", "published_at")
    search_fields = ("title", "description", "summary", "content")