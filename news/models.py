from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class NewsSource(models.Model):
    name = models.CharField(max_length=150, unique=True)
    website_url = models.URLField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name="articles"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="articles"
    )
    description = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    original_url = models.URLField()
    published_at = models.DateTimeField()

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def get_quick_summary(self):
        from .services import generate_quick_summary
        return generate_quick_summary(self)

class SavedArticle(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="saved_articles"
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="saved_by"
    )
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "article")
        ordering = ["-saved_at"]

    def __str__(self):
        return f"{self.user.username} saved {self.article.title}"

class BreakingNewsAlert(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="breaking_alerts"
    )
    alert_title = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.alert_title