---
title: Deployment Logs
---

Every change to any production environment must be reflected in deployment logs. This includes code and infrastructure changes.

!!! note "Deployments are not releases"
    We differentiate deployments from releases. We may deploy changes to production environments many times before we make those changes available to customers or users (a release).

    ![Deployments and releases](../../assets/continuous-deployment.png) 

## Why?

- We must track changes to our platform, this is a vital part of change management
- Helps us understand the cause of issues, especially important in rapidly diagnosing and mitigating critical issues and security incidents

## Requirements
 
 **minimum**
 - What has changed - this can simply be a link to the PR or branch
 - date and time of change
 - individuals involved - performing the deployment

**ideal**
 - individuals involved - making the change
 - reason for change - can be a link to the specification, even indirectly through the PR
 - tests performed

## Responsibilities

| Owner | Responsibility |
| - | - |
| Delivery Team     | Are **responsible** for ensuring that all production changes are reflected in deployment logs. |
| Engineering Owner | Is **responsible** for ensuring that deployment log mechanisms are in place and meet the stated requirements, and is **accountable** for the continued adherence to these mechanisms |

## Techniques

Deployment logs may be automated or manual. This will depend on the maturity of the platform being deployed to. 

Automated logs may be part of CI pipelines, for example. Manual logs may be manual documentation.

!!! danger "Review regularly"
    Never assume that deployment logging is automated and functioning, or that team members know when or how to log manually. Checking that deployments are being added to logs can be done quickly and made part of regular team health checks.