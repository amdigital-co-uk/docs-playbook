---
title: Decision Logs & Records 
tags: 
   - draft
   - Design
   - Architectural Design
---

Decision logs and records reduce time wasted relearning past decisions and support faster decision-making by the right people.

Decision logs and records enable:

- A clear record of previous decisions, their reasoning, and who made them
- Clear and recorded feedback on proposed decisions (Request for Comment, or RFC)
- Rapid decision-making by the appropriate people

There are five primary decision types:

1. **Discovery**: Deciding on outcomes following research
2. **Scope**: Deciding which requirements will be included in a solution
3. **Design**: Deciding the high-level and low-level overarching solution to problems
4. **Architecture**: Deciding the technical design of a solution
5. **Action**: Deciding what we will do

!!! failure "Not for requirements or specifications"
      While scope, design, and architecture decisions may include details of solution requirements or specifications, they are not a substitute for proper requirements and specification documents.

      Decisions relating to specifications would not normally require a decision record - unless there is a meaningful design or architectural decision to be made.

## Decision Log

The [Decision Log](https://adammatthewdigital.sharepoint.com/sites/Technology/SitePages/Decision-Logs.aspx) is a list of all the past and current decisions. It presents key information and signposts to the full Decision Record documents and is accessible to all staff via the intranet.

## Decision Records

Decision Records are individual documents that describe a decision in full, including the context, research, alternatives, and final choice.

Defaults:

  - decision records should be saved in the [decisions library](https://adammatthewdigital.sharepoint.com/sites/Technology/Decisions/Forms/AllItems.aspx), ensuring tha the document is accessible to all staff and retained for future reference. 
  - use the [template format](./Decision-Record-Template.md), and the [document template](https://adammatthewdigital.sharepoint.com/:f:/s/Technology/ErSjnjprhOdOsxiMEh3CnqkBgAjB92ryx3Oa72WgCR6uLw?e=E9DQIw) provided in the decision library.

The general guidance for all decision records is the same, however where appropriate specific guidance is available for creating records for each decision type.

 - [Architecture Decision Record guide](./Architectural-Decision-Records.md)

!!! success "Use appropriate tools"
      Records must have the following capabilities:

      - [x] Access control: Accessible to all staff, but not to the public
      - [x] Commenting
      - [x] Change history and revision control
      - [x] Discoverable: can be found easily

!!! failure "Avoid collaboration tools"
      Collaborative tools are often designed for transient documentation, do not effectively track changes, and usually encourage formal structures. Avoid tools such as Microsoft Loop and Miro for documentation such as this. 

## Process Flow Overview

In its most simple form, an individual or team puts forward a proposal and then the individuals with the correct authority decide if that proposal should be accepted. There are some additional nuances to how this works in practice.

The lifecycle of a decision follows these steps:

1. **Identify need for decision**  
   A need for a decision is identified (e.g., a new requirement, technical challenge, or opportunity).

2. **Assign Problem Owner**  
   A *Problem Owner* is assigned. This person ensures the decision progresses.

3. **Determine Decision Authority and Decision Owners**  
   The Problem Owner determines [*Decision authority*](#decision-authority) and identifies appropriate *Decision Owners*, who must make the final decision.

4. **Research and proposal development**  
   Research is conducted, and the problem owner ensures that one or more proposals (solutions, outcomes etc.) are drafted.

5. **Create the Decision Record and log entry** 
   
      A formal Decision Record is created, capturing the essential [fields](#decision-record-fields) 

      - Add the Decision to the Decision Log, ensuring it is linked to the document
      - Set the status to "*Draft*"

 6. **Request for comment (Optional)** 
  
    If feedback is needed on the proposed solutions, the status is changed to "*RFC Open*"

    - Stakeholders are notified by the Problem Owner
    - Feedback is provided via comment directly on the decision record
    - The Decision Record is refined based on input
    - Process is repeated until problem owner is comfortable with proposal

6. **Request for approval**
    - Once the problem owner is ready, the status changes to "*Request for Approval*"
    - The Decision Owners are then notified by the Problem Owner

7. **Finalise decision**  
    The Decision Owners finalise the decision. 
   
    - The Resolved Date is recorded, and status is updated to *Approved* or *Rejected*.
    - The Problem Owner is then notified by the Decision Owners 


!!! Note "Decisions library automations"
      Decision records added to the Decisions library in SharePoint will automatically be added to the decision log and remain in sync. Changes to the record will be reflected in the log and vice-versa. 


??? Info "Flow Diagram"
      ``` mermaid
      flowchart TD
         A(Identify need for decision) --> B(Assign Problem Owner)
         B --> C(Determine Decision Authority and Decision Owners)
         C --> D(Research and proposal development)
         D --> E(Create Decision Record and log entry<br><b>Status:Draft<b>)
         E --> F{Request<br>for Comment?}
         
         F -- Yes --> G(Request for Comment process<br><b>Status:RFC Open<b>)
         G --> H(Request for approval<br><b>Status:Request for Approval<b>)
         
         F -- No --> H
         
         H --> I(Finalise decision<br><b>Status:Approved or Rejected<b>)
      ```

## Decision Log Fields

The following fields are stored in the decision log. Decision records created in the decisions library will also have these fields as metadata.

| Field  | Description |
| :--------------------- | :----------------------------------------------------------------------------------------------- |
| **Title**              | A short, clear title for the decision.                                                           |
| **Summary**            | Brief description of the context, the problem, or the decision purpose.                          |
| **Created Date**       | Date and time the Decision Record was first created.                                             |
| **Resolved Date**      | Date and time when the decision was finalised (approved or rejected).                            |
| **Status**             | Current status of the decision: Draft, RFC Open, Pending Approval, Approved, Rejected.           |
| **Problem Owner**      | Person or group responsible for progressing the decision including coordinating the proposals.                                        |
| **Link**               | Hyperlink to the full Decision Record document.                                                  |
| **Impact**             | Importance or consequences of the decision Minor, Moderate, Major                                |
| **Decision Type**      | Categorization: Discovery, Scope, Design, Architecture, or Action.                               |
| [**Decision Authority**](#decision-authority) | The organisational level at the authority to decide resides (e.g., Team, Department, Executive). |
| **Decision Owner**     | Person or group responsible for approving the final decision.                                    |
| **Project/Objective**  | (Optional) Associated project or business objective (linked lookup field).                       |

!!! Info "RFC stakeholders"
      Key stakeholders required to provide feedback to an RFC are not recorded on the decision log. This is because this group may evolve and adapt quite quickly (e.g. one stakeholder may share the document with another). Their comments will however be recorded on the decision record document.


## Decision authority

The decision authority describes who has the authority to make the decision.

In many cases, decisions can be owned and decided by the same individual or team. It is still necessary to record the decision for posterity, and to gather and record feedback via the Request for Comments process.

### Devolved 

Individual or team ownership. This is used then those proposing the solution are entirely able to select the solution themselves. 

This is most well suited to operational decisions, or immediate impact tactical decisions. For example, backlog items and features, lower level UX design or architecture (e.g. component level).

### Departmental

Owned by a leadership community within the Technology Department.

The leadership community may vary depending on the decision. Examples include the divisional management team (DMT), the engineering leadership community, the DevOps team, Product Management team. 

This is most well suited to tactical decisions with inter-team or medium term impact. For example, complex features and outcomes, higher level architecture (e.g, system context or container).

### Organisational 

Requires cross-department agreement, or executive team sponsorship. This is most well suited to strategic decisions with inter-departmental or long-term impact.

!!! Tip 
      Break issues down into small decisions to prevent decisions that could be devolved being swept up in more complex strategic issues. 

## Request for Comments Process

The Request for Comments process is a tool to enable devolved decision making. 

The primary goal is to ensure that key stakeholders are consulted or informed, while the individuals who are closest to the work put forwards the proposal, and even make the decision.

!!! Success "Benefits"
      - **Helps prevent knowledge silos** - new initiatives are made public
      - **Collates expertise and diverse perspectives** - everyone gets to have an input
      - **Record of though process retained** - allowing deeper insights into past decisions
      - **Buy-in and trust building** - everyone has had a chance to contribute towards the proposed solution, making alignment easier
      - **Reduces repeated mistakes** - catching problems early
      - **Quicker than meetings and emails** - a structured process should reduce waste

### RFC Process summary

When a decision record's status is set as Request for Comment, the decision record should clearly outline the problem being solved, the context of the decision (why we need a decision), and the proposal(s). 

More than one option can be put forward, but ultimately one proposal will need to be selected before the decision record can move on to request for approval. Equally, it is encouraged that the problem owner put forward options that are not being proposed, but have been considered.

   1. Stakeholders are notified by the Problem Owner
   2. Feedback is provided via comment directly on the decision record
   3. The Decision Record is refined based on feedback
   4. Process is repeated until problem owner is comfortable with proposal