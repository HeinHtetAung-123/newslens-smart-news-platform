# NewsLens Delivered Solution

## 1. Solution Overview

NewsLens is a smart news aggregation and bias insight platform developed as an agile software engineering project. The system allows users to read news from multiple sources, browse articles by category, search for news, save articles, view breaking news alerts, compare related coverage, and review simple bias/balance insights.

The delivered solution matches the planned project goal: to help readers access news more easily and think more critically about how different sources report similar stories.

---

## 2. Problem Being Solved

Many readers consume news quickly from one source without checking how other sources report the same topic. This can make it harder to notice different perspectives, wording choices, or missing context.

NewsLens addresses this problem by providing:

- A multi-source news feed
- Quick article summaries
- Category browsing
- Search functionality
- Saved articles
- Breaking news alerts
- Same-story source comparison
- Bias and balance insight guidance
- User preference-based recommendations

---

## 3. Main Features Delivered

| Feature | Description | Related User Story |
|---|---|---|
| User account access | Users can register, log in, and log out | US01 |
| Multi-source news feed | Homepage displays news articles from different sources | US02 |
| News categories | Users can browse articles by category | US03 |
| Article detail page | Users can read more information about an article | US04 |
| Search news | Users can search for articles by keyword | US05 |
| Quick article summary | Articles display short summaries | US06 |
| Save articles | Logged-in users can save and remove articles | US07 |
| Breaking news alerts | Important active alerts are shown on the homepage | US08 |
| Same-story comparison | Users can compare related articles from different sources | US09 |
| Bias and balance insights | Article detail page gives wording and balance guidance | US10 |
| User preferences | Users can choose preferred categories for recommendations | US11 |
| Admin management | Staff users can manage and review platform data | US12 |

---

## 4. Delivered Iterations

NewsLens was developed across three iterations. Each iteration delivered working features that built on the previous iteration.

### Iteration 1: Core Reading Features

Iteration 1 focused on the foundation of the website.

| User Story | Feature Delivered | Status |
|---|---|---|
| US01 | User Account Access | Completed |
| US02 | Multi-Source News Feed | Completed |
| US03 | News Categories | Completed |
| US04 | Article Detail Page | Completed |
| US05 | Search News | Completed |

Iteration 1 delivered the core reading experience. Users could open the homepage, browse articles, use categories, open article detail pages, and search for news.

Actual velocity: **15 estimated days**

---

### Iteration 2: Reader Usefulness Features

Iteration 2 improved the usefulness of the platform.

| User Story | Feature Delivered | Status |
|---|---|---|
| US06 | Quick Article Summary | Completed |
| US07 | Save Articles | Completed |
| US08 | Breaking News Alerts | Completed |

Iteration 2 delivered quick summaries, saved article functionality, and breaking news alerts. These features made NewsLens more useful for regular readers.

Actual velocity: **10 estimated days**

---

### Iteration 3: Advanced Insight Features

Iteration 3 focused on advanced functionality and final project improvements.

| User Story | Feature Delivered | Status |
|---|---|---|
| US09 | Same-Story Comparison | Completed |
| US10 | Bias and Balance Insights | Completed |
| US11 | User Preferences | Completed |
| US12 | Admin Management | Completed |

Iteration 3 delivered source comparison, bias and balance insight, user preferences, recommendations, and admin dashboard support.

Planned work: **17 estimated days**

---

## 5. Homepage

The homepage is the main entry point of NewsLens. It displays latest articles, breaking news alerts, category sections, and recommended articles for logged-in users.

Main homepage elements:

- Header and navigation
- Search bar
- Breaking news alert section
- Recommended articles section
- Latest articles
- Category article sections
- Article cards with title, source, category, date, image/placeholder, and quick summary

The homepage was improved during development to make the layout more professional and readable.

---

## 6. Article Detail Page

The article detail page gives users more information about a selected article.

The page includes:

- Article title
- Source
- Category
- Published date
- Article image or placeholder
- Quick summary
- Bias and balance insight
- Description
- Article content preview
- Original source link
- Save/remove article button
- Compare Sources button

This page supports both reading and critical thinking because users can read the article summary, check insight guidance, save the article, or compare it with related coverage.

---

## 7. Search and Category Browsing

NewsLens includes search and category browsing so users can find relevant articles quickly.

Search supports matching by:

- Article title
- Source
- Category
- Description
- Summary
- Content

Category browsing allows users to open one category and view only articles from that category. This makes the system easier to navigate.

---

## 8. Saved Articles

The saved articles feature allows logged-in users to save articles and return to them later.

This feature includes:

- Save article button
- Remove saved article button
- Saved articles page
- Authentication protection so only logged-in users can save articles

This makes NewsLens more personalised and useful for returning users.

---

## 9. Breaking News Alerts

Breaking news alerts highlight important articles on the homepage.

This feature includes:

