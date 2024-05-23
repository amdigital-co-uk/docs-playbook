---
title: RAID
tags: 
 - draft
 - Challenge Mapping
 - Default
---


## Objective

Proactively manage and mitigate risks, assumptions, issues and dependencies throughout the full problem lifecycle.

## RAID

RAID is a well established project management tool used to identify, track, and manage key aspects that can impact the success of the delivery of a solution. 

RAID provides a mechanism for [Challenge Mapping](../Governance/Problem-Governance/Challenge-Mapping.md)  

- **Risks** - The objective of managing risks within RAID is to identify potential threats or uncertainties that could impact the delivery plan objectives, timeline, budget, or quality. By identifying risks early on, the development team can implement strategies to mitigate or eliminate them, reducing the likelihood of negative consequences
- **Assumptions** - Assumptions are underlying beliefs, or conditions that are taken for granted, or preliminary decisions that have not been validated. Assumptions have the potential to influence outcomes. The objective of managing assumptions within RAID is to document and validate these assumptions to ensure that they are accurate and aligned with the problem hypothesis and solution. By addressing assumptions upfront, the team can avoid misunderstandings or misalignments that could derail delivery.
- **Issues** - Issues are problems or challenges that arise throughout the problem lifecycle (although particularly during Design and Implementation). The objective of managing issues within RAID is to track and address these issues in a timely manner to prevent them from escalating and impacting progress. By actively managing issues, the team can minimize disruptions and keep the delivery on track towards its objectives.
- **Dependencies** - Dependencies are relationships between tasks or deliverables that dictate their sequence or interdependence. The objective of managing dependencies within RAID is to identify and track these relationships to ensure that tasks are executed in the correct order and dependencies are managed effectively. By understanding and managing dependencies, the team can optimize workflow and minimize delays.

## RAID Logs

A RAID log is a document or tool used to capture, track and manage any identified RAID items. Typically RAID logs are used to proactively identify, assess, and manage risks, assumptions, issues, and dependencies throughout the problem lifecycle. 

By maintaining a comprehensive RAID log, delivery teams can improve their ability to anticipate and respond to challenges, minimise disruptions, and ultimately improve effectiveness.

Typical RAID tooling options include:

- Excel Spreadsheets
- Software development tools e.g Azure DevOps and Jira
- Project management tools e.g Loop, Confluence
- Visual collaboration tools e.g Miro 

Each tool comes with its own set of distinct advantages and potential disadvantages for capturing and managing RAID

## RAID Planning Events

RAID Planning is an event during which the delivery team produces and/or updates a structured RAID log.

Together the delivery team will review existing and identify any new RAID items, considering and documenting:

- the perceived impact, 
- the perceived likelihood,
- workarounds or mitigation plans


## Responsibilities

| Owner                 | Responsibility |
|---|---|
| Delivery Owner        | The Delivery Owner is **accountable** for ensuring that effective RAID management is happening at appropriate times and the results are both accessible and effectively communicated with colleagues and stakeholders |
| Delivery Team         | The whole Delivery team is collectively **responsible** for RAID identification, management and mitigation |
| Product Lead          | **Responsible** for participating in any RAID planning events where necessary, and by collating and sharing relevant product related insights that could lead to the identification of new RAID items |
| Engineering Owner     | **Responsible** for participating in any RAID planning events where necessary, and by collating and sharing relevant engineering related insights that could lead to the identification of new RAID items |
| Design Owner          | **Responsible** for participating in any RAID planning events where necessary, and by collating and sharing relevant design related insights that could lead to the identification of new RAID items |

## Triggers
Typical triggers for RAID capture and/or RAID planning events include (but are not limited to):

- **Requirement Elicitation** - as requirements are gathered for the problem during the discovery zone 
- **Design** - during the design zone and design workshops, triggers could include architectural decisions that introduce technical risks, assumptions about third party integrations, or dependencies on specific design components
- **Resource Allocation** - changes in resource availability or allocation
- **Technologies and/or Tools** - selecting new technologies or tools for the solution 
- **Change Requests** - whenever there are changes to solution requirements, scope, or timeline
- **Testing and Quality Assurance** - issues identified during testing and quality assurance activities can trigger RAID items relating to defects, performance issues, or dependencies on external systems 


## Communication Plan

Delivery teams are responsible for ensuring relevant stakeholders and/or colleagues are informed about the status of key RAID items and any actions being taken that could potentially impact delivery timelines, other delivery teams plans, or stakeholders and other departments.

RAID communication plans typically include and document:

1. **Communication Channels** - with delivery teams via regular team meetings or RAID planning events or **with stakeholders:** via [delivery status updates and reports](../Governance/Delivery-Governance/Delivery-Status-Reporting/index.md), ad-hoc communications to address urgent or critical RAID items, 
2. **Content & Format** - RAID item summary, detailed descriptions, action items and trends in RAID dat over time
3. **Escalation Process** - defined escalation process for addressing high-priority or critical RAID items that require immediate attention or resolution 
4. **Feedback Mechanism** - encourage feedback from stakeholders and team members on the effectiveness of RAID communication and any improvements or suggested adjustments required
5. **Review & Continuous Improvement** - regularly review the effectiveness of the RAID communication plan, gathering feedback from stakeholders and team members and identify opportunities for improvement

!!! Note
    Not all RAID entries need to be communicated to all stakeholders, and in some situations can confuse rather than inform a stakeholder. Reporting on RAID should be tailored for the appropriate audiences, focussing on the key entries of most concern or perceived impact.


## Considerations

- Review the tooling section of the Knowledgebase for current [default document templates](https://knowledgebase.platformdev.amdigital.co.uk/Tools-and-Providers/AMPFlow-Governance/).
