# Practical 5: Iteration 1 Review and Reflection

## 1. Practical Objective

The objective of Practical 5 was to review the work completed in Iteration 1 of the NewsLens project. This practical focused on checking the quality of the code, reviewing completed and unfinished user stories, updating documentation, calculating actual velocity, and preparing evidence for GitHub Pages.

Iteration 1 delivered the foundation of the NewsLens system, including user accounts, a multi-source news feed, category browsing, article detail pages, and search functionality.

---

## 2. Iteration 1 User Stories Reviewed

| ID | User Story | Priority | Planned Estimate | Final Status |
|---|---|---:|---:|---|
| US01 | User Account Access | 10 | 3 days | Completed |
| US02 | Multi-Source News Feed | 10 | 4 days | Completed |
| US03 | News Categories | 10 | 2 days | Completed |
| US04 | Article Detail Page | 10 | 3 days | Completed |
| US05 | Search News | 20 | 3 days | Completed |

Total planned estimate: **15 days**

Total completed estimate: **15 days**

---

## 3. Completed User Stories

### US01: User Account Access

This story was completed by adding user registration, login, logout, and navigation links. Django’s built-in authentication features were used to keep the implementation simple and reliable.

Evidence:
- Register page created.
- Login page created.
- Logout function added.
- Navigation changes depending on authentication state.

### US02: Multi-Source News Feed

This story was completed by creating the main article feed. The system displays articles from multiple sources and includes source name, category, publication date, article title, description, and quick summary.

Evidence:
- `Article`, `Category`, and `NewsSource` models created.
- Sample article data added through seed command.
- Homepage displays multiple articles from different sources.

### US03: News Categories

This story was completed by creating category navigation and category-based article filtering.

Evidence:
- Category model includes name and slug.
- Category navigation appears on the website.
- Users can browse articles by category.

### US04: Article Detail Page

This story was completed by creating an article detail page that shows more information about a selected article.

Evidence:
- Article detail route created.
- Detail template created.
- Article metadata, description, preview content, quick summary, and original source link displayed.

### US05: Search News

This story was completed by adding a search form and search results page.

Evidence:
- Search form added to the base layout.
- Search view searches article title, description, summary, source, and category.
- Search results page displays matching articles.

---

## 4. Unfinished User Stories

No Iteration 1 user stories were left unfinished.

| User Story | Status | Notes |
|---|---|---|
| US01 | Completed | No major unfinished items |
| US02 | Completed | Real API fetching was treated as later enhancement |
| US03 | Completed | Category browsing works |
| US04 | Completed | Detail page works |
| US05 | Completed | Search works |

Although all Iteration 1 stories were completed, some improvements were intentionally left for later iterations. For example, saving articles, breaking news alerts, recommendations, source comparison, and bias/balance insights were not part of Iteration 1 and were scheduled for Iteration 2 or Iteration 3.

---

## 5. Actual Velocity Calculation

Velocity measures how much estimated work was actually completed during the iteration.

### Planned Work

| User Story | Estimate |
|---|---:|
| US01 | 3 days |
| US02 | 4 days |
| US03 | 2 days |
| US04 | 3 days |
| US05 | 3 days |

Total planned work: **15 days**

### Completed Work

| User Story | Estimate Completed |
|---|---:|
| US01 | 3 days |
| US02 | 4 days |
| US03 | 2 days |
| US04 | 3 days |
| US05 | 3 days |

Total completed work: **15 days**

### Velocity Result

```text
Actual Velocity = Completed Estimate / Planned Estimate
Actual Velocity = 15 / 15
Actual Velocity = 100%