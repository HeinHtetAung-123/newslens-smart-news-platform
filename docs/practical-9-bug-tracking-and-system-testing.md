# Practical 9: Bug Tracking and System Testing Plan

## 1. Practical Objective

The objective of Practical 9 was to review error tracking and system testing for the NewsLens project. This practical focused on identifying bugs, recording them clearly, tracking them through the project board, and preparing a system testing plan for the final Week 10 demonstration.

NewsLens was tested as a complete system, including the homepage, article list, article detail page, search, saved articles, breaking news alerts, source comparison, bias insight, user preferences, admin dashboard, and News API fetching feature.

---

## 2. Bug and Error Tracking Approach

Bugs were tracked using GitHub Issues and the GitHub project board. Each bug was treated like project work and moved through the board until it was fixed and checked.

The workflow used was:

```text
Todo → In Progress → Fixed → Verified → Done
```

This made the bug fixing process visible and easier to manage, even though the project was completed by one developer.

---

## 3. Bug Labels Used

The following labels were used or planned for bug tracking:

| Label | Purpose |
|---|---|
| `bug` | Identifies the issue as a defect |
| `iteration-3` | Shows the bug was found during Iteration 3/final testing |
| `testing` | Shows the issue was found during testing |
| `priority-high` | Important bug that affects main functionality |
| `priority-medium` | Bug affects usability but does not stop the system |
| `priority-low` | Minor UI or polish issue |
| `status-todo` | Bug is recorded but not started |
| `status-in-progress` | Bug is currently being fixed |
| `status-fixed` | A fix has been added |
| `status-verified` | The fix has been tested |
| `status-done` | The issue is complete |

---

## 4. Bug Report Template

The following bug report template was used for consistent bug documentation.

```markdown
# Bug Report: [Short Bug Title]

## Summary

Briefly describe the problem.

## Related User Story

Example: US09 Same-Story Comparison

## Environment

- Browser:
- Operating System:
- Django Version:
- App Version/Commit:

## Steps to Reproduce

1. Open the relevant page.
2. Perform the action that causes the bug.
3. Observe the result.

## Expected Result

Describe what should have happened.

## Actual Result

Describe what actually happened.

## Severity

Low / Medium / High

## Priority

Low / Medium / High

## Status

Todo / In Progress / Fixed / Verified / Done

## Fix Notes

Describe how the bug was fixed.

## Verification Notes

Describe how the fix was tested.
```

---

## 5. Bugs Identified During Testing

| Bug ID | Bug Summary | Related Story | Severity | Priority | Final Status |
|---|---|---|---|---|---|
| BUG01 | Article images displayed too large on cards | US02 / US04 | Medium | Medium | Fixed |
| BUG02 | Missing article images left empty space | US02 / US04 | Medium | Medium | Fixed |
| BUG03 | Breaking news alert section looked too plain | US08 | Low | Medium | Fixed |
| BUG04 | Compare Sources visual map lines did not connect all nodes clearly | US09 | Medium | High | Fixed |
| BUG05 | Comparison Snapshot repeated similar source card information | US09 | Low | Medium | Fixed |
| BUG06 | Recommended article buttons were not aligned | US11 | Low | Medium | Fixed |
| BUG07 | Related source card buttons were not aligned | US09 | Low | Medium | Fixed |
| BUG08 | News API returned 401 Unauthorized when API key was missing or invalid | US08 / API Feature | High | High | Fixed/Handled |
| BUG09 | Test suite originally failed because `published_at` was missing in test articles | Testing | High | High | Fixed |
| BUG10 | Automated test count initially showed zero tests before `news/tests.py` was created correctly | Testing | Medium | Medium | Fixed |

---

## 6. Detailed Bug Reports

### BUG01: Article Images Displayed Too Large

| Field | Details |
|---|---|
| Summary | Article images were too large on article cards, causing the homepage layout to look unbalanced. |
| Related User Story | US02 Multi-Source News Feed, US04 Article Detail Page |
| Steps to Reproduce | Open the homepage and view article cards with images. |
| Expected Result | Images should fit neatly inside article cards. |
| Actual Result | Images appeared too large and affected the card layout. |
| Severity | Medium |
| Priority | Medium |
| Status | Fixed |
| Fix Notes | CSS was updated to control image size and make article cards more consistent. |
| Verification Notes | Homepage article cards were checked after the CSS update. |

---

### BUG02: Missing Article Images Left Empty Space

| Field | Details |
|---|---|
| Summary | Some articles did not have images, which made the card layout look incomplete. |
| Related User Story | US02 Multi-Source News Feed, US04 Article Detail Page |
| Steps to Reproduce | Open an article card where the article has no image URL. |
| Expected Result | A clean placeholder should appear when no image is available. |
| Actual Result | The image area looked empty or inconsistent. |
| Severity | Medium |
| Priority | Medium |
| Status | Fixed |
| Fix Notes | A NewsLens placeholder image area was added for missing article images. |
| Verification Notes | Articles with and without images were checked on the homepage and detail page. |

