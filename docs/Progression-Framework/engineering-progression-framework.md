---
title: Engineering Progression Framework 
---

This framework is designed to offer engineers clarity on the competencies expected within their role, and guide their career progression.

This should be used by engineers and their managers to guide training and personal development needs.

Hiring managers should use this framework to help inform hiring decisions.

Role applicants can also use this information to understand what would be expected, and also gain clarity on the future opportunities within AM. 

!!! info "Updates"
    This framework will be updated annually, as roles and business needs evolve.

## Role Types and Levels

In Engineering at AM there are various _Role Types_, for example: Software Engineering, Test Engineering, DevOps Engineering.

_Role Levels_ represent the level of the engineer, there are 6 levels.

The levels are represented E0-E5, where E5 is most senior.

!!! info "Apprenticeships"
    The competency matrix places apprentices and junior engineers together: i.e. the expected behaviours are the same. This is because an apprentice is in training for the junior role. 

    **An apprentice is not expected to perform at the level of a junior, but they are expected to work towards this level.**

    Any apprentice will additionally have clear training objectives specific to their apprenticeship scheme.  

## Career Progression Pathways

Below describes a the simple progression pathway an engineer may take through role levels.

While this diagram presents a linear progression path, it is not expected or implicit that an engineer must pass through each level, nor that they can only progress within the same role type. For example, a test engineer may move into a DevOps role.

This progression path demonstrates the current and near-future role types and levels, but it is expected that this will evolve alongside AM's changing needs.

!!! Info "Progression beyond E4"
    Progression beyond E4 level engineers has not been defined, due to the current and planned structure of the department. However, E5 competencies are partially outlined to provide guided progression for E4 engineers.

``` mermaid
flowchart TD
E0

E0([E0: Apprentice]) --> S-E1([S-E1: Junior Software Engineer])
S-E1 --> S-E2([S-E2: Software Engineer])
S-E2 --> S-E3([S-E3: Senior Software Engineer])
S-E3 --> S-E4a([S-E4: Staff Engineer])
S-E3 --> S-E4([S-E4: Lead Engineer])
S-E4a --> E5
S-E4 --> E5

E0 --> T-E1([T-E1: Junior Test Engineer])
T-E1 --> T-E2([T-E2: Test Engineer])
T-E2 --> T-E3([T-E3: Senior Test Engineer])
T-E3 --> T-E4([T-E4: Lead Test Engineer])
T-E4 --> E5

E0 --> DO-E1([DO-E1: Junior DevOps Engineer])
DO-E1 --> DO-E2([DO-E2: DevOps Engineer])
DO-E2 --> DO-E3([DO-E3: Senior DevOps Engineer])
DO-E3 --> DO-E4([DO-E4: Lead DevOps Engineer])
DO-E4 --> E5

subgraph E1
S-E1
T-E1
DO-E1
end

subgraph E2
S-E2
T-E2
DO-E2
end

subgraph E3
S-E3
T-E3
DO-E3
end

subgraph E4
S-E4
S-E4a
T-E4
DO-E4
end

subgraph E5
TBD
end
```

## Leadership 

### Managerial Leadership

The competence framework describes behaviours expected of individuals with line management responsibility. 

There are 3 levels of management responsibility: 

1. M1: Manager of E0/E1 - An entry to line management, usually managing just one junior or apprentice engineer.
2. M2: Manager of E0-E3 - An accomplished manager, usually managing 2 or more engineers. Typically this would be a **Lead level Engineer** (E4)
3. M3: Manager of E4+ - A highly accomplished manager, usually managing one or more managers.

### Non-Managerial Leadership

Management responsibility is not for everyone. We have created a progression route that enables highly experienced, expert engineers to move into leadership roles, these are know as **Staff Engineers** (S-E4). Staff and Lead engineers share many behaviours, however, a staff engineer would maintain a more holistic system architecture knowledge, as well as profound understanding of the business domain.

## Competency Matrix

The matrix of competencies provides a clear description of an engineer's responsibilities and expected competencies for each level. This document serves as a foundation for communication between an engineer and their manager(s), and it also facilitates feedback between colleagues. 

Our assumption is that engineers can demonstrate their competencies within their specific role and field of work, given adequate opportunities. However, we acknowledge that certain constraints within their role, field of work, and opportunities may impact their ability to demonstrate certain competencies.

[Download the Engineering Competency Matrix](AM%20Engineering%20Competency%20Matrix%20-%20September%202024.xlsx){ .md-button }

### Matrix Structure

The matrix is broken down into three sections:

1. Core Engineering Competencies - competencies that are expected of all role types
2. Role Specific Competencies - competencies that are expected of engineers within a specific role type
3. Management Competences - competencies that are expected of engineers with management responsibilities

Each section contains a number of competencies, grouped into themes and topics.

Each competency describes behaviours that are expected at each role level.

We recognize that growth is not a linear or straightforward process, which means that engineers may demonstrate competencies at various levels. For example, an engineer may exhibit strong debugging skills at level E3, while their security skills may be more in line with level E1. 

To account for this, we treat the competency matrix as a guideline rather than a checklist, and we acknowledge that some minor deviations are normal. If there is evidence of overall growth, these deviations will not hinder an engineer's promotion.

### Implicit Behaviours 

Behaviours of more junior role levels are implicitly expected at each level above, except where that behaviour has explicit stated differently. I.e. an E2 engineer is expected to perform each behaviour of the E1 engineer, plus any specified additional competencies. 

### Glossary

Specific language is used to improve consistency. 

!!! quote "Often / Very Often / Always"
    Occurs frequently / most of the time / consistently and reliably all of the time
    Always is the default, if none is stated.

!!! quote "Proactively"
    Taking the initiative without being asked.

!!! quote "Objectives"
    Refers to Departmental and Product Delivery Team objectives.

!!! quote "Primary Languages & Technologies"
    The language(s) that an engineer is most competent and experience with.

!!! quote "Default Languages & Technologies"
    The languages our business use by default for implementing solutions.

!!! quote "System Context (Technical domain)"
    Information regarding our technology specific to a context or problem.

!!! quote "Technology Estate"
    Encapsulates all the technical domains. E.g. all system context. 
    (See [C4 Architecture](https://c4model.com/))

!!! quote "Piece of work"
    A generic term referring to a discrete task, a backlog item, a feature, or a roadmap item. 

!!! quote "Platform/Service Architecture"
    How the platform or set of services is architected.

!!! quote "Component Architecture"
    How a specific independent component is architected. 
    (See [C4 Architecture](https://c4model.com/))

!!! quote "Container"
    An architecturally grouped set of solution components.
    (See [C4 Architecture](https://c4model.com/))

!!! quote "Team"
    Refers to the Product Delivery team the engineer works within.

!!! quote "Able / Proficient / Expert"
    A basic capability based on limited experience / A good capability based on repeated and varied experience / An excellent capability based on significant and varied experience and supported by theoretical knowledge. 

!!! quote "Technology Vision"
    The planned future state of the _technology estate_. 

!!! quote "Business Domain"
    AM's overall area of activity.


