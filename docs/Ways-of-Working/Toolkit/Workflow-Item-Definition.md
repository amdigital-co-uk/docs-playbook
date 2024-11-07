---
title: Workflow Item Definitions
tags:
 - Workflow Management
---


This document outlines the way in which our [workflow management](../Governance/Delivery-Governance/Workflow-Management.md) item types are defined and configured.

![workflow relationships](../assets/workflow-relationships.png)

## Workflow Item Configuration Guidelines

Workflow items will evolve over time. Keep the following guidelines in mind when making changes to how they defined:

1. It is important to find the balance between simplicity and usefulness. Too much to fill in will create blockers. Err towards simplicity first.
2. Fields should generally never be made mandatory, as often information is emergent during the items lifespan.
3. Reports should be used to identify items that are missing required information or are misconfigured.
4. "Rules" can be used to enforce field completion under certain conditions, but this should be done cautiously.
5. Uniformity across teams is generally necessary, even though it can impede experimentation. Carefully consider the impact of deviation.

''' Info "Further information outstanding"
    It may be useful to include:
    - what each field is for
    - the reports that are run, when, and how they are used
    - any rules applied to specific fields
  

## Outcomes

### States

1. Discovery
2. Design
3. Implementation
4. Operation

### Primary Fields

- Outcome Summary 
- Description
- Ownership: 
    - Problem Owner, 
    - Engineering Owner, 
    - Product Lead, 
    - Delivery Owner, 
    - UX Lead, 
    - Delivery Team
- Estimate
- Roadmap Item: link
- Maintenance Period (Weeks): Number 

### Additional Fields

- Rough Order of Magnitude: Outcome Size
- RAID: related items
 
## Features

### States 

1. New
2. Readying
3. Ready
4. In Progress
5. Complete
   
### Primary Fields

- Description
- Key Stakeholders
- Requirements and Specifications
- Estimate
- Owners: Item Assignee is Problem Owner
- Purpose Type: 
    - New development, 
    - Perfective, 
    - Corrective, 
    - Preventative, 
    - Adaptive
- Outcome: Parent Item Link

### Additional Fields

- RAID: related items 
- Rough Order of Magnitude: Feature Size
- Design and Implementation Plan
- Target Date: date
   
### Ready Criteria

For Feature to be marked as Ready, the following fields must populated: 

- Owners
- Estimate
- Requirements and Specifications
- Description
- Key Stakeholders
- Purpose Type
 
## Bug

### States

- New
- In Refinement
- Ready
- In Progress
- Resolved

### Primary Fields

- Bug Summary
- Estimate: Feature Size
- Steps to replicate 
- Requirements and Specifications affected 
- Requirements data
- Test Data
- Reported By
- Feature: Related Item Link
- Outcome: Parent Item Link
- Priority: integer

### Additional Fields

- Service desk ticket: Link
- Rough Order of Magnitude: Feature Size
- Root Cause

### Ready Criteria

For a Bug to be marked as Ready, all Primary Fields must be populated

## Backlog Item

### States 

- New
- In Refinement
- Ready
- In Progress
- Done

### Primary Fields: 

- Description
- Requirements and Specification summary
- Specifications: link
- Estimate either:
    - Numeric Estimate: decimal
    - **AND** Numeric Estimate Type:  
        - Points, 
        - Hours, 
        - Days, 
        - Weeks
    - **OR** Size Estimate:
        - XS, 
        - S, 
        - M, 
        - L, 
        - XL 
- Estimation Confidence: Percentage
- Engineering Owner
- Owners
- Actual Effort

### Additional Fields

- Design and Implementation Notes
- Test plan: link

### Ready Criteria

Following fields must be populated for a Backlog Item to be marked as Ready: 

- Owners, 
- Estimate, 
- Estimate Confidence, 
- Specification Summary OR Specifications link, 
- Description


### Done Criteria

Following fields must be populated for a Backlog Item to be marked as Done: 

- Design and implementation notes
- Test Plan
 
## Spike

### Status 

- New
- In Refinement
- Ready
- In Progress
- Done

### Primary Fields 
- Learning objective
- Estimate either:
    - *Numeric* Estimate: decimal
    - **AND** *Numeric* Estimate Type:  
        - Points, 
        - Hours, 
        - Days, 
        - Weeks
    - **OR** *Size* Estimate:
        - XS, 
        - S, 
        - M, 
        - L, 
        - XL 
- Estimation Confidence: Percentage
- Owners

### Additional Fields

- RAID: related items
- Approach
- Learning Outcome

### Ready Criteria

- Owners, 
- Estimate, 
- Estimate Confidence, 
- Approach, 
- Learning objective

### Done Criteria

- Learning outcome populated

## Defect

### States

- New 
- Readying 
- In Progress
- Done

### Primary Fields

- Defect Summary
- Environment: *Select test environment*
- Steps to replicate
- Requirements and Specification affected
- Requirements and Specification delta
- Test Data
- Reported By: Assigned to
- Backlog Item: link

## Tasks

### States

- Todo
- In Progress
- Done

### Primary Fields

- Description
- Actual Effort: integer

### Additional Fields

- Numeric Estimate: decimal
- Numeric Estimate Type: 
    - Points
    - Hours
    - Days
    - Weeks
- Remaining: integer

### Done Criteria

Actual Effort is populated with total number of hours spent, for all individuals who performed work for this task.