- BreakingNewsAlert model
- Active/inactive alert status
- Homepage alert section
- Django admin management
- Improved visual layout

Only active alerts are displayed to users. This allows important news to be highlighted without hard-coding alerts into the homepage.

---

## 10. Source Comparison

The Compare Sources page allows users to compare related coverage.

This page includes:

- Selected main article
- Related source cards
- Visual source map
- Comparison insight section
- Links to related article detail pages

This feature supports the main purpose of NewsLens by helping users check more than one source before forming an opinion.

---

## 11. Bias and Balance Insights

The bias and balance insight feature provides simple guidance about article wording.

The insight panel includes:

- Source context
- Category context
- Summary length
- Wording style
- Strong word count
- Balance reminder

This feature does not claim to fully detect bias. Instead, it encourages readers to compare sources and notice wording style.

---

## 12. User Preferences and Recommendations

Logged-in users can select preferred categories. NewsLens then uses those selected categories to show recommended articles on the homepage.

This feature includes:

- UserPreference model
- Preferred category selection
- Preferences page
- Recommended article section on homepage

This makes the platform more personalised for users.

---

## 13. Admin Management

NewsLens includes admin management through Django admin and a custom admin dashboard.

Admin users can manage:

- Articles
- Categories
- News sources
- Saved articles
- Breaking news alerts
- User preferences

The custom admin dashboard displays useful system statistics such as article count, category count, source count, saved article count, and alert count.

---

## 14. Database Choice

The project used Django models with a relational database structure. During development, SQLite was suitable because it was simple to set up and supported fast local development. The design can be moved to MySQL for a more production-ready deployment because the project uses Django ORM models instead of database-specific SQL.

This database choice supported fast iteration during coursework while keeping the system compatible with a modern relational database approach.

---

## 15. UI Design Choices

The UI was designed to be clean, readable, and practical.

Important UI choices included:

| UI Choice | Reason |
|---|---|
| Card-based article layout | Makes articles easy to scan |
| Category navigation | Helps users browse by topic |
| Quick summary blocks | Helps readers understand articles faster |
| Breaking news section | Highlights urgent content |
| Image placeholder | Keeps the layout consistent when images are missing |
| Compare Sources visual map | Makes related sources easier to understand |
| Bias insight panel | Encourages critical reading |
| Responsive CSS | Improves readability on different screen sizes |

The UI was improved throughout the iterations based on testing and feedback.

---

## 16. Client Feedback and Improvements

After each iteration, the delivered solution was reviewed and improved.

| Iteration | Feedback / Issue Found | Improvement Made |
|---|---|---|
| Iteration 1 | Homepage needed clearer article presentation | Improved article card layout and styling |
| Iteration 1 | Article images affected layout | Added image sizing and placeholder design |
| Iteration 2 | Breaking news section looked too plain | Improved breaking news layout |
| Iteration 2 | More realistic article data was needed | Added News API fetching support |
| Iteration 3 | Compare Sources visual map needed clearer connections | Updated CSS connector lines |
| Iteration 3 | Comparison section repeated information | Replaced it with Comparison Insights |
| Iteration 3 | Card buttons were not aligned | Updated CSS flex layout |

These improvements show that the solution was not only coded once, but reviewed and refined after feedback.

---

## 17. External API Integration

NewsLens includes an external News API fetching feature. This supports more realistic article data than manually added seed data.

The API feature:

- Fetches articles from external news sources
- Saves article information into the database
- Stores title, source, category, description, content, image URL, original URL, and published date
- Handles failed API responses safely
- Uses `.env` for the API key instead of hard-coding it

Mock object tests were also added so the API feature could be tested without calling the real external API.

---

## 18. Testing Evidence

The delivered solution was supported by automated testing and system testing.

Final automated test evidence:

```text
Ran 23 tests in 7.379s

OK
Destroying test database for alias 'default'...
```

Testing covered:

- Homepage loading
- Article feed
- Category browsing
- Search
- Quick summaries
- Saved articles
- Breaking news alerts
- Compare Sources
- Mock News API response

This shows that important functionality was tested and passed successfully.

---

## 19. Deployment Choice

The project was designed as a Django web application that can be deployed to a Python-compatible hosting platform such as Render, Railway, or PythonAnywhere.

The deployment design includes:

- Django application structure
- `requirements.txt`
- Environment variable support through `.env`
- Static files
- Database-backed content
- External API key separated from source code

This supports a safer and more realistic deployment process.

---

## 20. Final Delivered Solution Summary

NewsLens successfully delivered the planned IT solution across three agile iterations. The system includes core reading features, user account features, article summaries, saved articles, breaking alerts, source comparison, bias insight, preferences, recommendations, admin management, testing, and external API support.

The solution delivered what was planned in the backlog and was improved through feedback, testing, and iteration. Overall, NewsLens meets the project goal of providing a smart news platform that helps users read, organise, and compare news more critically.