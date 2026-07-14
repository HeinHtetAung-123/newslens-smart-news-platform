# Practical 2: Requirements Gathering and User Stories

## 1. Purpose of Practical 2

The purpose of this practical is to gather early requirements for the NewsLens project through mock interviews and convert those requirements into user stories. These user stories will later be prioritised, estimated, and planned into three development iterations.

NewsLens is a smart news aggregation website that allows users to read news from multiple sources, view quick summaries, browse by category, receive breaking news alerts, save articles, and compare how different sources report the same story.

---

# 2. Mock Interviews

## Interview 1: General News Reader

**Role:** General user
**Goal:** Wants a simple way to read news from different sources.

### Questions and Answers

**Q1. How do you normally read news?**
I usually read news from different websites and social media, but it is time-consuming to move between platforms.

**Q2. What problem do you face when reading news online?**
There are too many articles and sometimes different sources report the same story differently. It is hard to know what to focus on.

**Q3. What feature would help you most?**
I would like one website where I can see news from different sources and browse by category.

**Q4. Would summaries be useful?**
Yes. A short summary would help me understand the main points before deciding whether to read the full article.

**Q5. Would you save articles?**
Yes. I would like to save important articles and read them later.

### Requirements Collected

* Users should be able to view news from multiple sources.
* Users should be able to browse news by category.
* Users should be able to read quick article summaries.
* Users should be able to save articles for later.

---

## Interview 2: Student User

**Role:** Student
**Goal:** Wants to compare sources for learning and research.

### Questions and Answers

**Q1. Why would you use a news website like NewsLens?**
I would use it to understand current events and compare how different sources explain the same issue.

**Q2. What would make the platform useful for study?**
The comparison feature would be useful because it can show different viewpoints from different news sources.

**Q3. What kind of comparison would help you?**
I would like to see the main points from each source, the tone, and whether one article focuses more on politics, business, society, or other angles.

**Q4. Do you need search?**
Yes. Search is important because I may need to find specific topics like AI, elections, climate change, or business news.

**Q5. Should the system explain bias?**
Yes, but it should not claim that one source is always right or wrong. It should show indicators and let users think critically.

### Requirements Collected

* Users should be able to search for news by keyword.
* Users should be able to compare articles about the same story.
* The system should show tone and balance insights.
* The system should support critical reading without claiming perfect bias detection.

---

## Interview 3: Busy Professional

**Role:** Busy reader
**Goal:** Wants quick updates and breaking news.

### Questions and Answers

**Q1. What is your biggest issue with reading news?**
I do not have much time to read long articles.

**Q2. What would help you stay updated?**
Short summaries and breaking news alerts would be helpful.

**Q3. How should breaking news be shown?**
A clear alert banner or notification area on the website would be enough for the first version.

**Q4. Do you want to customise the news you see?**
Yes. I would like to choose categories such as business, technology, sports, and local news.

**Q5. What should the homepage show?**
It should show the latest news, breaking news, and categories clearly.

### Requirements Collected

* Users should be able to view quick article summaries.
* Users should be able to receive or view breaking news alerts.
* Users should be able to choose or browse preferred categories.
* The homepage should show latest and important news clearly.

---

## Interview 4: Admin User

**Role:** Platform admin
**Goal:** Wants to manage news sources, categories, and alerts.

### Questions and Answers

**Q1. What does the admin need to manage?**
The admin should manage categories, sources, and breaking news alerts.

**Q2. Why is source management important?**
The platform needs reliable sources, and the admin should be able to update or remove sources if needed.

**Q3. Should admins manage users?**
Basic user management may be useful, but it is not the first priority.

**Q4. What about breaking news?**
Admins should be able to mark important stories as breaking news or manage alert messages.

**Q5. What should be kept simple for the first version?**
The first version should focus on news display, categories, search, summaries, saved articles, and basic admin management.

### Requirements Collected

* Admin should be able to manage news sources.
* Admin should be able to manage news categories.
* Admin should be able to manage breaking news alerts.
* Admin should help maintain platform quality.

---

# 3. Consolidated Requirements

After reviewing the mock interviews, the following main requirements were identified:

