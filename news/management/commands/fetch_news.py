import requests

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from news.models import Article, Category, NewsSource


class Command(BaseCommand):
    help = "Fetch real news articles from NewsAPI and store them in the database."

    NEWS_API_URL = "https://newsapi.org/v2/top-headlines"

    CATEGORY_MAP = {
        "business": "Business",
        "entertainment": "Entertainment",
        "sports": "Sports",
        "technology": "Technology",
    }

    def handle(self, *args, **options):
        api_key = settings.NEWS_API_KEY

        if not api_key:
            self.stderr.write(
                self.style.ERROR("NEWS_API_KEY is missing. Add it to your .env file.")
            )
            return

        total_created = 0

        for api_category, local_category_name in self.CATEGORY_MAP.items():
            created_count = self.fetch_category(api_key, api_category, local_category_name)
            total_created += created_count

        self.stdout.write(
            self.style.SUCCESS(f"News fetch completed. {total_created} new articles added.")
        )

    def fetch_category(self, api_key, api_category, local_category_name):
        category, _ = Category.objects.get_or_create(
            name=local_category_name,
            defaults={"slug": local_category_name.lower().replace(" ", "-")},
        )

        params = {
            "apiKey": api_key,
            "country": "us",
            "category": api_category,
            "pageSize": 20,
        }

        response = requests.get(self.NEWS_API_URL, params=params, timeout=15)

        if response.status_code != 200:
            self.stderr.write(
                self.style.ERROR(
                    f"Failed to fetch {api_category} news. Status: {response.status_code}"
                )
            )
            return 0

        data = response.json()
        articles = data.get("articles", [])

        created_count = 0

        for item in articles:
            title = item.get("title")
            original_url = item.get("url")
            source_name = item.get("source", {}).get("name") or "Unknown Source"

            if not title or not original_url:
                continue

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
                    "image_url": item.get("urlToImage") or "",
                    "published_at": published_at,
                },
            )

            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"{local_category_name}: {created_count} new articles added."
            )
        )

        return created_count