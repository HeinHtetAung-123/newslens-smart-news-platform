# NewsLens Design Documentation

## 1. Design Overview

NewsLens is a smart news aggregation and bias insight platform. The system allows users to read news articles, browse categories, search for articles, save articles, view breaking news alerts, compare related coverage, and review bias/balance insights.

The design was created to support the main project requirements and user stories. The system uses a Django web application structure, where models manage data, views handle user requests, templates display the interface, and helper services support reusable logic such as quick summaries and bias insight generation.

The design focuses on:

- Clear separation of responsibilities
- Simple and maintainable database structure
- User-friendly interface design
- Support for iterative feature development
- Testable components

---

## 2. Architectural Design

NewsLens follows a Model-View-Template architecture using Django.

```mermaid
flowchart TD
    User[User Browser] --> Templates[HTML Templates and CSS]
    Templates --> Views[Django Views]
    Views --> Models[Django Models]
    Models --> Database[(Database)]
    Views --> Services[Helper Services]
    Services --> Models
    FetchCommand[Fetch News Command] --> NewsAPI[External News API]
    FetchCommand --> Models
    Admin[Django Admin / Admin Dashboard] --> Models
```

## 3. Architecture Explanation

The main architectural components are:

| Component | Purpose |
|---|---|
| User Browser | Allows readers and admins to interact with NewsLens |
| HTML Templates and CSS | Display pages such as homepage, article detail, saved articles, and compare sources |
| Django Views | Handle user requests and return the correct page or action |
| Django Models | Store and manage articles, categories, sources, saved articles, alerts, and preferences |
| Database | Stores all application data |
| Helper Services | Provide reusable logic such as quick summaries and bias insight |
| Fetch News Command | Retrieves article data from the external News API |
| Django Admin / Admin Dashboard | Allows admin users to manage and review system data |

This design was selected because Django supports rapid development, authentication, database models, admin management, testing, and template-based web pages. This made it suitable for a solo agile project with three short development iterations.

---

## 4. Major Components

### 4.1 User Account Component

The user account component supports registration, login, logout, saved articles, and user preferences.

Main features:

- User registration
- User login and logout
- Logged-in users can save articles
- Logged-in users can select preferred categories
- Homepage recommendations use saved user preferences

Related user stories:

| User Story | Feature |
|---|---|
| US01 | User Account Access |
| US07 | Save Articles |
| US11 | User Preferences |

---

### 4.2 Article Feed Component

The article feed component displays the main list of articles on the homepage. It shows article title, source, category, published date, quick summary, and link to read more.

Main features:

- Latest articles
- Multi-source article feed
- Article cards
- Category display
- Quick summary display
- Image placeholder for articles without images

Related user stories:

| User Story | Feature |
|---|---|
| US02 | Multi-Source News Feed |
| US04 | Article Detail Page |
| US06 | Quick Article Summary |

---

### 4.3 Category Component

The category component allows users to browse articles by topic. Categories include areas such as technology, sports, business, entertainment, and other news groups.

Main features:

- Category links
- Category filtered pages
- Homepage category sections
- Article grouping by category

Related user story:

| User Story | Feature |
|---|---|
| US03 | News Categories |

---

### 4.4 Search Component

The search component allows users to search for articles using keywords. It searches article information such as title, description, summary, content, source, and category.

Main features:

- Search bar
- Search results page
- Keyword matching
- Empty result handling

Related user story:

| User Story | Feature |
|---|---|
| US05 | Search News |

---

### 4.5 Breaking News Alert Component

The breaking news alert component highlights urgent or important news on the homepage. Admin users can manage alerts, and only active alerts are displayed to readers.

Main features:

- Breaking alert model
- Active/inactive alert status
- Homepage breaking news section
- Admin management through Django admin

Related user story:

| User Story | Feature |
|---|---|
| US08 | Breaking News Alerts |

---

### 4.6 Source Comparison Component

The source comparison component allows readers to compare related articles from different sources. It includes a selected article, related source cards, a visual source map, and comparison guidance.

