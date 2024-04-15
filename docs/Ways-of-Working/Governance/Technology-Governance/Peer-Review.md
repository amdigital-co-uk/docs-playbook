---
title: Peer Review
---

## Objective

Every change to a production system must be reviewed by someone other than the person who implemented that change, and evidence must be retained that this review has been performed.

Reviews, at a minimum, must look to identify critical quality and security flaws, but also serve to reduce knowledge silos and create better solutions.

## Requirements

All code repositories must be configured to enforce peer review, by protecting branches used for production deployments (e.g. requiring pull requests).

Where code changes are not available, for example when infrastructure is not coded, the changes must be documented in a [deployment log](Deployment-Logs.md), and a reviewer must digitally sign the document (or provide an tracked update) following their review.

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
| Engineering Owner | Is **responsible** for ensuring that peer review mechanisms are in place and meet the stated requirements, and is **accountable** for the continued adherence to these mechanisms |