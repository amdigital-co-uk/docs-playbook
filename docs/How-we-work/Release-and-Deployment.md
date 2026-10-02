---
title: Release and deployment
authors:
  - Dave Arthur
  - Helen Duriez
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

We deploy often and release deliberately. Keeping the two apart is what lets us do both safely.

## Deployments and releases

A **deployment** is any change to a production system. Most deployments do not affect users: a small step towards a releasable capability, a fix behind the scenes, an infrastructure change. A **release** is a change that affects one or more groups of users. Releases usually happen after deployment, by switching functionality on through configuration (a feature flag). Enabling the same change for another group of users later is a separate release.

Our aim is continuous deployment: small changes, deployed automatically and frequently, with as little manual involvement as possible.

## The deployment log

Every production change is recorded in the deployment log: what changed, when, and who was involved; ideally also why and what tests were run. Where deployment is automated the log entry can be too, though a higher-risk deployment still needs an entry added in advance. The log is our change history. It is how we trace the cause of an issue quickly, tell other teams about changes that might affect them, and report on how often we change things.

Notice is proportional to risk. A low-risk deployment, with no expected downtime, low complexity and no cross-team dependency, needs no advance notice, though it is welcome. A higher-risk deployment is one that could cause downtime on a critical or high-tier service, interfere with another team's work, or has a real chance of failure. It states its expected impact, gives notice in advance, keeps stakeholders updated as it happens, and actively seeks their feedback rather than waiting for it.

| Deployment | Minimum notice |
|---|---|
| Critical or urgent fix during an incident | 20 minutes, with stakeholders told directly |
| Short downtime, under 15 minutes | 24 hours |
| Downtime of 15 minutes or more | One week |

## Planning a release

Release planning begins during detailed design. Each release is recorded on the release dashboard, first as speculative, then planned, then completed. A release record says what value is being released, which systems are affected, what functionality is changing, which user groups receive it, the expected and actual dates, and links to the user guides it changes. Staff subscribe to the releases they care about.

Communication is both push and pull: we tell stakeholders what they need to know as soon as we know it, and they can find the current state whenever they want it without asking.

## Release plans

Any release that is not fully automated has a release plan, reviewed by a senior engineer who did not write it. The plan names the stakeholders to communicate with, the risks, the steps, the smoke tests that will confirm success, and how to roll back. For a simple, low-risk release from a single repository, the plan lives in the pull request. Higher-risk releases, or ones that deploy several components together, use the full template.

Fully automated releases need no separate plan: the pull request, pipeline logs and source control history are the record, and they satisfy our compliance obligations.

## Telling people

A good release message says what changed and where, why, what users will see (and whether it is behind a flag), any action users must take, such as republishing or clearing a cache, and, for a fix, which support issue it resolves. Write it for someone who did not know the change was coming.

## After the release

The as-is outcome specification becomes the user guide. Through the release dashboard and the user guide, Customer Support can see what changed before users start asking. End-to-end and smoke tests run against the live system; if they find a defect, we roll back or raise a bug according to the risk. Then we [measure whether the outcome landed](Operation-and-Support.md).