---

### BUG03: Breaking News Alert Section Looked Too Plain

| Field | Details |
|---|---|
| Summary | The breaking news section was functional but did not stand out clearly on the homepage. |
| Related User Story | US08 Breaking News Alerts |
| Steps to Reproduce | Open the homepage and view active breaking news alerts. |
| Expected Result | Breaking alerts should be visually clear and easy to notice. |
| Actual Result | Alerts appeared too plain. |
| Severity | Low |
| Priority | Medium |
| Status | Fixed |
| Fix Notes | The layout and styling of the breaking news section were improved. |
| Verification Notes | Active alerts were checked on the homepage after the design update. |

---

### BUG04: Compare Sources Visual Map Lines Did Not Connect Clearly

| Field | Details |
|---|---|
| Summary | The visual source map did not clearly connect the central article to all related source nodes. |
| Related User Story | US09 Same-Story Comparison |
| Steps to Reproduce | Open the Compare Sources page for an article with related articles. |
| Expected Result | Each related source node should appear visually connected to the selected article. |
| Actual Result | Some connector lines were not clearly aligned. |
| Severity | Medium |
| Priority | High |
| Status | Fixed |
| Fix Notes | CSS connector classes were updated so each source node had a clear connection line. |
| Verification Notes | The Compare Sources page was rechecked to confirm all source nodes were visually connected. |

---

### BUG05: Comparison Snapshot Repeated Similar Information

| Field | Details |
|---|---|
| Summary | The Comparison Snapshot section repeated information already shown in the source cards. |
| Related User Story | US09 Same-Story Comparison |
| Steps to Reproduce | Open the Compare Sources page and scroll below the source cards. |
| Expected Result | The page should provide new comparison guidance. |
| Actual Result | The snapshot section repeated similar article/source information. |
| Severity | Low |
| Priority | Medium |
| Status | Fixed |
| Fix Notes | The section was replaced with Comparison Insights, focusing on source diversity, category coverage, headline angle, and reading balance. |
| Verification Notes | The Compare Sources page was reviewed after replacing the repeated content. |

---

### BUG06: Recommended Article Buttons Were Not Aligned

| Field | Details |
|---|---|
| Summary | Buttons in recommended article cards appeared at different vertical positions. |
| Related User Story | US11 User Preferences |
| Steps to Reproduce | Log in, set preferred categories, and view recommended articles on the homepage. |
| Expected Result | Buttons should align neatly across cards. |
| Actual Result | Buttons were uneven because article text lengths varied. |
| Severity | Low |
| Priority | Medium |
| Status | Fixed |
| Fix Notes | Card CSS was updated using flex layout and automatic spacing. |
| Verification Notes | Recommended article cards were checked after the layout update. |

---

### BUG07: Related Source Card Buttons Were Not Aligned

| Field | Details |
|---|---|
| Summary | Buttons in Compare Sources related article cards were not aligned evenly. |
| Related User Story | US09 Same-Story Comparison |
| Steps to Reproduce | Open the Compare Sources page and compare related source cards. |
| Expected Result | Related source card buttons should align consistently. |
| Actual Result | Buttons appeared at different heights. |
| Severity | Low |
| Priority | Medium |
| Status | Fixed |
| Fix Notes | CSS was updated to give related cards consistent height and push actions to the bottom. |
| Verification Notes | Related source cards were checked after the fix. |

---

### BUG08: News API 401 Unauthorized Error

| Field | Details |
|---|---|
| Summary | News API fetching returned 401 Unauthorized when the API key was missing or invalid. |
| Related User Story | US08 Breaking News Alerts / API Feature |
| Steps to Reproduce | Run the news fetch command without a valid `NEWS_API_KEY`. |
| Expected Result | The system should fetch news when a valid key is configured or fail safely when the key is invalid. |
| Actual Result | The API returned 401 Unauthorized and no articles were added. |
| Severity | High |
| Priority | High |
| Status | Fixed/Handled |
| Fix Notes | The API key was moved into `.env`, and the fetch command handled failed API responses without crashing the app. |
| Verification Notes | The command was tested again after adding the API key. Mock object tests were also added to test API behaviour safely. |

---

### BUG09: Tests Failed Because `published_at` Was Missing

| Field | Details |
|---|---|
| Summary | The automated tests failed because test articles were created without the required `published_at` field. |
| Related User Story | Testing |
| Steps to Reproduce | Run `python manage.py test news` after creating initial tests. |
| Expected Result | Test articles should be created successfully. |
| Actual Result | Tests failed with `NOT NULL constraint failed: news_article.published_at`. |
| Severity | High |
| Priority | High |
| Status | Fixed |
| Fix Notes | `published_at=timezone.now()` was added to all test article records. |
| Verification Notes | Tests were rerun and passed successfully. |

---

### BUG10: Django Initially Found Zero Tests

