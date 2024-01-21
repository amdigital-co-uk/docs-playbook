---
title: Release Plan Review
authors: 
  - Rhodri Hewitson
reviewed: 
reviewer:
next*review: 2023-06-01
---
# Release Plan Review

## Why do we have Release Plans? 

For any platforms without a fully automated release process, delivery teams are required to create a Release Plan and make sure care and consideration is taken in reducing downtime and releasing the BLI as safely as possible.

## Who can approve a release? 

All Senior Software Engineers and Tech Leads can approve Release Plans.

!!! warning
    A reviewer cannot sign-off a Release Plan they've had a hand in writing. 

## What does a review entail? 

The following is a checklist an engineer should use when performing a Release Plan review. 

* Are all sections filled in?
* Do links to external resources 
    -	Go somewhere?
    - Go to the correct place?
*	Understand the complexity of the release.
*	Given the evident complexity?
    - Are there risks that have not been identified?
    -	Have identified risks been mitigated sufficiently for the given probability and impact?
    -	Are release steps (and rollback steps) detailed enough?
    -	If multiple components are to be released, do they need to be deployed (and rolled back) in any particular order?	
    -	Is there sufficient Smoke Testing? 
* If there is low automated e2e test coverage for a given scenario, would a greater level of smoke testing be required?
* Is there an agreed communication plan?
    - Have timelines been clearly and explicitly shared?
    - Are identified risks and mitigations being communicated appropriately?

