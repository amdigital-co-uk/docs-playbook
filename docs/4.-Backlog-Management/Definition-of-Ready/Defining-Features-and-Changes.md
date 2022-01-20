---
title: Features and Changes
authors: 
- Helen Duriez
- Ed Earle
reviewed: 
reviewer:
next-review: 01-04-2022
---

# Definition of Ready 

Ready Features and Change Backlog Items should:

1. Meet [INVEST](https://www.agilealliance.org/glossary/invest/) criteria and 
1. Include the following artefacts:
    1. [Problem Statement](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Problem,-Value,-Solution-Statements)
    1. [Value Proposition](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Problem,-Value,-Solution-Statements)
    1. [Solution Executive Summary](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Problem,-Value,-Solution-Statements)
    1. [User Flow diagrams](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/User-Flow-Diagrams)
    1. [UI & UX designs](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/UI-&-UX-Designs)
    1. [Functional Requirements](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Functional-Requirements-with-BDD), expressed as:
        1. BDD Scenarios
        1. BDD Business Rules
    1. Non-functional requirements including:
        1. [Non-functional acceptance criteria](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Non%2DFunctional-Requirements) (above and beyond platform-wide standards)
        1. [Privacy Impact Assessment](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Privacy-Impact-Assessments)*
        1. [Security Impact Assessment](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Security-Impact-Assessment)*
        1. [Accessibility Impact Assessment](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Accessibility-Impact-Assessment)*
    1. [Architectural design]()
    1. [Risks, Assumptions, Issues, and Dependencies](/4.-Backlog-Management/3-Amigos-&-Readying-Backlog-Items/Risk,-Assumptions,-Issues,-&-Dependencies)
    1. Rationalisation - any sporting information that provides context to the artefacts above (for example, a decision log)





# Definition Process Flow
`// TODO:  Determine diagramming needs. Is Mermaid sufficient? Should we link out to Miro, import images, or use something else?

The process flow details an example of the way a roadmap item is understood and eventually turned into well defined backlog items. 

> Note that the specific mechanisms are generally purposefully excluded, such that different techniques and tools can be used as desired by the team. **What matters is that we are able to define great solutions that read for delivery teams as fast and effectively as possible, not _how_ that comes about.**

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggTFI7XG5BW0NyZWF0ZSAzIEFtaWdvc10tLT5CW1BsYW5uaW5nIGFuZCBTY29waW5nXVxuc3ViZ3JhcGggXCJSb2FkbWFwIERlZmluaXRpb25cIlxuQi0tPkNbSW5pdGlhbCBEZXNpZ25dXG5CLS0-RFtUZWNobmljYWwgU2NvcGluZ11cbkQtLT5Fe1N1ZmZpY2llbnQgPGJyPiBLbm93bGVkZ2U_fVxuQy0tPkVcbkUtLT58WWVzfEZbRGVmaW5lIGhpZ2gtbGV2ZWwgPGJyPiBzb2x1dGlvbl1cbmVuZFxuRS0tPnxOb3xYKChDcmVhdGUgPGJyPiBLbm93bGVkZ2UgPGJyPiBBY3F1aXNpdGlvbiA8YnI-IEl0ZW0pKVxuWC0tPkVcbnN1YmdyYXBoIFwiQmFja2xvZyBEZWZpbml0aW9uXCJcbkYtLT5HW0xvdyBSZXMgRGVzaWduIDxicj4gJiBVc2VyIEZsb3ddXG5HLS0-SFtDcmVhdGUgQmFja2xvZyBJdGVtc11cbkgtLT5JW1RlY2huaWNhbCBhcHByb2FjaF1cbkgtLT5KW0hpZ2ggcmVzIGRlc2lnbnNdXG5ILS0-S1tGdW5jdGlvbmFsIDxicj4gYW5kIE5vbi1GdW5jdGlvbmFsIDxicj4gUmVxdWlyZW1lbnRzXVxuSS0tPkxbVGVhbSBSZXZpZXddXG5KLS0-TFxuSy0tPkxcbkwtLT5Ne1JlYWR5P31cbk0tLT58Tm98SFxuZW5kXG5NLS0-fFllc3xOKChBZGQgdG8gQmFja2xvZykpIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRhcmsifSwidXBkYXRlRWRpdG9yIjp0cnVlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid.live/edit#eyJjb2RlIjoiZ3JhcGggTFI7XG5BW0NyZWF0ZSAzIEFtaWdvc10tLT5CW1BsYW5uaW5nIGFuZCBTY29waW5nXVxuc3ViZ3JhcGggXCJSb2FkbWFwIERlZmluaXRpb25cIlxuQi0tPkNbSW5pdGlhbCBEZXNpZ25dXG5CLS0-RFtUZWNobmljYWwgU2NvcGluZ11cbkQtLT5Fe1N1ZmZpY2llbnQgPGJyPiBLbm93bGVkZ2U_fVxuQy0tPkVcbkUtLT58WWVzfEZbRGVmaW5lIGhpZ2gtbGV2ZWwgPGJyPiBzb2x1dGlvbl1cbmVuZFxuRS0tPnxOb3xYKChDcmVhdGUgPGJyPiBLbm93bGVkZ2UgPGJyPiBBY3F1aXNpdGlvbiA8YnI-IEl0ZW0pKVxuWC0tPkVcbnN1YmdyYXBoIFwiQmFja2xvZyBEZWZpbml0aW9uXCJcbkYtLT5HW0xvdyBSZXMgRGVzaWduIDxicj4gJiBVc2VyIEZsb3ddXG5HLS0-SFtDcmVhdGUgQmFja2xvZyBJdGVtc11cbkgtLT5JW1RlY2huaWNhbCBhcHByb2FjaF1cbkgtLT5KW0hpZ2ggcmVzIGRlc2lnbnNdXG5ILS0-S1tGdW5jdGlvbmFsIDxicj4gYW5kIE5vbi1GdW5jdGlvbmFsIDxicj4gUmVxdWlyZW1lbnRzXVxuSS0tPkxbVGVhbSBSZXZpZXddXG5KLS0-TFxuSy0tPkxcbkwtLT5Ne1JlYWR5P31cbk0tLT58Tm98SFxuZW5kXG5NLS0-fFllc3xOKChBZGQgdG8gQmFja2xvZykpIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRhcmtcIlxufSIsInVwZGF0ZUVkaXRvciI6dHJ1ZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)



## Planning and Scoping
"Scoping" of the roadmap item includes the solicitation of requirements from stakeholders and users, and the definition what the scope of deliverable. 

Generally, this includes _who_ (which users) will be able to do _what_, and _why_. This would be accompanied by the specific needs of the users, as well as any specific exclusions (i.e. things that are out of scope). This information will inform the functional and non-functional requirements of resulting backlog items.

Once the scope is known, the 3As can plan the specific activities they wish to perform as through the Definition phase - including how long this will take and when.

## Technical Scoping
This stage include understanding technical scope. This is not to be confused with technical design, which comes later. At this point we know what problem we are trying to solve, and we are looking to understand the technology constraints. 

This could include:
- 3rd party technologies specifically required - for example is there are pre-defined 3rd party API we must integrate with, and what are its limitations and benefits.
- Other work that may block or impact.
- Existing platform limitations or competencies.

## Initial Design
The initial design stage covers researching and then creating one or more design options. 

Design does not necessarily mean creating visual designs.

Again there are no fixed practices for this stage. Each problem will require its own approach and it is up to the 3As to agree on the approach taken.

This is a great time to think about what additional knowledge could be needed. It's quite possible that a desirable solution raises a number of questions about technical feasibility. Do we need to embark on an investigation - such as creating a proof of concept, understanding some technical documentation, etc?

## Define high-level solution
Armed with the scope and some potential solutions, a high level can be defined. A high level solution to a roadmap item should be summarised and, where appropriate, supported with UI designs and a technical overview.

## Low Res Design & User Flow
"Low Res" refers to a low degree of detail, and example of this is wireframing.

Coupled with user flow diagrams, these provide the backbone to our functional requirements.

## Create Backlog Items
The 3As must split the roadmap item into backlog items. Initially this is done by creating "shell" backlog items with the basic information of what it will deliver, the following steps will progress from here to make them "ready".

Turning large solutions into discrete deliverables is an art form! Our definition of ready provides some guidelines of what a backlog item should be, generally centred around the INVEST principals. Further reading and learning on this topic is highly recommended. 

## High Res designs
`// TODO:  complete high res designs section

## Functional and Non-Functional Requirements
`// TODO:  complete Reqs section

## Technical approach
`// TODO:  complete tech approach section

## Team Review
`// TODO:  complete review section