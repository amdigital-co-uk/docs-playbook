---
title: Performing a Peer Review
authors: 
  - Dave Arther
  - Rhodri Hewitson
reviewed: 
reviewer:
next-review: 01-04-2022
---

The engineer performing the review must:

* Copy and paste the template checklist (below) into their a new comment on the PR in GitHub
* Start reviewing the changes with respect to the [Quality Standards](/6.-Engineering/Quality-Standards)
* When the reviewer is happy that a particular guideline has been met, the relevant item in the checklist is checked
* If any guidelines are **not** met, the reviewer should add a comment (either a general comment, or next to the offending portion of code) to explain why

When the reviewer has finished reviewing the code, they must submit the review via GitHub:
* If all the guidelines have all been met, they should tick the **Approve** option
* Otherwise, they should tick the **Request Changes** option

Engineers are also encouraged to provide positive feedback. If code being submitted for review is well-structured and meets all guidelines, then this should be celebrated.

## Checklist Template

```
- [ ] Code implements the backlog item
- [ ] Code is readable and well-structured
    - [ ] Code adheres to SOLID design principles
    - [ ] Code is not duplicated, or is moved into shared packages where relevant
    - [ ] Endpoint paths are restful and follow guidelines
    - [ ] Avoid hardcoded variables - all behaviour should be configurable via configuration settings
- [ ] Code has good logging throughout
- [ ] Code is well unit-tested
    - [ ] Minimum coverage level of approx 80% is maintained
    - [ ] Code coverage has been increased where it is not already at approx 80%
- [ ] New UI elements are Accessible
- [ ] Code follows Security best-practices
- [ ] Code follows Performance best-practices
- [ ] Documentation has been created or updated
```
