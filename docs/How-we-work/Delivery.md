---
title: Delivery
authors:
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

Delivery is how an objective becomes a stream of small, safe releases. We break work down the same way everywhere so that plans, estimates and progress line up from the roadmap to the individual task.

## Work breakdown

<figure markdown style="width: 100%; max-width: 560px;">
--8<-- "docs/assets/images/work-breakdown.svg"
</figure>

**Objective.** A committed roadmap item of about three months or less. See [Roadmap and objectives](Roadmap-and-Objectives.md).

**Outcome.** A measurable result the objective must deliver, described as impact rather than output. Outcomes are the unit we plan and report against, and carry target dates.

**Feature.** A tangible unit of value a non-technical stakeholder can understand. Features define what is in and out of scope, the behavioural requirements and quality attributes, and the dependencies, assumptions and risks. They carry target dates. A feature is not always user-facing; it may be a reliability, security or maintenance improvement.

**Design.** A work item for low-level design activity on a feature: technical, user experience or product design that needs planning and tracking in its own right.

**Backlog item.** An independently deployable, testable piece of work that does no damage on its own, even if it is not independently valuable. Typically it touches one repository. Its specification is written as scenarios.

**Bug.** A defect found in production, linked to the feature whose behaviour it breaks. Defects found before release are fixed within the work in progress.

**Task.** A discrete piece of work towards a backlog item: development, testing, design, documentation. Effort is recorded here.

The roadmap and our work tracker mirror each other at the objective and outcome levels. The roadmap carries the plan; the tracker carries the execution.

## Just in time

We design and create work items only when they are needed. Items in Later exist only as objectives and outcomes. Features are designed in time to give planning clarity, and backlog items are created only once their feature is ready and prioritised for near-term delivery. Creating backlog items for future objectives is premature design, and it causes confusion when scope changes. Teams keep a few weeks of ready work ahead of them, so that design never blocks delivery.

## Ready and done

A **feature is ready** when the team can explain the value it delivers, understands its scope, has identified the artefacts it needs, and agrees the work can be decomposed into independently deployable backlog items. Some artefacts are always required: requirements, estimates, and a test plan derived from the design. Others are produced as needed: architecture designs, decision records, an accessibility impact assessment, a risk log, user experience specifications. Decision records that the feature depends on, each carrying its security and reliability impact assessment, are accepted before it starts.

A **feature is done** when its artefacts have been reviewed and all its backlog items are complete. It has been released, or a dated release has been planned and communicated. Its release notes and user guide exist.

Backlog item design is decomposition, not a second requirements exercise. If a genuine requirements gap appears while breaking a feature down, it goes back to the Product Owner.

## Small increments, low work in progress

We deliver in thin slices. Small changes are easier to reason about, review, test and roll back, and they reach users sooner. Teams limit work in progress and finish features before starting new ones. Cadence is the team's choice: most run a two-week iteration with regular design and refinement sessions, and every team writes down its own working agreements.

## Estimation

A **rough order of magnitude** (ROM) is an early indication of scale, given before a solution is designed, with its assumptions stated. An **estimate** is tied to a defined scope and carries real confidence. We keep the words apart on purpose: "No, we haven't estimated this yet, but there is a ROM."

ROMs support planning and prioritisation only. They are not targets or commitments. Estimates sharpen as work gets nearer: near-term work has committed timelines based on high-confidence estimates, medium-term work is detailed and confident, and long-term work has a ROM with its uncertainty made clear. When child items are estimated, their parent's estimate is updated. Outcomes and features are sized on agreed scales; teams choose their own scale for backlog items.

## Risks, assumptions, issues and dependencies

Every team keeps a live record of its risks, assumptions, issues and dependencies, captured as they emerge rather than at set points, each with an owner. They are reviewed in the team's planning sessions and escalated when they threaten an outcome.

## Recording effort

We record the hours spent on tasks before a backlog item is closed. The record tells the business where its investment went, which it needs for financial reporting. It tells us how our estimates compare with reality, so they improve. It shows the true cost of support work. It is never used to judge individuals.
