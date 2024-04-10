---
title: Technical Design Workshops
authors: 
- Rhodri Hewitson
reviewed: 
reviewer:
next-review: 2021-01-01
---


## Design Session Guidelines

A Technical Design Workshop is an opportunity for the team to come together to design a technical solution for a problem, creating **Alignment** and **Confidence** in the approach. 

This document aims to share some guidelines on how to maximize the opportunity.

### Inputs

Careful planning and preparation is required to ensure the Technical Design Workshop is successful. The following is a non-exhaustive list of **Inputs** required.

Many of these input should already be documented.

| Input | Details | Ownership |
|-- | -- | -- |
| Session Plan          | A plan for the design session (e.g. format, agenda, participants, duration) | Engineering Owner |
| Stakeholder Map       | A visual representation of all the stakeholders of a roadmap item.   | Product Lead |
| Problem Statement     | A clear summary of the problem being solved.                         | Product Lead |
| Problem Requirements  | A clear breakdown requirements.                                      | Product Lead |
| Solution Vision       | A vision of how we will realize the solution this (e.g. low-fi designs) | Product Lead |
| RAID Log              | Documented Risks, Assumptions, Issues, Dependencies                  | Product Lead, Engineering Owner |
| Existing Architecture | An understanding of existing related or dependent technologies       | Engineering Owner |
| Technical Limitations | Specifications of any technical limitation that must be followed to engineer the solution. | Engineering Owner |
| Investigation outcomes| Summary of learnings from up-front investigations                    | Engineering Owner |

!!! Note 
    Responsible refers to who must ensure inputs are prepared. It will be neccessary to involve others to create them.

### During

Here are some tips to ensure the success of a Technical Design Workshop

- Accountability: The Engineering Owner is accountable for the Technical Design of a solution and outcomes of these workshops.
- Duration:
  - Break it down into chunks
  - High-level design can identify the need for multiple low-level designs 
- Location:
  - In person is better where possible
  - Hybrid should be avoided where possible (multiple people in person, multiple people dialled in)
  - Large, complex, or very complicated problems will benefit from face-to-face collaboration
  - Urgency should take preference over coordinating face-to-face design
- Give careful consideration to pre-existing solutions, but always evaluate their efficacy, and be sure the problem is fully understood first.
- Be prepared to challenge ideas. Solutions may be put forward, they need to be challenged.
- If during the session it is clear the outcomes cannot be achieved, make a plan to revisit and continue the technical design 
- Always capture:
  - Risks, Assumptions, Issues and Dependencies.
  - Designs and ideas agreed and discarded.
- Ensure that someone is tasked with recording these throughout the workshop, and review them frequently.

### Outputs

Following the completion of a Technical Design Workshop the following outputs are expected:

- **High-level implementation plan** - this should include rationalised Rough Order of Magnitude (ROM) estimates as well as an iterative and incremental order of delivery, decorated with dependencies and milestones. Consider critical path mapping.
- **RAID Log** - this should be an ongoing output during the whole of the design session, consider having a dedicated RAID logger to continually update the RAID log. 
- **Functional Design Definition** - this should detail how the solution will behave functionally.
- **Technical Design** - this should detail how we will go about engineering the solution and should include any additional investigations needed to validate the technical design.
- **High-level Test Plan** - this should detail the approach of how we will test the solution, this shouldn't be exhaustive but should contain the approach and any additional investigations needed.
- **Design Plan** - update the plan for continuing the design process.
- **Stakeholder update plan** - Create a plan for communicating the outcomes of the session with stakeholders.

### Outcomes

The following are the expected outcomes of a Technical Design Workshop, if the team hasn't achieved the expected outcomes then it is an indication that further design work is necessary: 

- Aligned on & confidence in functional & technical design
- Aligned on a plan for design & definition
- Understanding of unknown and investigations required
- Stakeholders understand the route to problem resolution

!!! Tip
    If travel will be required for a Technical Design Workshop, consider organising workshops for other problems consecutively. This may reduce travel fatigue as well as costs. Be careful not to overload attendees, as these workshops can be draining.
