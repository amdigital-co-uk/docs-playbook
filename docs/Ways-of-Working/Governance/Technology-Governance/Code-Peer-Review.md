---
title: Implementation Peer Review
---

## Objective

Implementation Peer Reviews ensure that changes to production system meet required quality, security and reliability standards and is aligned with the technical design of the solution.  


## Implementation Peer Review

Every change to a production system must be reviewed at least one additional engineer, other than the person who implemented that change. Evidence must be retained that this review has been performed. 

Reviews, at a minimum, must look to identify quality, security, and reliability flaws, but also serve to reduce knowledge silos and provide a platform to constructively challenge one another and ultimately create better solutions.

Changes to production systems will usually involve code changes, and the review will usually occur before the code changes are merged into the main branch, via a pull request.

However, not all production systems are managed via code. For example, some infrastructure may not be managed via [IAC](https://en.wikipedia.org/wiki/Infrastructure_as_code){ target=default }. Such **"uncoded" changes to production systems are not exempt**, and different techniques may be required for uncoded production system changes.

!!! Info "Types of Peer Review"
    Peer reviews are used in many settings, for example during [Architectural Design](Architectural-Design.md#peer-review), and the [Technical Validation Review](Technical-Validation-Review.md#objective). 

## Requirements

All code repositories must be configured to enforce peer review, by protecting branches used for production deployments (e.g. requiring pull requests).

Where code changes are not available, for example when infrastructure is not coded, the changes must be documented in a [deployment log](Deployment-Logs.md), and a reviewer must digitally sign the document (or provide a tracked update) following their review.

A reviewer may provide feedback and request clarification, or request amends to the change. A peer review will remain active until all feedback or requested amends have been satisfied.

Reviews must include:

- Date of review
- Reviewer name
- Comments / feedback / requested amends
- Log of remediation taken

## Responsibilities

| Owner | Responsibility |
| - | - |
| Delivery Team     | Are **responsible** for ensuring that all changes are reviewed effectively. |
| Engineering Owner | Is **responsible** for ensuring that peer review mechanisms are in place and meet the stated requirements, and is **accountable** for the continued adherence to these mechanisms. 
| Peer Reviewers    | Are **accountable** for the quality of their review, and **responsible** for ensuring that reviews are thorough and adhere to review guidelines. |


#### Toolkit

!!! toolkit "Toolkit"

    <!-- material/tags { include: [Implementation Peer Review] } -->