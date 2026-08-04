# US08: Breaking News Alerts

## User Story
As a reader, I want to see breaking news alerts so that I can quickly notice urgent or important stories.

## Priority
30

## Estimate
3 days

## Completed Work
- Created BreakingNewsAlert model.
- Added alert management through Django admin.
- Displayed active alerts on the homepage.
- Improved alert section layout.
- Tested active and inactive alert visibility.

## Status
Completed

## Testing Notes
Active alerts were checked on the homepage. Inactive alerts were tested to confirm that they do not appear to users.

## Mock Object Testing Evidence

Mock object testing was used to test the News API fetch command without calling the real News API. This was important because the real API depends on an API key, internet access, live data, and rate limits. Those factors would make automated tests unreliable.

The mock test replaced `requests.get()` with a fake response. The fake response returned controlled article data, allowing the test to check that NewsLens correctly saved an article into the database.

Two mock tests were added:

| Test | Purpose | Expected Result |
|---|---|---|
| `test_fetch_news_creates_article_from_mock_api_response` | Checks that mocked API article data is saved | Article is created |
| `test_fetch_news_does_not_create_article_when_api_fails` | Checks that failed API response does not create an article | No article is created |

This supports the TDD idea that tests should run from a known state and should be repeatable. The mock object made the test predictable because it removed dependency on the live News API.