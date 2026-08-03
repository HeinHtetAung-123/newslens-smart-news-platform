import requests

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from news.models import Article, Category, NewsSource, BreakingNewsAlert


class Command(BaseCommand):
    help = "Fetch real news articles from NewsAPI and store them in the database."

    NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

    CATEGORY_MAP = {
        "business": "Business",
        "entertainment": "Entertainment",
        "general": "Local News",
        "health": "Health",
        "science": "Science",
        "sports": "Sports",
        "technology": "Technology",
    }

    PAGE_SIZE = 100
    MAX_PAGES_PER_CATEGORY = 3
    MAX_ACTIVE_BREAKING_ALERTS = 8

    def handle(self, *args, **options):
        api_key = settings.NEWS_API_KEY

        if not api_key:
            self.stderr.write(
                self.style.ERROR("NEWS_API_KEY is missing. Add it to your .env file.")
            )
            return

        total_created = 0
        total_updated = 0

        for api_category, local_category_name in self.CATEGORY_MAP.items():
            created_count, updated_count = self.fetch_category(
                api_key,
                api_category,
                local_category_name
            )

            total_created += created_count
            total_updated += updated_count

        self.limit_active_breaking_alerts()

        self.stdout.write(
            self.style.SUCCESS(
                f"News fetch completed. {total_created} new articles added, "
                f"{total_updated} existing articles updated."
            )
        )

    def fetch_category(self, api_key, api_category, local_category_name):
        category, _ = Category.objects.get_or_create(
            name=local_category_name,
            defaults={"slug": local_category_name.lower().replace(" ", "-")},
        )

        created_count = 0
        updated_count = 0

        for page in range(1, self.MAX_PAGES_PER_CATEGORY + 1):
            params = {
                "apiKey": api_key,
                "country": "us",
                "category": api_category,
                "pageSize": self.PAGE_SIZE,
                "page": page,
            }

            response = requests.get(self.NEWS_API_URL, params=params, timeout=20)

            if response.status_code != 200:
                self.stderr.write(
                    self.style.ERROR(
                        f"Failed to fetch {api_category} news on page {page}. "
                        f"Status: {response.status_code}"
                    )
                )
                self.stderr.write(response.text)
                break

            data = response.json()
            articles = data.get("articles", [])

            if not articles:
                break

            for item in articles:
                article_created, article_updated, article = self.save_article(
                    item,
                    category
                )

                if article_created:
                    created_count += 1

                    if created_count <= 2:
                        self.create_breaking_alert(article)

                elif article_updated:
                    updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{local_category_name}: {created_count} new articles added, "
                f"{updated_count} existing articles updated."
            )
        )

        return created_count, updated_count

    def save_article(self, item, category):
        title = item.get("title")
        original_url = item.get("url")
        source_name = item.get("source", {}).get("name") or "Unknown Source"

        if not title or not original_url:
            return False, False, None

        source, _ = NewsSource.objects.get_or_create(
            name=source_name,
            defaults={"website_url": original_url},
        )

        published_raw = item.get("publishedAt")
        published_at = parse_datetime(published_raw) if published_raw else timezone.now()

        if published_at is None:
            published_at = timezone.now()

        description = item.get("description") or ""
        content = item.get("content") or ""
        image_url = item.get("urlToImage") or ""

        summary = description

        if not summary and content:
            summary = content[:250]

        article, created = Article.objects.get_or_create(
            original_url=original_url,
            defaults={
                "title": title[:255],
                "source": source,
                "category": category,
                "description": description,
                "summary": summary,
                "content": content,
                "image_url": image_url,
                "published_at": published_at,
            },
        )

        if created:
            return True, False, article

        updated = False

        if article.title != title[:255]:
            article.title = title[:255]
            updated = True

        if article.description != description:
            article.description = description
            updated = True

        if article.summary != summary:
            article.summary = summary
            updated = True

        if article.content != content:
            article.content = content
            updated = True

        if article.image_url != image_url:
            article.image_url = image_url
            updated = True

        if article.published_at != published_at:
            article.published_at = published_at
            updated = True

        if article.category != category:
            article.category = category
            updated = True

        if article.source != source:
            article.source = source
            updated = True

        if updated:
            article.save()

        return False, updated, article

    def create_breaking_alert(self, article):
        if article is None:
            return False

        existing_alert = BreakingNewsAlert.objects.filter(article=article).exists()

        if existing_alert:
            return False

        BreakingNewsAlert.objects.create(
            article=article,
            alert_title=article.title,
            message=article.description or article.get_quick_summary(),
            is_active=True,
        )

        return True

    def limit_active_breaking_alerts(self):
        active_alerts = BreakingNewsAlert.objects.filter(
            is_active=True
        ).order_by("-created_at")

        alerts_to_keep = active_alerts[:self.MAX_ACTIVE_BREAKING_ALERTS]
        keep_ids = [alert.id for alert in alerts_to_keep]

        BreakingNewsAlert.objects.filter(
            is_active=True
        ).exclude(
            id__in=keep_ids
        ).update(
            is_active=False
        )