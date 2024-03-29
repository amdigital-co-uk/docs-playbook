---
title: Guide to Planning Design Sessions
authors: 
- Rhodri Hewitson
reviewed: 
reviewer:
next-review: 2021-01-01
---


## Design Session Guidelines

A Design session is an opportunity for the team to come together to design a technical solution for a Roadmap item and get **Alignment** and **Confidence** in the approach. This document aims to share some guidelines on how we can maximize the opportunity.


### Inputs
Careful planning and preparation is required to ensure the session is successful. The following is a non-exhaustive list of **Inputs** required. We've broken down the responsibility to ensure these have been produced for the design session. 

#### Product Manager

- **Stakeholder Map** - a visual representation of all the stakeholders of a roadmap item.
- **Clear problem outline** - a clear breakdown of what problem we're trying to solve.
- **Technical Limitations** - specifications of any specific technical limitation that must be followed to engineer the solution. 
- **Solution Vision** - a vision of how we will realize the solution this (e.g. low-fi designs)
- **Known RAID** - Known Risks, Assumptions, Issues, and Dependencies must be documented

#### Tech Lead

- **Technical considerations** - a high-level idea of how to approach the solution with a rough idea of the platform areas affected and research required to engineer the solution.
- **Session Plan** - a plan of the design session, you should consult with the following to produce this; Principal Engineer, Software Architect, and VP of Engineering. 
- **Existing Architecture**  - an understanding of existing platforms/infrastructure/design, this can be done in collaboration with others to produce this. 
- **Investigations** - given the technical considerations, any components/tools must be investigated and a report produced.
- **Session Length** - ensure the session length takes into account the size and complexity of the roadmap item (use your team to help choose a realistic time frame). 

!!! Tip 
    The person responsible for the input isn't always the person generating the input, but they do need to coordinate the generation of the inputs. Use the _Enablers_ and your product delivery team to help generate the inputs.


### During
Here are some tips to ensure the success of the design session

- As many key participants as possible in-person!
- Interrogate solutions proposed to understand problems needing solving. It is OK to bring solutions, but we must always work backward to the problem.
- Be prepared to challenge ideas. Solutions may be put forward, they need to be challenged.
- The session plan must be led by Tech Lead.
- If during the session it is clear the outcomes cannot be achieved, make a plan to revisit and continue the technical design 
- Always capture Risks, Assumptions, Issues and Dependencies as you go. Ensure that someone is tasked with recording these, and review them frequently.

### Outputs
Once the session has ended there is an expectation we would have produced the following outputs:

- **Low-fi delivery plan** - this should use ROM estimates only, the delivery plan should demonstrate how value will be delivered not when (e.g. critical path map)
- **RAID Log** - this should be an ongoing output during the whole of the design session, consider having a dedicated RAID logger to continually update the RAID log. 
- **Functional Design Definition** - this should detail how the solution will behave functionally.
- **Technical Design** - this should detail how we will go about engineering the solution and should include any additional investigations needed to validate the technical design.
- **High-level Test Plan** - this should detail the approach of how we will test the solution, this shouldn't be exhaustive but should contain the approach and any additional investigations needed.
- **Design & Definition Plan** - outline the design & readying process remaining, our "Road to confidence" 

### Outcomes
The following are the expected outcomes of a design session, if the team hasn't achieved the expected outcomes then it is an indication that further design work is necessary: 

- Aligned on & confidence in functional & technical design
- Aligned on a plan for design & definition
- Understanding of unknown and investigations required
- Stakeholders understand the route to problem resolution


!!! Tip 
    
    Given we are a department that works remotely when setting up an in-person design session, consider the viability of addressing multiple problems. But be considerate of WIP and make sure that you can work on the outputs produced. A further consideration is whether the design session can align with existing collaboration opportunities, e.g. before or after a team day or other in-person event that participants are already likely to be attending in person.
