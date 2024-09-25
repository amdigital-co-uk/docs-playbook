---
title: Request for Comments (RFC)
tags:
- Architectural Design
---

## What Are RFCs?

In software, standards, or tech projects, there are lots of ideas and decisions to sort out. A Request for Comments (RFC) is like an open invitation to talk about an idea before making it final. This can be anything from how a new code feature should work to what rules a whole system should follow.

RFCs are written docs that lay out the plan or idea in detail. They let everyone know what you're thinking and give them a chance to give feedback.

## Why Do We Use RFCs?

**1. Open Dialogue:** RFCs let everyone speak their mind. They help make sure you don't miss out on good ideas or avoidable mistakes.

**2. Keeping a Record:** With RFCs, you write down what's being proposed. This helps people understand it better and keeps a record for those who join the project later.

**3. Team Buy-In:** When people have a say in a decision, they're more likely to support it. RFCs make it easier to get everyone on board.

**4. Clearer Thinking:** Writing down your plan makes you think it through. This can help you see flaws or better ways to do things.

## Lightweight RFC vs. Full RFC

For less complex decisions, a simplified RFC using our existing Architectural Decision Record (ADR) format may suffice. In these instances, continue with the standard ADR format while still following the RFC review process. For decisions requiring more comprehensive analysis and documentation, employing the full RFC format is recommended.

## How to Create a Full RFC?

To create a full Request for Comments (RFC), you'll need to follow specific guidelines and structure to ensure the proposal is comprehensive and clear. This involves not just describing the idea or feature, but also laying out the problem statement, alternatives considered, and potential impact.

A detailed template for crafting a full RFC can be found [here](RFC-template.md).

### Key Sections in a Full RFC

- **Title**: Briefly captures the essence of the proposal. It should be prefixed with 'RFC' for easy identification.
  
- **Problem Statement**: A concise explanation of the issue or need the RFC is addressing. This sets the stage for the rest of the document.

- **Duration**: Specifies the time period during which comments and feedback can be given.

- **Current State**: Indicates whether the RFC is in draft, awaiting feedback, closed, and so on.

- **Proposer(s)**: Lists the people who are the main authors or sponsors of the RFC.

- **Detail**: An extension of the problem statement, providing additional context or data.

- **Proposal**: A thorough description of the proposed solution, often supported by code snippets, mockups, or diagrams.

- **Resolution**: The current decision status of the RFC—whether it is in draft, approved, declined, etc.

By following the template and including all these sections, you'll make it easier for team members to understand, discuss, and make decisions based on your RFC.

## Initiating a New RFC

To introduce a new Request for Comments (RFC), please follow the steps outlined below:

1. Create a new RFC document within the appropriate section of our Knowledge Base.
2. Ensure that the document is placed in the correct platform-specific location.

### Pull Request for RFC Review

1. Initiate a Pull Request (PR) specifically for the newly created RFC.
2. Utilize this PR as the forum for reviewing and discussing the RFC's content.

This approach ensures that all RFCs undergo a standardized review process, contributing to the project's overall quality and integrity.

## Approval of an RFC

It's uncommon for an RFC to be outright rejected unless it is significantly misaligned with project goals or standards. More typically, the RFC undergoes a process of refinement until there is a consensus among the team and the broader department. This iterative process ensures alignment and contributes to the overall quality of the project.

## Outcome of an RFC

Upon conclusion of the RFC discussion, an Architectural Decision Record (ADR) should be generated to document the finalized decision. This ADR will serve as the authoritative reference for the decision reached, providing both rationale and implications.