Main features:

- Compare Sources page
- Main selected article
- Related articles from the same category
- Visual source map
- Comparison insight cards
- Links to related article details

Related user story:

| User Story | Feature |
|---|---|
| US09 | Same-Story Comparison |

---

### 4.7 Bias and Balance Insight Component

The bias and balance insight component gives readers simple guidance about article wording and source balance. It does not claim to fully determine political bias. Instead, it encourages users to compare coverage before forming an opinion.

Main features:

- Source context
- Category context
- Wording style detection
- Strong word count
- Balance reminder
- Article detail insight panel

Related user story:

| User Story | Feature |
|---|---|
| US10 | Bias and Balance Insights |

---

### 4.8 Admin Management Component

The admin management component supports content review and system management. Django admin is used for managing database records, while a custom admin dashboard provides a summary of system data.

Main features:

- Django admin registration
- Staff-only dashboard
- Article count
- Category count
- Source count
- Saved article count
- Breaking alert count

Related user story:

| User Story | Feature |
|---|---|
| US12 | Admin Management |

---

## 5. Database Design

The database design stores articles, sources, categories, saved articles, breaking news alerts, and user preferences.

```mermaid
erDiagram
    User ||--o{ SavedArticle : saves
    Article ||--o{ SavedArticle : is_saved_in
    Category ||--o{ Article : contains
    NewsSource ||--o{ Article : publishes
    Article ||--o{ BreakingNewsAlert : has
    User ||--|| UserPreference : owns
    UserPreference }o--o{ Category : prefers

    User {
        int id
        string username
        string password
        string email
    }

    Category {
        int id
        string name
        string slug
    }

    NewsSource {
        int id
        string name
        string website_url
    }

    Article {
        int id
        string title
        text description
        text summary
        text content
        string image_url
        string original_url
        datetime published_at
        int category_id
        int source_id
    }

    SavedArticle {
        int id
        int user_id
        int article_id
        datetime saved_at
    }

    BreakingNewsAlert {
        int id
        int article_id
        string alert_title
        text message
        boolean is_active
        datetime created_at
    }

    UserPreference {
        int id
        int user_id
    }
```

---

## 6. Database Table Explanation

| Table | Purpose |
|---|---|
| User | Stores Django user accounts |
| Category | Stores article categories |
| NewsSource | Stores news source information |
| Article | Stores article information |
| SavedArticle | Stores articles saved by users |
| BreakingNewsAlert | Stores homepage breaking news alerts |
| UserPreference | Stores user category preferences |

The database design supports all major project features. Articles are connected to categories and sources, which allows filtering, searching, and comparison. SavedArticle connects users to articles, which supports personalised saved lists. UserPreference connects users to preferred categories, which supports homepage recommendations.

---

## 7. Class Design

The main classes in NewsLens are represented by Django models.

```mermaid
classDiagram
    class User {
        +username
        +password
        +email
    }

    class Category {
        +name
        +slug
    }

    class NewsSource {
        +name
        +website_url
    }

    class Article {
        +title
        +description
        +summary
        +content
        +image_url
        +original_url
        +published_at
        +get_quick_summary()
    }

    class SavedArticle {
        +user
        +article
        +saved_at
    }

    class BreakingNewsAlert {
        +article
        +alert_title
        +message
        +is_active
        +created_at
    }

    class UserPreference {
        +user
        +preferred_categories
    }

    User "1" --> "many" SavedArticle
    Article "1" --> "many" SavedArticle
    Category "1" --> "many" Article
    NewsSource "1" --> "many" Article
    Article "1" --> "many" BreakingNewsAlert
    User "1" --> "1" UserPreference
    UserPreference "many" --> "many" Category
```

---

## 8. Interface Design

The interface design was created to make NewsLens simple to use. The main design goal was to let users quickly find, read, save, and compare news articles.

Main interface pages:

