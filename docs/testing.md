# NewsLens Testing Documentation

## 1. Testing Overview

Testing was an important part of the NewsLens project because the system includes user accounts, article browsing, search, saved articles, breaking alerts, comparison features, bias insight, preferences, admin management, and an external News API feature.

The testing approach included:

- Test-driven development planning
- Automated Django tests
- Acceptance testing
- System testing
- Mock object testing
- Manual interface testing
- Testing with realistic article data

The goal was to make sure the delivered implementation matched the planned user stories and worked correctly across all major components.

---

## 2. Test-Driven Development Approach

NewsLens used Test-Driven Development practice during the later practicals. The TDD approach followed this cycle:

```text
Write a test → Run the test → See it fail → Write/fix code → Run the test again → Refactor
```

This helped make the project more reliable because features were checked through repeatable automated tests.

TDD was especially useful for:

- Quick article summaries
- Saved articles
- Breaking alerts
- Source comparison
- Mock News API response testing

---

## 3. Automated Testing Tool

Automated tests were written using Django’s built-in testing framework.

The main test file was:

```text
news/tests.py
```

The tests were run using:

```bash
python manage.py test news
```

The final automated test result was:

```text
Ran 23 tests in 7.379s

OK
Destroying test database for alias 'default'...
```

This shows that the final automated test suite passed successfully.

---

## 4. Automated Test Coverage

The automated test suite covered important NewsLens features.

| Area Tested | What Was Tested |
|---|---|
| Homepage | Homepage loads and displays articles |
| Multi-source feed | Article title, source, and category appear |
| Categories | Category page loads and filters articles |
| Search | Search works by article title and source name |
| Quick summaries | Summary fallback behaviour works |
| Saved articles | Logged-in users can save and remove articles |
| Authentication | Anonymous users are redirected when saving |
| Breaking alerts | Active alerts appear and inactive alerts are hidden |
| Compare Sources | Compare page loads and shows related articles |
| Mock API testing | Fake API response creates article without real API call |

---

## 5. User Stories Tested

| User Story | Feature | Test Evidence |
|---|---|---|
| US02 | Multi-Source News Feed | Homepage tests |
| US03 | News Categories | Category page tests |
| US05 | Search News | Search result tests |
| US06 | Quick Article Summary | Summary helper tests |
| US07 | Save Articles | Save/remove article tests |
| US08 | Breaking News Alerts | Active/inactive alert tests |
| US09 | Same-Story Comparison | Compare Sources tests |
| API Feature | News API Fetching | Mock object tests |

Although not every user story required the same number of automated tests, the final test suite covered the main user-facing behaviours and the most important database actions.

---

## 6. Test Data Used

The automated tests used controlled test data created inside the test setup.

Example test data included:

| Test Data | Purpose |
|---|---|
| Test user | Used to test login and saved articles |
| Technology category | Used to test category filtering and comparison |
| Sports category | Used to test exclusion of unrelated categories |
| Tech Daily source | Used to test article source display and search |
| Sports World source | Used to test different source/category data |
| AI article | Used as the main test article |
| Related technology article | Used for Compare Sources tests |
| Sports article | Used to confirm unrelated articles are excluded |
| Active breaking alert | Used to confirm alerts display |
| Inactive breaking alert | Used to confirm inactive alerts are hidden |
| Mock API article | Used to test external API behaviour safely |

Using controlled test data made the tests predictable and repeatable.

---

## 7. Example Automated Tests

### Homepage Test

```python
def test_homepage_loads_successfully(self):
    response = self.client.get(reverse("news:home"))
    self.assertEqual(response.status_code, 200)
```

This test checks that the homepage loads successfully.

### Category Filtering Test

```python
def test_category_page_excludes_other_category_articles(self):
    response = self.client.get(
        reverse("news:category_articles", args=[self.technology.slug])
    )
    self.assertNotContains(response, "Local Team Wins Final")
```

This test confirms that a category page does not display articles from another category.

### Save Article Test

```python
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
```

This test confirms that a logged-in user can save an article.

---

## 8. Mock Object Testing

Mock object testing was used to test the News API feature without depending on the real external API.

This was important because the real News API:

- Requires an API key
- Requires internet access
- May return changing data
- May fail because of rate limits
- May return different results each time

The mock test replaced the real API call with a fake response.

### Mock API Test Example

```python
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
```

This test proves that the fetch command can create an article from API-style data without calling the real News API.

---

## 9. Mock Test Cases

| Test | Purpose | Expected Result |
|---|---|---|
| `test_fetch_news_creates_article_from_mock_api_response` | Checks article creation from fake API data | Article is saved |
| `test_fetch_news_does_not_create_article_when_api_fails` | Checks failed API response handling | No article is created |

The mock tests made the API feature safer and easier to test.

---

## 10. Acceptance Testing

Acceptance testing checked whether each delivered feature matched the original user story.

