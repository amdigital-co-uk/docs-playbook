---
title: Release Plan Review
authors: 
  - Rhodri Hewitson
reviewed: 
reviewer:
next*review: 2023-06-01
---
# Release Plan Review

## Why do we have release documentation? 
Until we have fully automated our release process, as engineers we must fill out a release plan to make sure care and consideration is taken to ensure we reduce downtime as much as possible and release the BLI as safely as possible,

## Who can approve a release? 
All senior developers and tech leads can review release documentation, but an engineer cannot review a release document they've had a hand in writing. 

## What does a review entail? 
The following is a checklist an engineer should use when performing a release plan review. 

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
* Are comms to stakeholders well thought through?
    - Have timelines been clearly and explicitly shared?
    -	Are identified risks and mitigations being communicated appropriately?

