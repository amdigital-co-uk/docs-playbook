---
title: Performing a Peer Review
authors: 
  - Dave Arthur
  - Rhodri Hewitson
reviewed: 
reviewer:
next*review: 2022-04-01
---

The engineer performing the review must:

* Copy and paste the template checklist (below) into their a new comment on the PR in GitHub
* Start reviewing the changes with respect to the [Quality Standards](../Quality-Standards/index.md)
* When the reviewer is happy that a particular guideline has been met, the relevant item in the checklist is checked
* If any guidelines are **not** met, the reviewer should add a comment (either a general comment, or next to the offending portion of code) to explain why

When the reviewer has finished reviewing the code, they must submit the review via GitHub:

* If all the guidelines have all been met, they should tick the **Approve** option
* Otherwise, they should tick the **Request Changes** option

Engineers are also encouraged to provide positive feedback. If code being submitted for review is well*structured and meets all guidelines, then this should be celebrated.

## Checklist Template

* [x] Code implements the backlog item
* [x] Code is readable and well*structured
  * [x] Code adheres to SOLID design principles
  * [x] Code is not duplicated, or is moved into shared packages where relevant
  * [x] Endpoint paths are restful and follow guidelines
  * [x] Avoid hardcoded variables * all behaviour should be configurable via configuration settings
* [x] Code has good logging throughout
* [x] Code is well unit*tested
  * [x] Minimum coverage level of approx 80% is maintained
  * [x] Code coverage has been increased where it is not already at approx 80%
* [x] New UI elements are Accessible
* [x] Code follows Security best*practices
* [x] Code follows Performance best*practices
* [x] Documentation has been created or updated