| User Story | Acceptance Test | Result |
|---|---|---|
| US01 User Account Access | User can register, log in, and log out | Pass |
| US02 Multi-Source News Feed | Homepage displays article feed | Pass |
| US03 News Categories | User can browse by category | Pass |
| US04 Article Detail Page | Article detail page shows article information | Pass |
| US05 Search News | Search returns matching articles | Pass |
| US06 Quick Article Summary | Articles show short summaries | Pass |
| US07 Save Articles | Logged-in user can save/remove articles | Pass |
| US08 Breaking News Alerts | Active alerts appear on homepage | Pass |
| US09 Same-Story Comparison | Compare Sources page shows related articles | Pass |
| US10 Bias and Balance Insights | Bias/balance panel appears on article detail page | Pass |
| US11 User Preferences | User preferences affect recommendations | Pass |
| US12 Admin Management | Staff dashboard and Django admin support management | Pass |

---

## 11. System Testing

System testing checked NewsLens as a complete application from the user’s point of view.

| Test ID | Feature | Expected Result | Result |
|---|---|---|---|
| ST01 | Homepage | Latest articles, categories, and alerts display | Pass |
| ST02 | Category Browsing | Only selected category articles appear | Pass |
| ST03 | Search | Matching articles appear | Pass |
| ST04 | Article Detail | Article details and original link appear | Pass |
| ST05 | Quick Summary | Summary appears on cards/detail page | Pass |
| ST06 | Register/Login/Logout | Authentication works correctly | Pass |
| ST07 | Save Article | Article is saved for logged-in user | Pass |
| ST08 | Remove Saved Article | Article is removed from saved list | Pass |
| ST09 | Breaking Alerts | Only active alerts appear | Pass |
| ST10 | Compare Sources | Main and related articles appear | Pass |
| ST11 | Bias Insight | Bias/balance panel appears | Pass |
| ST12 | Preferences | Recommended articles update | Pass |
| ST13 | Admin Dashboard | Staff user can access dashboard | Pass |
| ST14 | Admin Restriction | Normal user cannot access dashboard | Pass |
| ST15 | Missing Images | Placeholder image appears | Pass |
| ST16 | Responsive Layout | Layout remains readable | Pass |
| ST17 | Mock API Fetch | Fake API response creates article | Pass |

---

## 12. Manual Interface Testing

Manual testing was used to check areas that are difficult to confirm through automated tests alone.

Manual checks included:

- Homepage layout readability
- Article card spacing
- Image placeholder display
- Breaking news alert styling
- Compare Sources visual source map
- Button alignment
- Navigation links
- Mobile/responsive layout
- Admin dashboard visibility
- Preferences form usability

Manual testing helped improve the user interface quality across the project.

---

## 13. Bugs Found and Fixed During Testing

| Bug | Fix |
|---|---|
| Article images were too large | CSS image sizing was improved |
| Missing images created empty layout | Placeholder image design was added |
| Breaking news section looked plain | Alert design was improved |
| Compare Sources connectors were unclear | CSS connector lines were updated |
| Comparison Snapshot repeated information | Replaced with Comparison Insights |
| Recommended card buttons were not aligned | Flexbox card layout was added |
| Related source card buttons were not aligned | Card height and action layout were fixed |
| News API returned 401 when key was missing | `.env` API key handling and safe response handling were used |
| Tests failed because `published_at` was missing | `published_at=timezone.now()` was added |
| Django initially found zero tests | `news/tests.py` was created correctly |

---

## 14. Testing Data Sets

The project used both controlled test data and realistic news data.

| Data Set | Purpose |
|---|---|
| Controlled automated test data | Used for repeatable Django tests |
| Mock API response data | Used to test API behaviour without real API calls |
| Realistic article data from News API | Used to make the application content more realistic |
| Admin-created alerts | Used to test breaking news display |
| User-created saved articles | Used to test personal article saving |
| User preference category selections | Used to test recommendations |

This combination made testing stronger because the system was checked using both predictable and realistic data.

---

## 15. How Testing Supports the Plan

The delivered implementation matched the planned backlog because each major planned user story was tested through automated tests, acceptance checks, system tests, or manual interface testing.

Testing supported the project plan by confirming that:

- Iteration 1 delivered the core reading features
- Iteration 2 delivered summaries, saving, and alerts
- Iteration 3 delivered comparison, bias insight, preferences, and admin management
- The external API feature could be tested safely with mocks
- The final system passed 23 automated tests

---

## 16. Testing Summary

The NewsLens testing approach covered automated testing, TDD practice, acceptance testing, system testing, manual UI testing, mock object testing, and realistic data testing.

The strongest testing evidence was the final automated test result:

```text
Ran 23 tests in 7.379s

OK
Destroying test database for alias 'default'...
```

This shows that the main tested components passed successfully. Combined with acceptance and system testing, this provides strong evidence that the delivered implementation matched the project requirements and planning.