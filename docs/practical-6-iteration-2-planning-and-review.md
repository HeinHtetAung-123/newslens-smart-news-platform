# Practical 6: Iteration 2 Planning, Tracking, and Review

## 1. Practical Objective

The objective of Practical 6 was to use the actual results from Iteration 1 to plan and monitor Iteration 2. This included using the Iteration 1 velocity, updating the backlog, creating an Iteration 2 plan, tracking Iteration 2 progress, reviewing completed and unfinished work, and preparing GitHub Pages evidence for the completed Iteration 2 user stories.

Iteration 2 focused on improving the usefulness of NewsLens by adding article summaries, saved articles, and breaking news alerts.

---

## 2. Iteration 1 Velocity Used for Planning

In Practical 5, the actual velocity for Iteration 1 was calculated.

| Iteration | Planned Work | Completed Work | Actual Velocity |
|---|---:|---:|---:|
| Iteration 1 | 15 days | 15 days | 15 days |

The Iteration 1 velocity was **15 estimated days**.

This meant that Iteration 2 should not exceed approximately 15 estimated days of planned work. Since NewsLens is a solo project, this helped keep the next iteration realistic.

---

## 3. Iteration 1 Burn-down Review

The Iteration 1 burn-down chart was reviewed before starting Iteration 2.

| Day | Planned Work Remaining | Actual Work Remaining |
|---:|---:|---:|
| 0 | 15 | 15 |
| 1 | 14 | 15 |
| 2 | 13 | 14 |
| 3 | 12 | 12 |
| 4 | 11 | 12 |
| 5 | 10 | 10 |
| 6 | 9 | 9 |
| 7 | 8 | 8 |
| 8 | 7 | 8 |
| 9 | 6 | 6 |
| 10 | 5 | 5 |
| 11 | 4 | 4 |
| 12 | 3 | 3 |
| 13 | 2 | 2 |
| 14 | 1 | 1 |
| 15 | 0 | 0 |

## 4. Iteration 1 Burn-down Interpretation

The Iteration 1 burn-down showed small delays at the beginning and middle of the iteration, but the work returned to the planned line and reached zero by the final day. This means the selected stories were manageable and the estimates were mostly accurate.

Because Iteration 1 reached zero remaining work, no unfinished Iteration 1 stories needed to be moved into Iteration 2.

---

## 5. Backlog Update After Iteration 1

After Iteration 1, the following user stories were completed:

| ID | User Story | Status |
|---|---|---|
| US01 | User Account Access | Completed |
| US02 | Multi-Source News Feed | Completed |
| US03 | News Categories | Completed |
| US04 | Article Detail Page | Completed |
| US05 | Search News | Completed |

The remaining backlog after Iteration 1 was:

| ID | User Story | Priority | Estimate | Planned Iteration |
|---|---|---:|---:|---|
| US06 | Quick Article Summary | 20 | 4 days | Iteration 2 |
| US07 | Save Articles | 20 | 3 days | Iteration 2 |
| US08 | Breaking News Alerts | 30 | 3 days | Iteration 2 |
| US09 | Same-Story Comparison | 30 | 5 days | Iteration 3 |
| US10 | Bias and Balance Insights | 40 | 5 days | Iteration 3 |
| US11 | User Preferences | 40 | 3 days | Iteration 3 |
| US12 | Admin Management | 50 | 4 days | Iteration 3 |

---

## 6. Iteration 2 User Stories Selected

Based on the Iteration 1 velocity of 15 days, the following stories were selected for Iteration 2.

| ID | User Story | Priority | Estimate | Reason Selected |
|---|---|---:|---:|---|
| US06 | Quick Article Summary | 20 | 4 days | Improves article readability |
| US07 | Save Articles | 20 | 3 days | Adds personal user functionality |
| US08 | Breaking News Alerts | 30 | 3 days | Highlights urgent news |

Total planned Iteration 2 estimate: **10 days**

The total planned work for Iteration 2 was 10 estimated days, which was below the Iteration 1 velocity of 15 days. This gave room for UI improvements, testing, and small fixes.

---

## 7. Iteration 2 Task Breakdown

### US06: Quick Article Summary

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T23 | Create summary helper function | 1 day | Done |
| T24 | Add `get_quick_summary()` method to Article model | 0.75 day | Done |
| T25 | Display quick summary on article cards | 0.75 day | Done |
| T26 | Display quick summary on article detail page | 0.75 day | Done |
| T27 | Test summary fallback when summary text is missing | 0.75 day | Done |

Total: **4 days**

### US07: Save Articles

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T28 | Create SavedArticle model | 0.75 day | Done |
| T29 | Add save article view | 0.75 day | Done |
| T30 | Add remove saved article view | 0.5 day | Done |
| T31 | Create saved articles page | 0.75 day | Done |
| T32 | Test saving/removing articles while logged in | 0.25 day | Done |

Total: **3 days**

### US08: Breaking News Alerts

| Task ID | Task | Estimate | Status |
|---|---|---:|---|
| T33 | Create BreakingNewsAlert model | 0.75 day | Done |
| T34 | Register alerts in Django admin | 0.25 day | Done |
| T35 | Display active alerts on homepage | 0.75 day | Done |
| T36 | Improve breaking news alert layout | 0.75 day | Done |
| T37 | Test active/inactive alert display | 0.5 day | Done |

Total: **3 days**

---

## 8. Iteration 2 Burn-down Chart Data

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

## 9. Iteration 2 Burn-down Interpretation

The Iteration 2 burn-down showed a small delay early in the iteration because the save article feature needed authentication checks and template changes. However, the work returned to the expected path and reached zero by the end of the iteration.

The final result was successful because all planned Iteration 2 user stories were completed.

---

## 10. Completed and Unfinished Stories

### Completed Stories

| ID | User Story | Estimate | Status |
|---|---|---:|---|
| US06 | Quick Article Summary | 4 days | Completed |
| US07 | Save Articles | 3 days | Completed |
| US08 | Breaking News Alerts | 3 days | Completed |

Total completed work: **10 days**

### Unfinished Stories

| ID | User Story | Status |
|---|---|---|
| None | No Iteration 2 stories unfinished | Not applicable |

All Iteration 2 stories were completed. No planned story needed to be moved to Iteration 3.

---

## 11. Iteration 2 Actual Velocity

```text
Actual Velocity = Completed Estimate
Actual Velocity = 10 days