# Practical 7: Test-Driven Development and Automated Testing

## 1. Practical Objective

The objective of Practical 7 was to apply Test-Driven Development (TDD) to the NewsLens project. This practical required selecting at least five user stories, planning at least three test cases for each story, and implementing at least fifteen automated tests.

The selected user stories were chosen from the completed NewsLens features because they represent important user-facing functionality and system behaviour.

---

## 2. TDD Approach Used

Test-Driven Development was used as the testing approach for this practical. The TDD cycle used was:

1. Write a test for the required behaviour.
2. Run the test and confirm that it fails.
3. Write the simplest production code needed to pass the test.
4. Run the test again and confirm that it passes.
5. Refactor the code if needed while keeping the tests passing.

For NewsLens, the automated tests were written using Django’s built-in `TestCase` and test client. This allowed the project to test models, views, page responses, authentication behaviour, saved articles, search, summaries, breaking news alerts, and comparison pages.

---

## 3. Selected User Stories for Testing

| ID | User Story | Reason Selected |
|---|---|---|
| US02 | Multi-Source News Feed | Core homepage functionality |
| US03 | News Categories | Important browsing feature |
| US05 | Search News | Important user interaction |
| US06 | Quick Article Summary | Core readability feature |
| US07 | Save Articles | Personal logged-in user feature |
| US08 | Breaking News Alerts | Homepage alert feature |
| US09 | Same-Story Comparison | Iteration 3 comparison feature |

Although the minimum requirement was five user stories, seven user stories were selected to provide stronger test coverage.

---

## 4. Planned Test Cases

### US02: Multi-Source News Feed

| Test Case | Description | Expected Result |
|---|---|---|
| TC02.1 | Load homepage | Homepage returns status code 200 |
| TC02.2 | Display article title | Homepage contains article title |
| TC02.3 | Display article source/category | Homepage shows source and category information |

### US03: News Categories

| Test Case | Description | Expected Result |
|---|---|---|
| TC03.1 | Open category page | Category page returns status code 200 |
| TC03.2 | Filter by category | Category page shows matching category articles |
| TC03.3 | Exclude other categories | Category page does not show unrelated category articles |

### US05: Search News

| Test Case | Description | Expected Result |
|---|---|---|
| TC05.1 | Search by title | Matching article appears |
| TC05.2 | Search by source | Matching source article appears |
| TC05.3 | Search with no match | Page still loads and shows no matching article |

### US06: Quick Article Summary

| Test Case | Description | Expected Result |
|---|---|---|
| TC06.1 | Article has summary | Summary is returned |
| TC06.2 | Article has no summary but has description | Description fallback is used |
| TC06.3 | Article has no text | Default unavailable message is returned |

### US07: Save Articles

| Test Case | Description | Expected Result |
|---|---|---|
| TC07.1 | Anonymous user tries to save | User is redirected to login |
| TC07.2 | Logged-in user saves article | SavedArticle record is created |
| TC07.3 | Logged-in user removes saved article | SavedArticle record is deleted |

### US08: Breaking News Alerts

| Test Case | Description | Expected Result |
|---|---|---|
| TC08.1 | Active alert exists | Homepage displays active alert |
| TC08.2 | Inactive alert exists | Homepage does not display inactive alert |
| TC08.3 | Alert links to article | Alert article title/link is available |

### US09: Same-Story Comparison

| Test Case | Description | Expected Result |
|---|---|---|
| TC09.1 | Open compare page | Compare page returns status code 200 |
| TC09.2 | Show selected article | Main article appears on comparison page |
| TC09.3 | Show related articles | Related category articles appear |

---

## 5. Automated Test Implementation

The automated tests were implemented in:

```text
news/tests.py