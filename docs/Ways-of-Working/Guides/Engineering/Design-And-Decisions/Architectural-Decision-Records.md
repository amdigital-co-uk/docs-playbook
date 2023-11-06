# Architectural Decision Record

## What Are ADRs?

In the world of software architecture, decisions are frequently made that can significantly impact the project's trajectory. These decisions might concern the selection of a certain framework, adopting a particular design pattern, or using a specific database system.

ADR records are a way to document these crucial decisions. Each ADR record is a small text document that describes a particular decision that was made, the context in which it was made, and the consequences and alternatives of the decision. For more information see the following: ["What is an ADR?"](https://github.com/joelparkerhenderson/architecture-decision-record#what-is-an-architecture-decision-record)

## Why Do We Use ADRs?

**1. Decision Transparency:** ADR records ensure that important decisions are clearly documented, making them transparent to all team members. This transparency helps team members understand why certain choices were made, even if they were not involved in the decision-making process.

**2. Knowledge Preservation:** By recording decisions, we ensure that the knowledge behind these decisions is not lost. This is particularly important when team members leave the project or when a new team takes over.

**3. Facilitating Discussion:** When decisions are documented, they can be discussed more effectively. ADRs provide a basis for discussion and can help to identify any issues or alternatives that were not initially considered.

**4. Onboarding New Team Members:** ADRs can be an invaluable resource when onboarding new team members. They provide a history of the project that can help newcomers understand why things are the way they are.

## How to create an ADR?

We recommend the following format by [Michael Nygard](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/templates/decision-record-template-by-michael-nygard/index.md) 

**Title:** A short descriptive name for the decision.

**Status:** The status of the decision [Accepted, Declined, Superseded, Deprecated]

**Context:** This describes the situation that calls for the decision.

**Decision:** The actual decision itself.

**Consequences:** What becomes easier or harder to do as a result of the decision?

**Alternatives:** Other options that were considered but not chosen.

!!! Warning

    It's essential to keep these records consistent and up-to-date. They should be treated as living documents that evolve with the project.

!!! note

    The Decision records you generate might be superseded as we learn more and gain a better understanding, and that's okay! It's a sign that the team is focused on continuous learning and exploring new technologies.

## Tips to writing an ADR

The goal is to create a clear and straightforward ADR that is as easily understandable as possible. Strive to use language that is both professional and simple. While using ChatGPT is acceptable and even recommended, be mindful that it may produce verbose replies, so use it with caution. If you need to describe a significant amount of information, you might want to consider writing a [RFC](Request-for-Comments.md) first.
