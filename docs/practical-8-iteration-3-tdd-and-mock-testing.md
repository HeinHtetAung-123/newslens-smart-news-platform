# Practical 8: Iteration 3 TDD Practice and Mock Object Testing

## 1. Practical Objective

The objective of Practical 8 was to apply Test-Driven Development practice to Iteration 3 of the NewsLens project. This practical used the user stories and interface designs as test specifications, reviewed Iteration 2 results, updated the backlog for Iteration 3, monitored the project board, updated GitHub Pages for completed stories, and researched mock objects for testing.

Iteration 3 focused on advanced NewsLens features:

- Same-story source comparison
- Bias and balance insights
- User preferences and recommendations
- Admin/content management

---

## 2. Iteration 2 Reflection

Iteration 2 focused on improving reader usefulness through quick summaries, saved articles, and breaking news alerts.

| ID | User Story | Estimate | Status |
|---|---|---:|---|
| US06 | Quick Article Summary | 4 days | Completed |
| US07 | Save Articles | 3 days | Completed |
| US08 | Breaking News Alerts | 3 days | Completed |

Total planned work: **10 days**

Total completed work: **10 days**

Actual Iteration 2 velocity: **10 estimated days**

Iteration 2 was successful because all planned stories were completed. The quick summary feature improved article scanning, saved articles added personal user functionality, and breaking news alerts made the homepage more useful.

The main challenge was that several features affected the same templates, especially the homepage and article detail page. This required extra manual checking after each change.

---

## 3. Iteration 2 Burndown Chart Data

| Day | Planned Work Remaining | Actual Work Remaining |
|---:|---:|---:|
| 0 | 10 | 10 |
| 1 | 9 | 10 |
| 2 | 8 | 9 |
| 3 | 7 | 8 |
| 4 | 6 | 6 |
| 5 | 5 | 5 |
| 6 | 4 | 5 |
| 7 | 3 | 3 |
| 8 | 2 | 2 |
| 9 | 1 | 1 |
| 10 | 0 | 0 |

## Mock Object Testing Evidence

Mock object testing was used to test the News API fetch command without calling the real News API. This was important because the real API depends on an API key, internet access, live data, and rate limits. Those factors would make automated tests unreliable.

The mock test replaced `requests.get()` with a fake response. The fake response returned controlled article data, allowing the test to check that NewsLens correctly saved an article into the database.

Two mock tests were added:

| Test | Purpose | Expected Result |
|---|---|---|
| `test_fetch_news_creates_article_from_mock_api_response` | Checks that mocked API article data is saved | Article is created |
| `test_fetch_news_does_not_create_article_when_api_fails` | Checks that failed API response does not create an article | No article is created |

This supports the TDD idea that tests should run from a known state and should be repeatable. The mock object made the test predictable because it removed dependency on the live News API.

## 4. Iteration 2 Burndown Graph

```mermaid
xychart-beta
    title "Iteration 2 Burndown Chart"
    x-axis "Iteration Day" [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y-axis "Estimated Days Remaining" 0 --> 10
    line "Planned Work Remaining" [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    line "Actual Work Remaining" [10, 10, 9, 8, 6, 5, 5, 3, 2, 1, 0]
