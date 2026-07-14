# Practical 3: Iteration Planning and Iteration 1 Board

## 1. Purpose of Practical 3

The purpose of this practical is to plan Milestone 1 for the NewsLens project and organise the planned user stories into three development iterations. The project is being completed by a solo developer, so the planned workload must be realistic and manageable.

This practical also creates a simple project board for Iteration 1 using the labels Todo, In Progress, and Done. A burn-down graph is also prepared to monitor the progress of Iteration 1.

---

# 2. Milestone 1 Overview

Milestone 1 is the first major release of the NewsLens project. The goal of Milestone 1 is to deliver a usable version of the smart news aggregation website with the most important features first.

The main purpose of Milestone 1 is to deliver:

* user account access
* multi-source news feed
* news categories
* article detail page
* search feature
* quick article summaries
* saved articles
* basic breaking news alerts
* basic same-story comparison
* early bias and balance insight support

The project uses three iterations for Milestone 1. Each iteration is planned based on user story priority and estimated effort.

---

# 3. User Story Allocation Across Three Iterations

Priority scale:

* 10 = Highest priority
* 20 = High priority
* 30 = Medium priority
* 40 = Low priority
* 50 = Lowest priority

## Iteration 1: Core Platform Foundation

Iteration 1 focuses on building the basic foundation of the website. These features are needed before advanced features such as summaries, alerts, and comparison can work properly.

| ID   | User Story             | Priority | Estimate | Reason for Iteration 1                                                    |
| ---- | ---------------------- | -------: | -------: | ------------------------------------------------------------------------- |
| US01 | User Account Access    |       10 |   3 days | Needed for user-specific features such as saved articles and preferences. |
| US02 | Multi-Source News Feed |       10 |   4 days | Core feature of the platform. Users must be able to view news articles.   |
| US03 | News Categories        |       10 |   2 days | Helps organise news and improves navigation.                              |
| US04 | Article Detail Page    |       10 |   3 days | Users need to open and read article information clearly.                  |
| US05 | Search News            |       20 |   3 days | Important for finding specific stories and topics.                        |

**Total Iteration 1 Estimate:** 15 days

---

## Iteration 2: User Engagement and News Understanding

Iteration 2 focuses on improving the reading experience after the basic platform is working.

| ID   | User Story            | Priority | Estimate | Reason for Iteration 2                            |
| ---- | --------------------- | -------: | -------: | ------------------------------------------------- |
| US06 | Quick Article Summary |       20 |   4 days | Helps users understand articles faster.           |
| US07 | Save Articles         |       20 |   3 days | Allows registered users to store useful articles. |
| US08 | Breaking News Alerts  |       30 |   3 days | Keeps users updated on urgent stories.            |

**Total Iteration 2 Estimate:** 10 days

---

## Iteration 3: Advanced Comparison and Insight Features

Iteration 3 focuses on the more advanced features that make NewsLens different from a basic news website.

| ID   | User Story                | Priority | Estimate | Reason for Iteration 3                                                             |
| ---- | ------------------------- | -------: | -------: | ---------------------------------------------------------------------------------- |
| US09 | Same-Story Comparison     |       30 |   5 days | Allows users to compare how different sources report the same story.               |
| US10 | Bias and Balance Insights |       40 |   5 days | Provides insight into tone, focus, balance, and possible bias.                     |
| US11 | User Preferences          |       40 |   3 days | Improves personalisation after core features are stable.                           |
| US12 | Admin Management          |       50 |   4 days | Supports platform maintenance but is lower priority for the first working release. |

**Total Iteration 3 Estimate:** 17 days

---

# 4. Justification of Iteration Order

The highest-priority user stories are placed in Iteration 1 because they create the foundation of the system. Users must first be able to register, view news, browse categories, open article details, and search for articles. Without these features, the platform cannot function as a useful news website.

Iteration 2 adds features that improve user engagement and understanding, such as summaries, saved articles, and breaking news alerts. These features depend on the basic article and user account features created in Iteration 1.

Iteration 3 includes the most advanced features, such as same-story comparison, bias and balance insights, preferences, and admin management. These are important but should be developed after the core platform is stable.

This order helps the project deliver what is needed first while keeping the workload realistic for a solo developer.

---

# 5. Iteration 1 Project Board

The Iteration 1 board tracks the status of user stories using three labels:

* Todo
* In Progress
* Done

## Iteration 1 Board at Start

