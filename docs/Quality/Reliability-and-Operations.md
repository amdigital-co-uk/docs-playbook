---
title: Reliability and operations
authors:
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

A system that is correct but slow, fragile or invisible in production is not finished. Reliability is designed, built and measured by the same team that builds the features, with DevOps engineers as the specialists who make that possible.

## Designed for failure

The reliability half of the impact assessment on every architectural, design and scope decision asks four questions:

- **Load.** How does the system perform under realistic numbers of users and realistic volumes of data? We test with live-like data because problems that are invisible on a laptop are crippling at scale.
- **Failure.** When a dependency is slow or down, does the system degrade gracefully or fall over? Where do we need timeouts, retries, circuit breakers or caching?
- **Recovery.** How does the system recover from failure, and how long does that take? For critical services, what are the recovery time and recovery point we are designing to?
- **Observability.** Can we see what the system is doing? Logs with enough context to trace a request, metrics that show health and business performance, and alerts that reach someone before a customer notices.

Our service catalogue tiers services by how critical they are to the business. The tier helps decide whether a deployment counts as higher risk, and sets the priority an outage receives.

## Continuous deployment

We aim to deploy every change automatically, as soon as it is merged, with releases controlled separately through configuration. Automated deployment removes the manual steps where mistakes happen, makes rollback routine, and keeps each change small enough to understand. Infrastructure is defined as code and reviewed like code. Pipelines run the tests, measure coverage, and write the deployment log entry.

## Flow, feedback and learning

Three ideas from the DevOps movement underpin how we operate:

- **Flow.** Look at the whole system from idea to running software, find the constraint, and improve that, rather than optimising one stage while the whole gets slower.
- **Feedback.** Shorten the loops and make sure the signal is heard: a failing test in minutes rather than a defect report in weeks; an alert rather than a support ticket.
- **Learning.** Use the feedback to experiment and improve, and accept that some experiments will fail.

*The Phoenix Project* and *The DevOps Handbook* are the standard introductions.

## DevOps as enablers

DevOps engineers design and run the platform, environments, pipelines and infrastructure that every team depends on, and bring reliability, security, observability and cost thinking into design conversations early. They embed with a team for infrastructure-heavy work and consult otherwise. Operating the platform is not a separate department's problem: the team that builds a service is on the hook for how it runs.

## Learning from operation

Every resolved support issue is categorised by root cause, and the operational categories, such as capacity limits, configuration errors, change-induced failures, dependency failures and monitoring gaps, tell us where to invest. A monitoring gap is treated as a defect in its own right. Teams check periodically that deployment logging and alerting are actually working, because an automated safety net that has quietly stopped is worse than none.

## Cost and sustainability

Running cost is a quality attribute. We size infrastructure to need, review spend regularly, and prefer efficient designs because they are cheaper for the business and lighter on the planet.
