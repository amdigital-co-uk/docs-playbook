---
title: Architectural Decision Record
tags:
 - Architectural Design
---

An Architectural Decision Record (ADR) captures a significant decision that impacts the structure, qualities, or core technical direction of a system. ADRs typically document choices around technologies, patterns, integration methods, scaling strategies, security postures, and data flows that are not easily reversed and have long-term implications.

## When to create an ADR

Create an ADR either:

1. The decision has a significant and lasting impact on overall system architecture
    - You are introducing or changing a foundational aspect of a system’s architecture. Even if you are changing it to use a default pattern.
    - A decision materially impacts scalability, maintainability, security, or interoperability.
    - You're choosing between frameworks, languages, cloud services, or deployment models.
    - A decision introduces long-term commitments (e.g., event-driven architecture, microservices, serverless).
2. A [Request for Comments](./index.md#request-for-comments-process) is needed

## Ownership and decision authority

### Problem Ownership

Typically the problem owner for an ADR would be an Engineering Lead or Engineering Owner for the project or objective

### Decision Owners & decision authority

Problems owners must make a balanced decision to determine decision owner and decision authority, but should seek guidance from the Head of Engineering. 

!!! tip "Tips"
      - **Use existing escalation routes:** If a decision has implications beyond your domain, consult higher-level leadership early
      - **Look for ownership and domain expertise:** e.g.
          - Security → consult the Executive Director of Technology
          - Networking or cloud infrastructure → consult the DevOps team
      - **Don’t over-escalate:** Avoid pushing decisions too far up the hierarchy if they can be devolved. Over-escalation slows delivery and prevents autonomy.
      - **Use shared ownership:** If a decision spans multiple domains (e.g., both application and infrastructure), indicate joint ownership or co-sign-off from both authorities.

As a principle, match the impact to the level of authority.

#### Impact is minor or moderate

Affects this team and immediate work or is architectural component level.

- **Authority:** Devolved
- **Decision Owner:** Same as problem owner

#### Impact is moderate

Affects multiple teams immediate or upcoming work, or is architectural container level. 

- **Authority:** Department (Engineering leadership)
- **Decision Owner:** Head of Engineering or multiple Lead Engineers

#### Impact is major: 

Affects medium or long term work or technology strategy, is architectural system context level.

- **Authority:** Department (DMT) or Organisational 
- **Decision Owner:** Head of Engineering and/or Executive Director of Technology
  

## Tips to writing an ADR

- Use diagrams, but sparingly. Ensure they help to improve clarity.
- Use plain language — remember future readers may not have the same context.
- Keep ADRs small and focused. Multiple decoupled decisions = multiple ADRs.
- Include links to supporting evidence (e.g., spike results, benchmarks, risk logs).
- The use of generate AI can be problematic. The problem owner must maintain a complete understanding of their proposal.
- Start simple and add more detail further down. Allow the reader to get the most important information fast, and choose if they want to read more.
