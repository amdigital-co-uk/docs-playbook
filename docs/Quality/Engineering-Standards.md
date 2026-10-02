---
title: Engineering standards
authors:
  - Dave Arthur
  - Rhodri Hewitson
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

These are the standards every engineer, software or test, holds their own work to and looks for in a peer's. The detailed conventions for each language and platform live in the Knowledgebase and are linked from each repository.

## Principles

- Code is easy to read and understand. Names carry intent; methods and classes stay small; code explains itself without comments.
- Object-oriented code follows SOLID principles. Shared logic lives in one place, scoped to where it is needed.
- Nothing is hard-coded that should be configured. Nothing commented out is committed.
- Test coverage is maintained or improved with every change. See [Testing](Testing.md).
- Services log useful events with enough context to diagnose a problem: which customer, which asset, what action.
- Every repository has a README that explains its purpose, dependencies, build steps and anything unusual about it.
- User interfaces conform to WCAG AA. See [Security, privacy and accessibility](Security-Privacy-and-Accessibility.md).
- Code follows secure coding practice and never contains secrets.
- Code performs acceptably with live-like data and load, and is tested that way.
- Dependencies are pinned to exact versions and kept up to date.
- Shortcuts and technical debt are written down, with a plan to remove them.
- Code is green: efficient with the compute, storage and network it uses.

## Small changes

Small changes are easier to review, test, reason about and undo. We work in thin slices, commit often, and open pull requests little and often rather than in one large batch. Refactoring that prepares for a change is submitted separately from the change itself.

Our guardrail is that a change normally touches fewer than ten files and fewer than two hundred lines. The numbers are a proxy for risk, not a rule. Crossing them is a prompt to pause and talk: can the work be split, and if not, does the reviewer need more time or more testing? A large rename is low risk; a large feature is not. Treating a guardrail as a hard limit gets it gamed or ignored, and either way it stops working.

Commit messages follow the conventional commits format, so that history is readable and tooling can act on it.

## Peer review

Every change to a production system is reviewed by at least one engineer other than the person who made it, and the evidence is retained. Branches that deploy to production are protected so that this cannot be skipped. Changes to systems that are not managed as code are not exempt: they are recorded in the deployment log and signed off there.

A pull request should never be the first time the reviewer sees the work. Pair programming, screen-share walkthroughs and reviewing a work branch all give earlier feedback with more context. Code written while pairing is still reviewed, usually by the pair together at the end of the session.

Anyone in the team can review anyone else's work; seniority is not a requirement. Reviewers look for correctness against the specification, readability and structure, test coverage, logging, accessibility, security, performance and documentation, and they say when something is done well. The reviewer is accountable for the quality of their review. The author decides how to act on feedback, and the conversation that follows is the point.

## Architecture and standards over time

Decisions that shape the structure or technical direction of a system are written up as [decision records](Decision-Records.md). Long-running work is validated periodically by the principal engineer: running the code to test the developer experience and documentation, and checking that deployment, security and coding practice follow our defaults, with any deviation documented and justified. The Engineering Owner plans those checkpoints and acts on what they find.
