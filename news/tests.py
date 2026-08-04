from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from unittest.mock import Mock, patch
from django.core.management import call_command
from django.test import TestCase, override_settings

from .models import Article, BreakingNewsAlert, Category, NewsSource, SavedArticle


class NewsLensTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.technology = Category.objects.create(
            name="Technology",
            slug="technology"
        )

        self.sports = Category.objects.create(
            name="Sports",
            slug="sports"
        )

        self.source_one = NewsSource.objects.create(
            name="Tech Daily",
            website_url="https://example.com/tech"
        )

        self.source_two = NewsSource.objects.create(
            name="Sports World",
            website_url="https://example.com/sports"
        )

        self.article = Article.objects.create(
            title="AI Tools Improve Software Testing",
            source=self.source_one,
            category=self.technology,
            description="Developers are using AI tools to improve software testing and productivity.",
            summary="AI tools are improving software testing.",
            content="Full article content about AI tools and software testing.",
            original_url="https://example.com/article-1",
            published_at=timezone.now()
        )

        self.related_article = Article.objects.create(
            title="New Testing Platform Announced",
            source=self.source_one,
            category=self.technology,
            description="A new testing platform has been announced for software teams.",
            summary="A new platform supports better software testing.",
            content="Full related article content.",
            original_url="https://example.com/article-2",
            published_at=timezone.now()
        )

        self.other_article = Article.objects.create(
            title="Local Team Wins Final",
            source=self.source_two,
            category=self.sports,
            description="A local sports team won the final match.",
            summary="A local team won the final.",
            content="Full sports article content.",
            original_url="https://example.com/article-3",
            published_at=timezone.now()
        )

    # US02: Multi-Source News Feed

    def test_homepage_loads_successfully(self):
        response = self.client.get(reverse("news:home"))
        self.assertEqual(response.status_code, 200)

    def test_homepage_displays_article_title(self):
        response = self.client.get(reverse("news:home"))
        self.assertContains(response, "AI Tools Improve Software Testing")

    def test_homepage_displays_source_and_category(self):
        response = self.client.get(reverse("news:home"))
        self.assertContains(response, "Tech Daily")
        self.assertContains(response, "Technology")

    # US03: News Categories

    def test_category_page_loads_successfully(self):
        response = self.client.get(
            reverse("news:category_articles", args=[self.technology.slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_category_page_shows_matching_articles(self):
        response = self.client.get(
            reverse("news:category_articles", args=[self.technology.slug])
        )
        self.assertContains(response, "AI Tools Improve Software Testing")
        self.assertContains(response, "New Testing Platform Announced")

    def test_category_page_excludes_other_category_articles(self):
        response = self.client.get(
            reverse("news:category_articles", args=[self.technology.slug])
        )
        self.assertNotContains(response, "Local Team Wins Final")

    # US05: Search News

    def test_search_by_article_title(self):
        response = self.client.get(reverse("news:search_articles"), {"q": "AI Tools"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AI Tools Improve Software Testing")

    def test_search_by_source_name(self):
        response = self.client.get(reverse("news:search_articles"), {"q": "Tech Daily"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AI Tools Improve Software Testing")

    def test_search_with_no_matching_result(self):
        response = self.client.get(reverse("news:search_articles"), {"q": "NoMatchTerm"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "AI Tools Improve Software Testing")

    # US06: Quick Article Summary

    def test_quick_summary_uses_existing_summary(self):
        self.assertEqual(
            self.article.get_quick_summary(),
            "AI tools are improving software testing."
        )

    def test_quick_summary_uses_description_when_summary_missing(self):
        article = Article.objects.create(
            title="Description Fallback Article",
            source=self.source_one,
            category=self.technology,
            description="This description should be used when summary is missing.",
            summary="",
            content="",
            original_url="https://example.com/article-4",
            published_at=timezone.now()
        )

        self.assertEqual(
            article.get_quick_summary(),
            "This description should be used when summary is missing."
        )

    def test_quick_summary_returns_default_message_when_text_missing(self):
        article = Article.objects.create(
            title="Empty Article",
            source=self.source_one,
            category=self.technology,
            description="",
            summary="",
            content="",
            original_url="https://example.com/article-5",
            published_at=timezone.now()
        )

        self.assertEqual(
            article.get_quick_summary(),
            "No quick summary is available for this article yet."
        )

    # US07: Save Articles

    def test_anonymous_user_redirected_when_saving_article(self):
        response = self.client.get(
            reverse("news:save_article", args=[self.article.id])
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_logged_in_user_can_save_article(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.get(
            reverse("news:save_article", args=[self.article.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            SavedArticle.objects.filter(
                user=self.user,
                article=self.article
            ).exists()
        )

    def test_logged_in_user_can_remove_saved_article(self):
        self.client.login(username="testuser", password="testpass123")

        SavedArticle.objects.create(
            user=self.user,
            article=self.article
        )

        response = self.client.get(
            reverse("news:remove_saved_article", args=[self.article.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            SavedArticle.objects.filter(
                user=self.user,
                article=self.article
            ).exists()
        )

    # US08: Breaking News Alerts

    def test_homepage_displays_active_breaking_alert(self):
        BreakingNewsAlert.objects.create(
            article=self.article,
            alert_title="Breaking: AI Testing News",
            message="Important update about AI testing.",
            is_active=True
        )

        response = self.client.get(reverse("news:home"))
        self.assertContains(response, "Breaking: AI Testing News")

    def test_homepage_hides_inactive_breaking_alert(self):
        BreakingNewsAlert.objects.create(
            article=self.article,
            alert_title="Hidden Breaking Alert",
            message="This should not be shown.",
            is_active=False
        )

        response = self.client.get(reverse("news:home"))
        self.assertNotContains(response, "Hidden Breaking Alert")

    def test_breaking_alert_article_title_is_available(self):
        BreakingNewsAlert.objects.create(
            article=self.article,
            alert_title="Breaking: AI Testing News",
            message="Important update about AI testing.",
            is_active=True
        )

        response = self.client.get(reverse("news:home"))
        self.assertContains(response, self.article.title)

    # US09: Same-Story Comparison

    def test_compare_sources_page_loads_successfully(self):
        response = self.client.get(
            reverse("news:compare_sources", args=[self.article.id])
        )
        self.assertEqual(response.status_code, 200)

    def test_compare_sources_page_displays_main_article(self):
        response = self.client.get(
            reverse("news:compare_sources", args=[self.article.id])
        )
        self.assertContains(response, "AI Tools Improve Software Testing")

    def test_compare_sources_page_displays_related_article(self):
        response = self.client.get(
            reverse("news:compare_sources", args=[self.article.id])
        )
        self.assertContains(response, "New Testing Platform Announced")

@override_settings(NEWS_API_KEY="fake-test-api-key")
class FetchNewsMockTest(TestCase):
    @patch("news.management.commands.fetch_news.requests.get")
    def test_fetch_news_creates_article_from_mock_api_response(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "articles": [
                {
                    "title": "Mock API Test Article",
                    "description": "This article was created from a mocked API response.",
                    "content": "Mock content for testing.",
                    "url": "https://example.com/mock-api-test",
                    "urlToImage": "",
                    "publishedAt": "2026-08-04T10:00:00Z",
                    "source": {
                        "name": "Mock News Source"
                    }
                }
            ]
        }

        mock_get.return_value = mock_response

        call_command("fetch_news")

        self.assertTrue(
            Article.objects.filter(
                title="Mock API Test Article"
            ).exists()
        )

    @patch("news.management.commands.fetch_news.requests.get")
    def test_fetch_news_does_not_create_article_when_api_fails(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_get.return_value = mock_response

        call_command("fetch_news")

        self.assertFalse(
            Article.objects.filter(
                title="Mock API Test Article"
            ).exists()
        )