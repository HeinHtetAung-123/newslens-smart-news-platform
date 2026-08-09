# NewsLens Tools and Technologies Documentation

## 1. Tools Overview

NewsLens was developed using modern software development tools, web development frameworks, external libraries, version control, testing tools, and project management tools.

The tools were selected to support:

- Agile iterative development
- Web application development
- Database-backed features
- Automated testing
- External API integration
- Version control
- Project documentation
- Local development and future deployment

---

## 2. Programming Language

### Python

Python was used as the main programming language for NewsLens.

Python was suitable because:

- It works well with Django.
- It supports fast web development.
- It has strong testing support.
- It has useful libraries for API integration.
- It is readable and suitable for coursework development.

Python was used for:

- Django models
- Views
- URL routing
- Services/helper functions
- Management commands
- Automated tests
- Mock object tests

---

## 3. Web Framework

### Django

Django was used as the main web framework for NewsLens.

Django was selected because it provides:

- Model-View-Template structure
- Built-in user authentication
- Database models through Django ORM
- Admin panel
- URL routing
- Template rendering
- Static file support
- Built-in testing framework
- Management commands

Django helped the project deliver features quickly across three iterations.

Main Django areas used:

| Django Feature | How It Was Used |
|---|---|
| Models | Stored articles, categories, sources, saved articles, alerts, and preferences |
| Views | Handled page requests and user actions |
| Templates | Displayed the user interface |
| URLs | Connected routes to views |
| Admin | Managed articles, categories, sources, and alerts |
| Authentication | Supported register, login, logout, and protected actions |
| TestCase | Supported automated testing |
| Management command | Supported News API fetching |

---

## 4. Development Environment

### PyCharm

PyCharm was used as the main development environment.

PyCharm supported the project by providing:

- Code editing
- Project file navigation
- Terminal access
- Python virtual environment support
- Git integration
- Error highlighting
- Django project management

Using PyCharm made development easier because the code, terminal, project structure, and Git tools were available in one environment.

---

## 5. Version Control Tools

### Git

Git was used for version control. It helped track changes during the development of NewsLens.

Git was used to:

- Save progress through commits
- Track code changes
- Revert or review changes if needed
- Manage iteration progress
- Push updates to GitHub
- Keep documentation and code together

Example Git commands used:

```bash
git add .
git commit -m "Add testing documentation and evidence"
git pull --rebase origin main
git push origin main
```

### GitHub

GitHub was used to store the project repository and provide evidence of development work.

GitHub was used for:

- Repository hosting
- Commit history
- Project board tracking
- Issues/user stories
- Labels
- Documentation pages
- Practical evidence
- Final project evidence pages

---

## 6. Project Management Tools

### GitHub Issues

GitHub Issues were used to represent user stories, tasks, and bugs.

Issue labels included:

- `user-story`
- `bug`
- `iteration-1`
- `iteration-2`
- `iteration-3`
- `priority-10`
- `priority-20`
- `priority-30`
- `priority-40`
- `priority-50`
- `testing`

### GitHub Project Board

The project board was used to track progress across iterations.

The workflow used was:

```text
Todo → In Progress → Done
```

For bug tracking, the workflow was extended to:

```text
Todo → In Progress → Fixed → Verified → Done
```

This helped show agile progress and made the work visible throughout development.

---

## 7. Database Tools

### SQLite for Local Development

SQLite was used during local development because it is simple and works automatically with Django.

SQLite was useful because:

- It required minimal setup.
- It worked well for local development.
- It supported quick testing.
- It allowed fast iteration.
- It integrated easily with Django ORM.

### MySQL Production Plan

The project design can be moved to MySQL for a more production-ready database because NewsLens uses Django ORM models instead of database-specific SQL.

A future MySQL deployment would be suitable because:

- MySQL is a modern relational database.
- It supports larger datasets.
- It is more appropriate for deployed multi-user applications.
- It fits the relational design of NewsLens.

---

## 8. Database Management Through Django ORM

Django ORM was used to interact with the database through Python model classes.

Main models included:

| Model | Purpose |
|---|---|
| Category | Stores article categories |
| NewsSource | Stores news source information |
| Article | Stores article data |
| SavedArticle | Stores saved user articles |
| BreakingNewsAlert | Stores breaking news alerts |
| UserPreference | Stores preferred categories for users |

Using Django ORM made the database easier to manage because database tables were represented as Python classes.

---

## 9. External API Tool

### News API

NewsLens used an external News API to fetch realistic article data.

The API feature supported:

- More realistic news content
- Multiple categories
- Article title, source, description, content, image URL, original URL, and published date
- Breaking news alert creation
- Database-backed article storage

The API key was stored in `.env` instead of being hard-coded into the source code.

This made the project safer because private keys were not committed to GitHub.

---

## 10. Environment Variable Tool

### python-dotenv

`python-dotenv` was used to load environment variables from a `.env` file.

It was used for:

```text
NEWS_API_KEY
```

This allowed the project to keep sensitive API keys outside the source code.

Example:

```python
from dotenv import load_dotenv
load_dotenv()
```

This helped make the project safer and more realistic.

---

## 11. HTTP Library

### requests