| Field | Details |
|---|---|
| Summary | Django initially reported zero tests because the test file had not been created or detected correctly. |
| Related User Story | Testing |
| Steps to Reproduce | Run `python manage.py test` before creating `news/tests.py` correctly. |
| Expected Result | Django should discover the automated test cases. |
| Actual Result | Django found zero tests. |
| Severity | Medium |
| Priority | Medium |
| Status | Fixed |
| Fix Notes | `news/tests.py` was created correctly and the test class was added. |
| Verification Notes | Django later discovered and ran 23 tests successfully. |

---

## 7. Final Automated Test Evidence

The automated test suite was run after fixing the test setup and adding mock object tests.

```text
Ran 23 tests in 7.379s

OK
Destroying test database for alias 'default'...
```

This shows that the automated test suite passed successfully.

---

## 8. System Testing Plan for Week 10 Demonstration

System testing was planned to check NewsLens as a complete working application from the user’s point of view. The purpose was to make sure the main features worked together before the final demonstration.

---

## 9. System Test Cases

| Test ID | Feature | Test Steps | Expected Result | Status |
|---|---|---|---|---|
| ST01 | Homepage | Open the homepage | Latest articles, categories, and alerts are displayed | Pass |
| ST02 | Category Browsing | Click a category link | Only articles from that category appear | Pass |
| ST03 | Search | Search for an article keyword | Matching articles are displayed | Pass |
| ST04 | Article Detail | Open an article | Title, source, category, summary, description, content preview, and original link appear | Pass |
| ST05 | Quick Summary | Open article cards/detail page | Quick summaries are displayed | Pass |
| ST06 | User Registration | Register a new account | User account is created and user can log in | Pass |
| ST07 | Login/Logout | Log in and log out | Authentication works correctly | Pass |
| ST08 | Save Article | Log in and save an article | Article is added to saved articles | Pass |
| ST09 | Remove Saved Article | Remove a saved article | Article is removed from saved list | Pass |
| ST10 | Breaking Alerts | Create active and inactive alerts | Only active alerts appear on homepage | Pass |
| ST11 | Compare Sources | Click Compare Sources on article detail page | Compare Sources page loads with main article and related cards | Pass |
| ST12 | Bias Insight | Open article detail page | Bias and balance insight panel appears | Pass |
| ST13 | User Preferences | Select preferred categories | Recommended articles appear on homepage | Pass |
| ST14 | Admin Dashboard | Open dashboard as staff user | Admin statistics and management summary appear | Pass |
| ST15 | Admin Restriction | Open dashboard as normal user | Normal user cannot access staff dashboard | Pass |
| ST16 | News API Fetch | Run fetch command with API key | Articles are fetched and saved safely | Pass |
| ST17 | Mock API Test | Run automated mock API test | Article is created from fake API response | Pass |
| ST18 | Responsive Layout | Resize browser/window | Layout remains readable on smaller screens | Pass |
| ST19 | Missing Images | Open article with no image | Placeholder image area appears | Pass |
| ST20 | Navigation Links | Click main navigation links | Pages open correctly | Pass |

---

## 10. Acceptance Testing Summary

The system testing plan also acted as acceptance testing because each test was based on user-visible behaviour.

| User Story | Acceptance Evidence |
|---|---|
| US01 User Account Access | Register, login, and logout tested |
| US02 Multi-Source News Feed | Homepage displays article feed |
| US03 News Categories | Category pages filter articles |
| US04 Article Detail Page | Article details and original source link shown |
| US05 Search News | Search returns matching articles |
| US06 Quick Article Summary | Summary appears on cards and detail pages |
| US07 Save Articles | Logged-in users can save and remove articles |
| US08 Breaking News Alerts | Active alerts appear on homepage |
| US09 Same-Story Comparison | Compare Sources page shows related coverage |
| US10 Bias and Balance Insights | Bias panel appears on article detail page |
| US11 User Preferences | Preferred categories affect recommendations |
| US12 Admin Management | Staff dashboard and Django admin support management |

---

## 11. Testing Reflection

Practical 9 showed that testing is not only about checking whether individual functions work. It is also about checking whether the full application works from the user’s point of view.

The bug tracking process helped record problems clearly and made fixes easier to explain. For example, the missing image issue, Compare Sources visual map issue, and button alignment issue were all usability bugs. They did not stop the whole system from working, but they affected the quality of the user experience.

The automated test suite was also useful because it confirmed that important features still worked after changes. The final result of 23 passing tests gave stronger evidence that the system was stable before the final demonstration.

---

## 12. Practical 9 Summary

Practical 9 focused on bug tracking, bug reporting, and system testing. GitHub Issues and labels were used to describe how bugs were managed. Several real bugs from the NewsLens project were documented with summaries, steps to reproduce, expected results, actual results, fixes, and verification notes.

A system testing plan was also prepared for the Week 10 demonstration. The final automated test evidence showed that **23 tests passed successfully**, including mock object tests for the News API feature.