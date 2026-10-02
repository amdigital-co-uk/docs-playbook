---
title: Decision records
authors:
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

We write down decisions that matter, so that nobody has to relearn them, so that the right people make them, and so that anyone affected can see them coming and comment.

## What gets recorded

Any decision with lasting consequence: what outcomes to pursue after research, what is in and out of scope, how a solution is designed, how it is architected, and what action we will take. Decision records are not a substitute for requirements or specifications. A decision about a specification only needs a record when there is a real design or architectural choice inside it.

An **architectural decision record** is the most common kind. Write one when a decision introduces or changes a foundational part of a system's architecture, materially affects scalability, maintainability, security or interoperability, chooses between frameworks, languages, cloud services or deployment models, or creates a long-term commitment such as an event-driven or serverless approach. Even adopting one of our default patterns deserves a record if it changes a system's shape.

## Where they live

Decision records are kept in a versioned, commentable store accessible to everyone in AM, and indexed in a decision log that shows each decision's title, summary, status, type, owner, authority and impact. We do not keep them in collaboration tools designed for transient notes: a decision record needs a change history and a stable home.

## How a decision is made

1. Someone identifies the need for a decision and becomes its owner, responsible for moving it forward.
2. The owner works out who has the authority to decide, and who the decision owners are.
3. Research is done and one or more proposals are drafted, including options considered and rejected.
4. The record is created in draft.
5. Optionally, the record is opened for **comment**. Stakeholders are told, comment directly on the record, and the proposal is refined until the owner is satisfied.
6. The owner requests approval. The decision owners approve or reject, record the date, and tell the owner.

## Who decides

Match the authority to the impact, and no higher.

| Authority | Suits | Examples |
|---|---|---|
| **Devolved** to an individual or team | Operational and tactical decisions with immediate, local impact | Backlog items and features, component-level design, lower-level user experience |
| **Departmental**, by the department's leadership | Tactical decisions with cross-team or medium-term impact | Complex features and outcomes, container-level architecture |
| **Organisational**, across departments or with executive sponsorship | Strategic decisions with long-term or cross-department impact | System-context architecture, technology strategy |

Most decisions can be devolved, and the request-for-comment step is what makes that safe: the people closest to the work propose and often decide, while everyone with a stake is consulted. Over-escalating slows delivery and erodes autonomy. Where a decision spans domains, name joint owners. Break big issues into small decisions so that the devolvable ones are not swept up in the strategic ones. For architectural decisions, the owner is usually the Engineering Owner, with the head of engineering as a sounding board on authority.

## Writing a good record

Every record carries a [security and reliability impact assessment](Security-Privacy-and-Accessibility.md) of the choice it proposes. Assessing impact at the point of decision is how we avoid auditing it afterwards, and it is why the assessment lives here rather than on every feature.

Lead with the decision and the reason, then the detail. Use plain language for a reader who lacks your context. Keep each record to one decision; several decoupled decisions mean several records. Link to the evidence: spike results, benchmarks, risk logs. Diagrams are welcome when they clarify. If you used a tool to help draft it, make sure you understand and can defend every word; the owner owns the proposal.