| User Story ID | Title                  | Estimate | Status |
| ------------- | ---------------------- | -------: | ------ |
| US01          | User Account Access    |   3 days | Todo   |
| US02          | Multi-Source News Feed |   4 days | Todo   |
| US03          | News Categories        |   2 days | Todo   |
| US04          | Article Detail Page    |   3 days | Todo   |
| US05          | Search News            |   3 days | Todo   |

At the beginning of Iteration 1, all user stories are marked as Todo.

---

# 6. Iteration 1 Implementation Plan

| Day    | Planned Work                                                                          |
| ------ | ------------------------------------------------------------------------------------- |
| Day 1  | Set up Django project structure, database connection, base templates, and navigation. |
| Day 2  | Implement user registration, login, and logout.                                       |
| Day 3  | Test user account access and update authentication UI.                                |
| Day 4  | Create article, source, and category models.                                          |
| Day 5  | Add sample article data and display news feed.                                        |
| Day 6  | Improve homepage news card layout and source display.                                 |
| Day 7  | Implement category filtering.                                                         |
| Day 8  | Test category browsing and fix navigation issues.                                     |
| Day 9  | Create article detail page.                                                           |
| Day 10 | Show article metadata, source, category, summary placeholder, and original link.      |
| Day 11 | Implement search form and search results page.                                        |
| Day 12 | Add keyword search across title, source, and category.                                |
| Day 13 | Test search and article detail navigation.                                            |
| Day 14 | UI cleanup, bug fixing, and documentation updates.                                    |
| Day 15 | Final Iteration 1 review and prepare feedback/demo notes.                             |

---

# 7. Burn Down Graph Data for Iteration 1

Iteration 1 has a total estimated workload of 15 days.

The burn-down graph tracks the remaining estimated work across the iteration.

| Iteration Day | Planned Remaining Work | Actual Remaining Work |
| ------------: | ---------------------: | --------------------: |
|             0 |                     15 |                    15 |
|             1 |                     14 |                    15 |
|             2 |                     13 |                    14 |
|             3 |                     12 |                    12 |
|             4 |                     11 |                    12 |
|             5 |                     10 |                    10 |
|             6 |                      9 |                     9 |
|             7 |                      8 |                     8 |
|             8 |                      7 |                     8 |
|             9 |                      6 |                     6 |
|            10 |                      5 |                     5 |
|            11 |                      4 |                     4 |
|            12 |                      3 |                     3 |
|            13 |                      2 |                     2 |
|            14 |                      1 |                     1 |
|            15 |                      0 |                     0 |

The planned line decreases steadily from 15 days to 0 days. The actual line may change depending on real development progress. At the start of the project, this table acts as a planned monitoring structure. It will be updated during and after Iteration 1.

---

# 8. Burn Down Graph Explanation

The burn-down graph is used to monitor whether Iteration 1 is on track. If the actual remaining work stays close to the planned remaining work, the iteration is progressing well. If the actual remaining work is higher than planned, it means development is slower than expected and the iteration may need adjustment.

Since this project is completed by one developer, the burn-down graph helps keep the workload realistic and shows whether the planned 15 days of work can be completed within the iteration.

---

# 9. GitHub Tracking Plan

For Iteration 1, GitHub will be used to track work through issues, labels, commits, and project board status updates.

## GitHub Labels

| Label         | Purpose                                      |
| ------------- | -------------------------------------------- |
| todo          | Work has not started yet.                    |
| in-progress   | Work is currently being developed.           |
| done          | Work has been completed.                     |
| iteration-1   | Work belongs to Iteration 1.                 |
| user-story    | Issue represents a user story.               |
| task          | Issue represents a smaller development task. |
| bug           | Issue represents an error or problem.        |
| documentation | Issue is related to project documentation.   |

## GitHub Issues for Iteration 1

| Issue Title                  | Label                         |
| ---------------------------- | ----------------------------- |
| US01: User Account Access    | user-story, iteration-1, todo |
| US02: Multi-Source News Feed | user-story, iteration-1, todo |
| US03: News Categories        | user-story, iteration-1, todo |
| US04: Article Detail Page    | user-story, iteration-1, todo |
| US05: Search News            | user-story, iteration-1, todo |

---

# 10. Practical 3 Summary

Practical 3 planned Milestone 1 by allocating user stories into three iterations. Iteration 1 focuses on the core platform foundation, Iteration 2 focuses on user engagement and news understanding, and Iteration 3 focuses on advanced comparison and insight features.

A project board was created for Iteration 1 using Todo, In Progress, and Done labels. A burn-down graph data table was also prepared to monitor Iteration 1 progress.
