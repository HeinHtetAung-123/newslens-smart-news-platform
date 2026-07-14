from django.core.management.base import BaseCommand
from django.utils import timezone

from news.models import Article, Category, NewsSource


class Command(BaseCommand):
    help = "Seed the database with sample categories, news sources, and articles."

    def handle(self, *args, **kwargs):
        categories = [
            ("Politics", "politics"),
            ("Technology", "technology"),
            ("Sports", "sports"),
            ("Business", "business"),
            ("Entertainment", "entertainment"),
            ("Local News", "local-news"),
        ]

        for name, slug in categories:
            Category.objects.get_or_create(name=name, slug=slug)

        sources = [
            ("CNA", "https://www.channelnewsasia.com"),
            ("BBC", "https://www.bbc.com"),
            ("Reuters", "https://www.reuters.com"),
            ("The Straits Times", "https://www.straitstimes.com"),
            ("TechCrunch", "https://techcrunch.com"),
            ("ESPN", "https://www.espn.com"),
        ]

        for name, website_url in sources:
            NewsSource.objects.get_or_create(name=name, website_url=website_url)

        sample_articles = [
            {
                "title": "Singapore expands AI adoption in public services",
                "source": "CNA",
                "category": "Technology",
                "description": "Singapore is increasing the use of AI tools to improve public service delivery.",
                "summary": "Singapore is expanding AI use in public services to improve speed, efficiency, and digital support.",
                "content": "This sample article discusses how AI tools may support public service transformation.",
                "original_url": "https://example.com/singapore-ai-public-services",
            },
            {
                "title": "Global markets respond to new business outlook",
                "source": "Reuters",
                "category": "Business",
                "description": "Markets reacted as investors reviewed new economic data and business forecasts.",
                "summary": "Investors are watching economic signals closely as global markets respond to changing business conditions.",
                "content": "This sample article covers market movement and investor reaction.",
                "original_url": "https://example.com/global-markets-business-outlook",
            },
            {
                "title": "Local transport improvements planned for city commuters",
                "source": "The Straits Times",
                "category": "Local News",
                "description": "New transport improvements are being planned to support smoother daily commuting.",
                "summary": "Local transport updates aim to improve convenience and reduce delays for commuters.",
                "content": "This sample article discusses local infrastructure and commuting improvements.",
                "original_url": "https://example.com/local-transport-improvements",
            },
            {
                "title": "Technology companies introduce new safety features",
                "source": "TechCrunch",
                "category": "Technology",
                "description": "Major technology companies are adding safety tools to improve user protection.",
                "summary": "Technology companies are focusing on safer digital experiences through new platform features.",
                "content": "This sample article discusses new technology safety features.",
                "original_url": "https://example.com/technology-safety-features",
            },
            {
                "title": "Football team prepares for important weekend match",
                "source": "ESPN",
                "category": "Sports",
                "description": "The team is preparing for a major match that may affect the season standings.",
                "summary": "A key weekend football match may influence the team’s position in the season.",
                "content": "This sample article covers team preparation and sports competition.",
                "original_url": "https://example.com/football-weekend-match",
            },
            {
                "title": "Film festival highlights rising independent directors",
                "source": "BBC",
                "category": "Entertainment",
                "description": "A new film festival is highlighting independent directors and emerging creative voices.",
                "summary": "The festival gives attention to independent filmmakers and new creative talent.",
                "content": "This sample article discusses entertainment, film, and creative industry trends.",
                "original_url": "https://example.com/film-festival-independent-directors",
            },
        ]

        for article_data in sample_articles:
            source = NewsSource.objects.get(name=article_data["source"])
            category = Category.objects.get(name=article_data["category"])

            Article.objects.get_or_create(
                title=article_data["title"],
                defaults={
                    "source": source,
                    "category": category,
                    "description": article_data["description"],
                    "summary": article_data["summary"],
                    "content": article_data["content"],
                    "original_url": article_data["original_url"],
                    "published_at": timezone.now(),
                },
            )

        self.stdout.write(self.style.SUCCESS("Sample data created successfully."))