---
title: Release Plans
authors: 
- Ed Earle
reviewed: 
reviewer:
next-review: 2023-06-01
---

Every change to any production environment must have a release plan. This includes code and infrastructure changes.

## Why?

- We must track changes to our platform, this is a vital part of change management
- Helps us understand the cause of issues, especially important in rapidly diagnosing and mitigating critical issues and security incidents
- Creating a release plan helps to ensure we think about the impact it will have so we can reduce risk

## How to create a Release Plan

Different types of release will require different release plans. Each platform should have a document outlining the release process in the [knowledgebase](https://knowledgebase.platformdev.amdigital.co.uk/Platforms/).

### Understanding Risk

Risk is introduced in a number of ways. Attempts should be made to reduce risk by mitigating them ahead of time.

None the less, increased complexity (e.g. many release steps, multiple components/repositories effected), changes to infrastructure, or changes to critical components introduces has inherent risk.

Small incremental releases will reduce risk.

!!! Important
    Release plans must be reviewed by other team members **unless they are deemed low risk**.

    **Low-risk releases can be self-signed by the engineer performing the release**

    If there is any doubt, seek a review.

## Reviewing a Release Plan

Follow the [release plan review guidelines](../Engineering/Peer-Reviewing/Release-Plan-Review.md)
