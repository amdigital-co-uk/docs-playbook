---
title: Shared quality
authors:
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

Quality is not a stage, a team or a sign-off. It is a property of how the whole team works, from the first conversation about a problem to the way we respond when something breaks.

## Quality is everyone's

Every member of a delivery team is responsible for the quality of what the team releases: software engineers, test engineers, DevOps engineers, designers and Product Owners alike. Nobody throws work over a fence for someone else to check. Nobody waits for a specialist to tell them whether their work is secure, accessible or fast enough.

Quality also means more than "works as specified". A solution is high quality when it is valuable to the people it is for, correct, secure, private, accessible, reliable under real load, observable in operation, maintainable by the next engineer, and affordable to run. We design for all of those from the start, because retrofitting any of them costs far more.

## Design the proof with the solution

We decide how we will prove something works while we are designing it, not after we have built it. A solution design is turned into a test plan, and the two iterate together until the team can see how every behaviour and quality attribute will be shown to hold. Specifications are written as scenarios that become tests. Before we change existing behaviour we check that it is protected by tests, and if it is not, we add them first. We prefer a fast automated test at the lowest level that gives us confidence to a slow manual one at the top.

This goes further than test-first or specification-driven development. The test plan is a design output, and we think that is one of the things that makes us distinctive. See [Testing](Testing.md).

## Specialists enable, they do not gate

Test engineers, DevOps engineers, security and accessibility expertise all work *with* teams, not downstream of them. A test engineer's job is to make the team better at testing. That means leading the team in turning each design into a test plan, pairing on automation, coaching on testable specifications, running exploratory sessions, and bringing an independent eye. The same is true of DevOps engineers for reliability, pipelines and infrastructure, and of designers for accessibility. They consult, coach and build alongside; they are not a checkpoint the work has to pass through on its way out.

## How we know

We look for evidence rather than reassurance:

- the trend in support issues caused by regressions
- automated test health across our platforms, visible to everyone every day
- test coverage measured in every repository's pipeline
- root cause categories on resolved issues, and what they say about testing, monitoring and change gaps
- lessons learned after incidents, with actions that get done

When the evidence says a practice is not working, we change the practice.

## In this section

- [Testing](Testing.md): our test strategy, the regression-first rule and exploratory testing.
- [Engineering standards](Engineering-Standards.md): readable code, small changes, peer review and the bars we hold.
- [Security, privacy and accessibility](Security-Privacy-and-Accessibility.md): designed in, assessed early.
- [Reliability and operations](Reliability-and-Operations.md): performance, failure, observability and continuous deployment.
- [Decision records](Decision-Records.md): how lasting decisions are proposed, challenged and recorded.