| ID  | Requirement                                                                                    |
| --- | ---------------------------------------------------------------------------------------------- |
| R01 | The system should display news articles from multiple sources.                                 |
| R02 | The system should allow users to browse news by category.                                      |
| R03 | The system should provide quick summaries for news articles.                                   |
| R04 | The system should allow users to search for news by keyword.                                   |
| R05 | The system should allow registered users to save articles.                                     |
| R06 | The system should display breaking news alerts.                                                |
| R07 | The system should allow users to compare articles from different sources about the same story. |
| R08 | The system should provide tone, bias, and balance insights.                                    |
| R09 | The system should allow users to register, log in, and manage their account.                   |
| R10 | The system should allow admins to manage categories, sources, and alerts.                      |

---

# 4. User Stories with Priority and Effort Estimates

Priority scale:

* 10 = Highest priority
* 20 = High priority
* 30 = Medium priority
* 40 = Low priority
* 50 = Lowest priority

Effort is estimated in development days for a solo developer.

| ID   | Title                     | User Story / Short Description                                                                                                                                                  | Priority | Estimate |
| ---- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | -------- |
| US01 | User Account Access       | As a user, I want to register, log in, and log out so that I can access personal features such as saved articles and preferences.                                               | 10       | 3 days   |
| US02 | Multi-Source News Feed    | As a user, I want to view news articles from multiple sources so that I can access different perspectives in one platform.                                                      | 10       | 4 days   |
| US03 | News Categories           | As a user, I want to browse news by categories such as politics, technology, sports, business, entertainment, and local news so that I can find news that matches my interests. | 10       | 2 days   |
| US04 | Article Detail Page       | As a user, I want to open a news article detail page so that I can view the article title, source, category, publication date, summary, and original article link.              | 10       | 3 days   |
| US05 | Search News               | As a user, I want to search for news using keywords so that I can quickly find specific stories or topics.                                                                      | 20       | 3 days   |
| US06 | Quick Article Summary     | As a user, I want to read a quick summary of each article so that I can understand the main points faster.                                                                      | 20       | 4 days   |
| US07 | Save Articles             | As a registered user, I want to save articles so that I can read them later.                                                                                                    | 20       | 3 days   |
| US08 | Breaking News Alerts      | As a user, I want to see breaking news alerts so that I can stay updated on urgent news.                                                                                        | 30       | 3 days   |
| US09 | Same-Story Comparison     | As a user, I want to compare how different sources report the same story so that I can understand different viewpoints.                                                         | 30       | 5 days   |
| US10 | Bias and Balance Insights | As a user, I want to see tone, bias, and balance indicators so that I can think more critically about the news I read.                                                          | 40       | 5 days   |
| US11 | User Preferences          | As a user, I want to choose preferred news categories so that the platform can show more relevant news.                                                                         | 40       | 3 days   |
| US12 | Admin Management          | As an admin, I want to manage categories, sources, and breaking news alerts so that the platform remains organised and useful.                                                  | 50       | 4 days   |

---

# 5. Justification of Priorities

The highest-priority user stories are the features needed to make the platform usable as a news website. These include user account access, multi-source news feed, categories, and article detail pages. Without these, the system cannot provide its core service.

Search, summaries, and saved articles are high-priority features because they improve the user experience and directly support the project goal of helping users access and understand news more efficiently.

Breaking news alerts and same-story comparison are medium-priority because they add stronger value after the basic reading experience is working.

Bias and balance insights, user preferences, and admin management are lower-priority for the first milestone because they are more advanced or supporting features. They are still important, but they should be developed after the core platform is stable.

---

# 6. Estimation Justification

The estimates are based on the expected development effort for a solo developer. Smaller features such as categories are estimated at 2 days because they mainly involve database fields, filtering, and interface updates. Larger features such as same-story comparison and bias insights are estimated at 5 days because they require more logic, data handling, and user interface design.

The estimates are rough at this stage and will be reviewed again when user stories are split into smaller development tasks during Iteration 1. Task-level estimates will provide more confidence and may lead to adjustments in the iteration plan.

---

# 7. Practical 2 Summary

This practical gathered requirements through mock interviews with different user types: general reader, student user, busy professional, and admin user. The collected requirements were then converted into user stories with titles, short descriptions, priorities, and effort estimates. These user stories will be used to plan Milestone 1 across three iterations.