| Page | Purpose |
|---|---|
| Homepage | Shows latest articles, category sections, breaking alerts, and recommendations |
| Category Page | Shows articles from one category |
| Search Results Page | Shows articles matching the search keyword |
| Article Detail Page | Shows full article information, quick summary, bias insight, save button, and original source link |
| Saved Articles Page | Shows articles saved by the logged-in user |
| Compare Sources Page | Shows related coverage and visual comparison |
| Preferences Page | Allows logged-in users to choose preferred categories |
| Admin Dashboard | Shows system statistics for staff users |

---

## 9. Interface Flow

```mermaid
flowchart TD
    Home[Homepage] --> Category[Category Page]
    Home --> Search[Search Results]
    Home --> Detail[Article Detail]
    Detail --> Save[Save Article]
    Save --> Saved[Saved Articles Page]
    Detail --> Compare[Compare Sources Page]
    Home --> Preferences[User Preferences]
    Preferences --> Recommended[Recommended Articles on Homepage]
    Staff[Staff User] --> AdminDashboard[Admin Dashboard]
```

---

## 10. Key UI Design Decisions

| UI Decision | Justification |
|---|---|
| Card-based article layout | Makes articles easy to scan quickly |
| Category navigation | Helps users browse by topic |
| Quick summaries | Helps users understand articles faster |
| Breaking news section | Makes urgent news more visible |
| Placeholder image design | Keeps layout consistent when article images are missing |
| Compare Sources page | Supports critical reading and multiple perspectives |
| Bias insight panel | Encourages users to think about wording and balance |
| Saved articles page | Gives logged-in users personal reading storage |
| Preferences page | Supports personalised recommendations |
| Staff dashboard | Gives admin users a quick system overview |

---

## 11. Sequence Design: Search News

```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant View as Django Search View
    participant Model as Article Model
    participant DB as Database
    participant Template as Search Results Template

    User->>Browser: Enter search keyword
    Browser->>View: Send search request
    View->>Model: Query articles by keyword
    Model->>DB: Search title, summary, description, content, source, category
    DB-->>Model: Return matching articles
    Model-->>View: Matching article objects
    View->>Template: Pass results and keyword
    Template-->>Browser: Display search results
    Browser-->>User: Show matching articles
```

---

## 12. Sequence Design: Save Article

```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant View as Save Article View
    participant Model as SavedArticle Model
    participant DB as Database

    User->>Browser: Click Save Article
    Browser->>View: Send save request
    View->>View: Check user is logged in
    View->>Model: Create SavedArticle record
    Model->>DB: Save user and article relationship
    DB-->>Model: Confirm saved record
    Model-->>View: Return saved article
    View-->>Browser: Redirect to article detail page
    Browser-->>User: Article appears as saved
```

---

## 13. Sequence Design: Compare Sources

```mermaid
sequenceDiagram
    actor User
    participant Browser
    participant View as Compare Sources View
    participant ArticleModel as Article Model
    participant DB as Database
    participant Template as Compare Sources Template

    User->>Browser: Click Compare Sources
    Browser->>View: Request compare page
    View->>ArticleModel: Get selected article
    ArticleModel->>DB: Query selected article by ID
    DB-->>ArticleModel: Return selected article
    View->>ArticleModel: Get related articles from same category
    ArticleModel->>DB: Query related articles
    DB-->>ArticleModel: Return related articles
    View->>Template: Pass main article and related articles
    Template-->>Browser: Display visual comparison page
    Browser-->>User: User compares related coverage
```

---

## 14. Design Justification

The design supports the project requirements because each major user story is connected to a clear system component. The Django architecture made it possible to build the system iteratively across three iterations.

The database design is simple but effective because it stores only the data needed for the planned features. The interface design focuses on usability, with article cards, summaries, category browsing, saved articles, comparison pages, and clear navigation.

The design also supports testing because models, views, helper services, and templates can be tested separately. Mock object testing was also possible because the external News API dependency was isolated in the fetch command.

Overall, the design allowed NewsLens to deliver the planned requirements on time while keeping the system maintainable and understandable.