The `requests` library was used to call the external News API.

It was used in the fetch news management command to:

- Send API requests
- Receive API responses
- Read JSON data
- Handle response status codes
- Save returned article data into the database

The API feature was later tested using mock objects so the real API did not need to be called during automated tests.

---

## 12. Testing Tools

### Django TestCase

Django `TestCase` was used for automated testing.

The tests checked:

- Homepage loading
- Article feed display
- Category filtering
- Search
- Quick summaries
- Saved articles
- Breaking alerts
- Compare Sources page
- Mock API response handling

Tests were run using:

```bash
python manage.py test news
```

Final test result:

```text
Ran 23 tests in 7.379s

OK
Destroying test database for alias 'default'...
```

---

## 13. Mock Testing Tools

### unittest.mock

Python’s `unittest.mock` library was used for mock object testing.

Mock testing was used to replace the real News API request with a fake response.

This was important because the real API:

- Requires internet access
- Requires an API key
- Can return changing data
- Can fail because of rate limits
- Should not be required for repeatable tests

Mock testing allowed the project to test API behaviour safely and predictably.

Example tools used:

```python
from unittest.mock import Mock, patch
```

---

## 14. Front-End Tools

### HTML

HTML was used to structure the pages.

Main templates included:

- Homepage
- Article detail page
- Category page
- Search results page
- Saved articles page
- Compare Sources page
- Preferences page
- Admin dashboard
- Login/register pages

### CSS

CSS was used to improve the user interface.

CSS supported:

- Article card layout
- Responsive layout
- Navigation styling
- Breaking news alert design
- Image placeholder design
- Compare Sources visual map
- Button alignment
- Admin dashboard styling
- Recommended article cards

The interface was improved throughout the project based on testing and feedback.

---

## 15. Build and Setup Tools

### Virtual Environment

A Python virtual environment was used to manage project dependencies.

Example setup command:

```bash
python -m venv venv
```

Activation on Windows:

```bash
venv\Scripts\activate
```

Using a virtual environment kept the project dependencies separate from the global Python installation.

### pip

`pip` was used to install dependencies.

Examples:

```bash
pip install django
pip install requests
pip install python-dotenv
```

### requirements.txt

`requirements.txt` was used to record project dependencies.

Example command:

```bash
pip freeze > requirements.txt
```

This makes the project easier to rebuild on another machine or deployment platform.

---

## 16. Django Management Commands

Django management commands were used for development tasks.

Common commands included:

```bash
python manage.py runserver
```

Used to run the local development server.

```bash
python manage.py makemigrations
```

Used to create database migration files.

```bash
python manage.py migrate
```

Used to apply database changes.

```bash
python manage.py createsuperuser
```

Used to create an admin account.

```bash
python manage.py test news
```

Used to run automated tests.

```bash
python manage.py fetch_news
```

Used to fetch articles from the external News API.

---

## 17. Deployment-Related Tools

NewsLens was designed so it can be deployed to a Python-compatible hosting platform.

Suitable deployment options include:

- Render
- Railway
- PythonAnywhere

The project supports deployment through:

- Django project structure
- `requirements.txt`
- Environment variables
- Static file structure
- Database-backed models
- External API key separation

---

## 18. Documentation Tools

### Markdown

Markdown was used to write project documentation.

Documentation files included:

- Practical documentation
- User story pages
- Design documentation
- Delivered solution page
- Testing documentation
- Tools documentation
- Agile process documentation

Markdown was suitable because it works well with GitHub and allows clear headings, tables, code blocks, and links.

### Mermaid

Mermaid was used to create diagrams in Markdown.

Mermaid diagrams included:

- Architecture diagram
- Database ERD
- Class diagram
- Sequence diagrams
- Burndown charts

This made the documentation more visual and easier to understand.

---

## 19. External Libraries Summary

| Tool / Library | Purpose |
|---|---|
| Django | Main web framework |
| python-dotenv | Load environment variables |
| requests | Call external News API |
| unittest.mock | Mock external API calls in tests |
| SQLite | Local development database |
| Git | Version control |
| GitHub | Repository, issues, board, documentation |
| Mermaid | Diagrams and burndown charts |
| PyCharm | Development environment |

---

## 20. Why These Tools Were Appropriate

The selected tools were appropriate because they supported the requirements of the project.

| Requirement | Tool Support |
|---|---|
| Build a web application | Django, Python, HTML, CSS |
| Store articles and users | Django ORM, SQLite, future MySQL |
| Fetch realistic news data | News API, requests |
| Protect API key | python-dotenv, `.env` |
| Test the system | Django TestCase, unittest.mock |
| Track development | Git, GitHub |
| Manage agile workflow | GitHub Issues and Project Board |
| Document the project | Markdown and Mermaid |
| Develop efficiently | PyCharm and virtual environment |

---

## 21. Tools Summary

NewsLens used a strong set of software development tools to support coding, testing, project management, documentation, and future deployment.

The main tools were Django, Python, PyCharm, Git, GitHub, SQLite, News API, `requests`, `python-dotenv`, Django TestCase, `unittest.mock`, Markdown, and Mermaid.

Together, these tools helped the project deliver the planned NewsLens features through an agile iterative process.