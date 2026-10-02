---
title: Roadmap and objectives
authors:
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

The roadmap is a funnel, not a wish list. Ideas enter as proposals and a few become objectives. Every objective is a commitment we expect to keep.

## Proposals

Anyone in AM can write a proposal, using the template in the proposals library on our intranet. It is a short, structured case for a piece of work: the problem or opportunity, who it affects and how, the rough shape of a solution, a rough sense of size and risk, and the open questions. It is deliberately cheap to write, because the point is to surface and compare options. The product team runs workshops with proposers to sharpen the alignment with strategy and the understanding of user need.

A proposal is not a commitment. Several can overlap, and many will never progress. That is the funnel working.

## Validation

Validation turns a proposal into a candidate; prioritising a candidate onto the roadmap makes it an objective. Validation happens in two time-boxed steps, and both decisions and their reasons are recorded.

1. **Viability.** Decision-makers judge whether the work is worth doing now: strategic alignment, the size of the opportunity, the resources it would take, the risk, and the expected return.
2. **Feasibility.** Engineering investigates whether and how it can be done: breaking the outcomes into components, naming the technical assumptions and risks, exploring approaches and giving a rough order of magnitude for effort.

A proposal that passes both becomes a **candidate**. One that does not can be refined and resubmitted, deferred, or discarded. Validation is not a rubber stamp.

## The roadmap

Candidates are prioritised onto the roadmap by senior stakeholders and the product team into three columns:

- **Now**: objectives in active delivery.
- **Next**: objectives ready to start when current work completes, usually already in high-level design.
- **Later**: agreed priorities after that.

The roadmap shows about nine months of work. Each delivery team normally has one objective in each column. The roadmap also shows the Product Owner and Engineering Owner for each objective and links to its canonical document and originating proposal. Alongside it, an outcome dashboard shows the state of every outcome and a release dashboard shows every planned and completed release. Anyone can subscribe to any of them.

## What an objective is

An objective is a committed piece of work scoped to about three months (twelve weeks) or less. It is framed in terms of the value it creates for customers or the business, not the technology that creates it, so that anyone reading the roadmap understands why it matters.

| Weak | Better | Best |
|---|---|---|
| Implement intelligent storage tiering | Reduce per-tenant storage cost through intelligent tiering | Reduce per-tenant storage cost to improve platform gross margin |

Every objective has a **canonical objective document**: the single source of truth for what it is, why we are doing it, and what we expect to deliver. It is owned by the Product Owner, kept short, and maintained throughout delivery. It contains:

- an objective summary anyone can understand
- the problem statement and the evidence behind it
- scope, and an explicit out-of-scope list
- key results that will tell us it worked
- a stakeholder map
- the outcomes that will deliver it

When the canonical document and anything else disagree about scope, the canonical document wins.

## Objectives and outcomes

People conflate these. An **objective** says what we are doing. An **outcome** is a measurable result that tells us it worked: "average per-tenant storage down 30% by the end of the quarter, with no change to page load times". An objective without outcomes is a wish. An outcome without an objective is an aspiration.

One sharp outcome beats several weak ones. Write more than one only when the objective genuinely delivers distinct kinds of value or they will land at different times.

## Scoping

An objective is a commitment, and the roadmap only works as a coordination tool if we deliver what we committed to. Every requirement added to an objective extends the timeline, blurs the success criteria, adds risk and displaces other work. So we scope hard.

Of every requirement, ask: is this the essence of the objective? Could it deliver meaningful value without it? If so, cut it. It may become a future objective, or it may not, and that is a separate decision.

Where the boundary falls is a judgement across four things: our technology strategy, our product strategy, the quality bar we hold ourselves to, and what is realistically deliverable with the people we have. A scope that fails on any of those is worse than a smaller scope that gets them all right. Product Owners should expect pushback on tight scope, from stakeholders and from engineers, and should test their scoping with senior leaders who see across the whole portfolio.

Sometimes an adjacent opportunity is too good to leave. Add it as a **stretch outcome**: explicitly optional, delivered only if the core lands comfortably and nothing more important is waiting. Stretch outcomes never extend the timeline and are always labelled as such. If a stretch starts to look more important than the core, re-examine the objective rather than quietly promoting it.

## Changing course

Priorities change. Objectives can be re-ordered, split, or cancelled after commitment. When they are, the canonical document records what changed and why, and the roadmap reflects the new state. Saying no, or not yet, is a core skill and kinder than saying yes and delivering late.
