---
title: Testing
authors:
  - Karen Farrell
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

Testing tells us whether we built the right thing and whether we broke anything on the way. We want that answer fast, often and automatically.

## What testing is for

- Prevent defects by reviewing specifications before code exists.
- Find defects in what we build before users do.
- Show that the solution does what stakeholders need and is fit for purpose.
- Give the team, and the business, justified confidence in each release.

## The test plan is a design output

We turn the solution design into a test plan, then iterate on both. As a feature is designed, the team asks how each behaviour and quality attribute will be proved, and the answer becomes the test plan: which scenarios matter, which will be automated and at what level, what test data is needed, how exploratory testing will be used, and what "done" looks like for testing. The test engineer leads this with the whole team taking part. The plan is a required artefact before a feature is ready, and it is never written in hindsight once the code exists. A behaviour that cannot be tested is a design flaw, and design is where it is cheapest to fix.

In a long programme the plan is thorough and settled before implementation. In a short, continuously discovered objective it is lighter and changes more often. The principle does not change. Specifications for backlog items are written as scenarios, in Given, When, Then form, so that the specification and the test are the same thing.

## The pyramid

| Level | What it checks | Who |
|---|---|---|
| Unit | Individual components in isolation | Delivery team |
| Integration or container | Components and services working together | Delivery team |
| System and end to end | The whole system behaving as specified, across supported browsers and devices | Delivery team |
| Business acceptance | Fitness for real-world use, in a live-like environment | Stakeholders, supported by the team |

Automation is the default at every level. Put each test at the lowest level that gives the same confidence; do not reach for a slow end-to-end test when a container test would do. Manual testing is for what cannot sensibly be automated and for deliberate exploration.

## Regression coverage comes first

Regressions have been a rising cause of support issues, and they are the most avoidable. So every piece of work on existing behaviour, whether a feature or a support fix, starts with a review of the automated coverage around the area being changed. Where it is thin, the team adds regression tests **before** making the change.

- The tests capture current behaviour; they do not fix it. Behaviour that looks wrong is raised and recorded, not silently corrected.
- They sit at the right level of the pyramid, usually container or system.
- Software and test engineers pair on them. This is shared engineering work, delegated to neither role.
- They land in their own commit and pull request, so the improvement ships quickly and is not tied to a long-lived branch.
- Exceptions are a hotfix during a live incident (the follow-up work adds the coverage), code that is being deleted, and time-boxed spikes.

When a work item is closed, the team records what testing was performed and what regression coverage was added beyond the immediate change.

## Coverage

Repositories measure and report test coverage in their pipeline and fail the build below an agreed threshold. We aim for around 80% branch coverage. Legacy repositories below the bar raise it with every change; repositories above it never let new code lower it. Coverage is a floor, not a goal: it tells us where tests are missing, not that the tests we have are good.

## Exploratory testing

Scripted testing executes known steps and should be automated. Exploratory testing is a thinking activity: designing and running tests at the same time, following curiosity within a mission. We run it as a time-boxed session of about ninety minutes, ideally in pairs, without interruptions, against a short charter that says what we are exploring, how, and what kinds of problem we expect. We record what was covered and what was found, and debrief on what further testing is needed. Pairing and recording offset the two weaknesses of the approach: it depends on domain knowledge, and findings can be hard to reproduce.

## Other kinds of test

**Static testing** reviews specifications and designs without running anything. **Confirmation testing** re-runs a failed test after a fix. **Smoke tests** are quick checks that the major features work after a build or release. **Business acceptance testing** is where stakeholders confirm the software handles their real tasks.

## Defects

A defect found before release is fixed within the work in progress. A defect found in production is a bug, linked to the feature it breaks and prioritised through the service desk. Every defect records the data used, the steps to reproduce it, expected and actual results, and evidence where possible.

## Visibility

Automated suites run on a schedule across all our platforms, nightly in our primary browser and weekly across every supported browser, with accessibility checks alongside. Results feed one dashboard everyone can see. A flaky test is a defect in the test and gets fixed, not ignored. A skipped test carries the reason in its title and is fixed within a couple of iterations; a test may be skipped temporarily, but never silently.

## After release

End-to-end and smoke tests run against the live system after every release. If they find a defect, the team rolls back or raises a bug depending on the risk.
