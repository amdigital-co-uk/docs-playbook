---
title: Workflow Management
---

Workflow Management describes the way that our solutions are broken down into a hierarchical structure. 

Throughout the problem lifecycle we break large solutions to problems down into small value increments, which are in turn broken down into the smallest independently deployable chunks, each of which require various specific tasks to be performed. 

The objective of workflow management is to provide an adaptable but repeatable structure that reflects this relationship between problems, solutions, value increments, and deployments.

## Workflow Hierarchy

![alt text](workflow-hierarchy.png)

The workflow hierarchy as 4 layers: 

1. Strategic:
   1. [Outcomes](#Outcomes), which belong to a Roadmap Item (in Product Board)
2. [Features](#Features), which belong to Outcomes
3. Backlog, including:    
    1. [Backlog Items](#Backlog-Items) 
    2. [Spikes](#Spikes), which belong to Features        
    3. [Bugs](#Bugs), which belong to Features
 4. Work, including:
    1. [Defects](#Defect), which belong to Backlog Items
    2. [Tasks](), which belong to Backlog Items or Defects
 
![alt text](workflow-relationships.png)

Each layer has its own planning mechanism:

1.	[Delivery Modelling](Delivery-Modelling.md) is used to model the delivery of Outcomes, and therefore show how the roadmap will be progressed. Looking ahead around 12 months.
2.	[Delivery Planning](Delivery-Planning.md) is used to plan the delivery of Features, and therefore show how Outcomes will be delivered. Looking ahead around 6-12 sprints / 3-6 months.
3.	Runway Planning is used to plan the implementation of Backlog Items, and therefore show how Features will be delivered.
4.	Sprint Planning / Iteration Planning is used to plan the tasks that must be performed in order to implement a backlog item.
Using this structure will mean that there is an inherent link between each plan.As estimates and plans are produced for lower layers, their parent item’s estimates and plans must also be updated.
 
!!! note 
    Actual plans will contain significantly more contextual information than is show here, such as dependencies, estimates, ownership, status, risks…

## Workflow Item Definitions

### Outcome

An Outcome is a generic term for a sub goal of a product roadmap objective. The term Outcome could be replaced by “Milestone” or “Epic”. We use the term outcome because it carries more meaning than epic, and is more flexible than milestone. Some Roadmap items may only have one Outcome, while others may have many.

Outcomes must belong to a roadmap item.

### Feature

A feature is a generic term for a sub-goal of an Outcome. Features must be independently usable and valuable. 
Features may require changes to many platforms/repositories.

A feature is not necessarily a functional or user-centric value improvement. While some features may be well described as “user stories”, a feature can also describe non-functional improvements. 

Features can be categorised by the type of investment or purpose, i.e. is this maintenance or added value? If this is maintenance then which type: perfective, preventative, adaptive, or corrective (bugs are generally corrective maintenance).

Features must belong to an Outcome.

### Backlog Item

A backlog item is the smallest operational increment that can be made.

A backlog item should only affect a single repository, for example.

An operational increment must be independently deployable and testable, it must not cause damage, but individually may not be usable or valuable. Each feature would typically require several backlog items.

Backlog items must belong to a feature.

### Spike

A spike is a technical investigation used to remove uncertainties around technical viability and feasibility. Spikes seek to answer specific questions. Then outputs of a spike will include a documented summary of the learnings, and may also include a proof of concept.

### Task

A task describes any discrete piece of work. Each backlog item will require several tasks in order to produce an operational increment. These tasks may span multiple disciplines such as development, testing, design, documentation, and so on.

Task items must belong to a backlog item.

### Defect

A defect is an issue identified during the development lifecycle. A defect is not a bug; an issue identified within production applications.