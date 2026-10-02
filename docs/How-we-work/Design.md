---
title: Design
authors:
  - Helen Duriez
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

Design gives everyone clarity on what will be delivered and how, before implementation starts and while it continues.

## Principles

**Prescriptive about outcomes.** Scope, design and specifications are clear before implementation begins. The team and its stakeholders share one picture of what success looks like.

**Flexible in process.** Different objectives need different depth of design. The process adapts to the complexity and risk of the work.

**Keeps pace.** Design is collaborative but time-boxed. We prefer iterative refinement to exhaustive up-front specification.

**Incrementally valuable.** Design supports delivery in thin slices of value. Feature flags separate deployment from release, but we do not accumulate several finished features behind a flag without a release reason.

## Two levels

**High-level design** completes before implementation begins and is recorded in the canonical objective document. It involves the product team, engineering leadership, technology leadership and the business owners of the problem.

| Component | What it says |
|---|---|
| Scope of requirements | The problem, the desired outcome, and what is in and out of scope |
| Solution design | The technical and behavioural approach at system and container level |
| Outcome specifications | The desired behaviour from the user's point of view (the to-be state) |
| Value delivery framework | How value will be realised and measured |

**Detailed design** continues alongside implementation, feature by feature. It involves the whole delivery team, with senior engagement only for significant scope changes or major technical decisions.

| Component | What it says |
|---|---|
| Backlog items | Defined, estimated, independently deployable pieces of work |
| User experience and interface designs | At the fidelity the work needs |
| Outcome specifications | Detailed behaviour that becomes the user guide on release |
| Technical specifications | Container, component and selected code-level detail |
| Incremental delivery plan | The work decomposed into the smallest valuable increments |

## Outcome specifications

An outcome specification describes how the system behaves from the user's perspective. During design it is the requirement (the to-be state). After release it is the documentation (the as-is state), and serves as the user guide. Writing it once and in this form keeps requirements testable and unambiguous, removes the need to rewrite documentation after delivery, and makes a proposed change easy to compare with current behaviour.

## Requirements

Requirements come out of discovery and are refined with the team. They cover behaviour (what the system does), interface and experience (how it appears, including accessibility and mobile considerations), and quality attributes (security, performance, scalability, privacy, testability). Linking them to real use cases keeps the conversation about value. Specifications for backlog items are usually written as scenarios, in Given, When, Then form, so that they become the tests.

The Product Owner is accountable for requirements and specifications being clear and testable. They are written with the team and reviewed hard.

## Design together

Design is a team activity. Everyone in the delivery team takes part in design and planning sessions, and we bring in experts from outside the team where the work needs them. Designers iterate from low-fidelity sketches to high-fidelity designs on feedback. Techniques such as example mapping help find the scenarios and edge cases before anyone writes code. Never design in a bubble: plan when you will check in with stakeholders and what you need from them.

## Design the tests with the solution

A solution design is not finished until it has been turned into a test plan. As the team designs a feature it asks how it will prove each behaviour and each quality attribute, and writes the answer down: the scenarios, the level of the pyramid each will be tested at, the data needed, and what will be explored by hand. The design and the test plan then iterate together. A behaviour that cannot be tested is a design problem, and design is where it is cheapest to fix.

This goes further than writing tests first or driving work from specifications. The test plan is an output of design, produced by the whole team with the test engineer leading, never written in hindsight once the code exists. In a long programme the plan is thorough and settled before a feature is ready. In a short, continuously discovered objective it is lighter and changes more often. The principle is the same: design the proof alongside the thing.

## Architecture, decisions and impact

Architecture is described in a shared model, from system context down to the containers and components the work touches, and reviewed with technical leadership so that it supports the technology strategy. Decisions with lasting consequence are written up as [decision records](../Quality/Decision-Records.md) and, where the wider department should weigh in, put out for comment first.

Security and reliability are assessed where the choices are made. Every architectural, design and scope decision record carries a [security and reliability impact assessment](../Quality/Security-Privacy-and-Accessibility.md), so that the impact is weighed as part of the decision rather than audited after it. Most features inherit their assessment from the decisions they rest on; a feature that introduces no new decision usually has no new impact to assess. An accessibility impact assessment accompanies any change to the user interface.

## Ready to build

Implementation can begin when the high-level design is complete and approved and the first feature meets its definition of ready, with its first backlog items defined and estimated. See [Delivery](Delivery.md) for what ready means. The Product Owner confirms the design addresses the problem; the Engineering Owner confirms it fits the technical strategy. There is no hard boundary after that: detailed design and implementation run together, feature by feature.
