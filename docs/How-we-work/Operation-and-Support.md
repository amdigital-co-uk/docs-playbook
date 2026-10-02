---
title: Operation and support
authors:
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

Releasing is not the end. We run what we build, support the people who use it, and measure whether it did what we said it would.

## One front door

Every issue, from a customer or from a colleague, comes in through Customer Support. They triage it, set its priority, keep the person who raised it informed, and decide what engineers work on next. Nobody brings an issue straight to an engineer, and nobody asks an engineer for a status update; both slow everything down. The one exception is a suspected critical incident, which colleagues raise immediately in the dedicated incident channel in Teams as well as logging it in the usual way.

## Three lines of support

**First line** is Customer Support. They investigate and resolve common issues using the knowledgebase, the known error log and a map of who knows what.

**Second line** is an engineer on rotation, working one issue at a time from the top of a prioritised list until it is resolved, blocked or escalated. Each week a shadow lead software engineer and a shadow test engineer support them: a sounding board, a second opinion, and someone to validate the fix before it ships. Shadowing is shared across all our lead and test engineers.

**Third line** is every delivery team. Each team reserves capacity for support, takes the highest-priority issue it is equipped to resolve, and delivers the fix through its normal backlog. Support is part of every team's work, not a separate team's.

## Priority

Priority comes from impact and urgency. Impact depends on how important the affected service is to the business; urgency on how soon it must be fixed, from a live sales opportunity blocked to a workaround that is merely inconvenient. The two combine into P1 to P4. Within a priority, Customer Support decides the order, using a shared scorecard so the reasoning can be explained.

A **P1** is an outage or major degradation of a critical service. When one is declared it becomes the department's only priority, and other work stops until the issue is contained. A coordinator runs the response. Stakeholders hear within fifteen minutes and then at least hourly. The incident ends with a root cause analysis within five working days and a lessons-learned session with tracked actions.

## Known errors

Not every issue is fixed straight away. When an issue is understood but the right choice is to leave it for now, because a workaround exists, the impact is low, or a planned change will remove it, it goes on the known error log with its impact, workaround, the reason and who decided. Known errors are conscious decisions, reviewed regularly and closed when they no longer apply. The log is never a place to park things we do not understand.

## Support feeds planning

Every resolved issue is given a root cause category: a logic error, a regression, a capacity limit, a configuration mistake, a monitoring gap, an issue in the customer's own environment. Trends in those categories shape objectives, the [regression testing policy](../Quality/Testing.md) and our monitoring. A rise in regressions is a signal we act on, not a statistic.

## Measuring outcomes

Each outcome has measures agreed before release: usage, performance, feedback, or whatever tells us the problem is solved. After release the team puts the measures in place, plans time to review them, and reports the result to stakeholders, including when the result is not what we hoped. That evidence closes the loop back into discovery.

## Learning

After a major milestone, a release or an incident, the team runs a review of what happened and what it will do differently, with actions and owners. We call these after action reviews rather than post-mortems because the point is learning, not blame.
