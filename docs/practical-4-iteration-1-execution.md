# Practical 4: Iteration 1 Execution and Tracking

## 1. Practical Objective

The objective of Practical 4 was to move Iteration 1 from high-level user stories into actual development work. In previous practicals, the NewsLens backlog was created and Iteration 1 was planned. In this practical, the Iteration 1 user stories were split into smaller development tasks, task estimates were checked against the original story estimates, GitHub was used to track progress, and basic system design diagrams were prepared.

This approach follows the idea that user stories describe the system from the user’s point of view, while tasks describe the development work needed to implement those stories. Breaking stories into tasks gives more accurate planning detail and helps the developer monitor progress during the iteration.

---

## 2. Iteration 1 User Stories

The following user stories were selected for Iteration 1.

| ID | User Story | Priority | Original Estimate |
|---|---|---:|---:|
| US01 | User Account Access | 10 | 3 days |
| US02 | Multi-Source News Feed | 10 | 4 days |
| US03 | News Categories | 10 | 2 days |
| US04 | Article Detail Page | 10 | 3 days |
| US05 | Search News | 20 | 3 days |

Total original estimate: **15 days**

---

## 3. Task Breakdown and Estimates

### US01: User Account Access

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T01 | Configure Django authentication routes | 0.5 day | Done |
| T02 | Create registration view using Django UserCreationForm | 0.5 day | Done |
| T03 | Create login and registration templates | 0.75 day | Done |
| T04 | Add login/logout/register navigation to base layout | 0.5 day | Done |
| T05 | Test registration, login, logout, and navigation manually | 0.75 day | Done |

Task estimate total: **3 days**

### US02: Multi-Source News Feed

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T06 | Create Category, NewsSource, and Article models | 1 day | Done |
| T07 | Register models in Django admin | 0.5 day | Done |
| T08 | Create seed data command for sample articles | 1 day | Done |
| T09 | Create homepage article list view | 0.75 day | Done |
| T10 | Build homepage template and article cards | 0.75 day | Done |

Task estimate total: **4 days**

### US03: News Categories

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T11 | Add category slug field and category navigation | 0.5 day | Done |
| T12 | Create category filtering view | 0.75 day | Done |
| T13 | Add category links to base template | 0.5 day | Done |
| T14 | Test category browsing using seeded data | 0.25 day | Done |

Task estimate total: **2 days**

### US04: Article Detail Page

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T15 | Create article detail view | 0.75 day | Done |
| T16 | Create article detail template | 1 day | Done |
| T17 | Display article metadata, description, summary, and original source link | 0.75 day | Done |
| T18 | Test article detail navigation from homepage and category pages | 0.5 day | Done |

Task estimate total: **3 days**

### US05: Search News

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T19 | Add search form to base layout | 0.5 day | Done |
| T20 | Create search view using title, description, summary, source, and category matching | 1 day | Done |
| T21 | Create search results template | 0.75 day | Done |
| T22 | Test search with matching and non-matching terms | 0.75 day | Done |

Task estimate total: **3 days**

---

## 4. Estimate Check

| User Story | Original Estimate | Task Estimate | Result |
|---|---:|---:|---|
| US01 | 3 days | 3 days | Estimate confirmed |
| US02 | 4 days | 4 days | Estimate confirmed |
| US03 | 2 days | 2 days | Estimate confirmed |
| US04 | 3 days | 3 days | Estimate confirmed |
| US05 | 3 days | 3 days | Estimate confirmed |

The total task estimate remained **15 days**, matching the original Iteration 1 estimate. This means Iteration 1 was still realistic after breaking the stories into smaller tasks.

---

## 5. GitHub Issue and Board Tracking

Each Iteration 1 user story was represented as a GitHub issue. The project board used the following workflow:

- Todo
- In Progress
- Done

The labels used were:

- `user-story`
- `iteration-1`
- `todo`
- `in-progress`
- `done`
- `priority-10`
- `priority-20`

As the project was completed by one developer, each issue was assigned to the sole developer. This kept the tracking realistic for a solo project while still showing an agile workflow.

Example issue structure:

```text
Title: US02 - Multi-Source News Feed

Description:
As a reader, I want to view news articles from different sources so that I can access multiple perspectives from one platform.

Tasks:
- Create Article, Category, and NewsSource models
- Register models in admin
- Create seed data
- Build homepage article list
- Display article source, category, date, and summary

Labels:
user-story, iteration-1, priority-10