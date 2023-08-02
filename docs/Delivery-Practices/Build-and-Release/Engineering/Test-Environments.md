---
title: Test Environments
authors: 
- Karen Farrell
- Rhod Hewitson
- Ed Earle
- Dave Arthur 
reviewed: 02/08/2023
reviewer: Karen Farrell
next-review: 2022-02-01
---

## Who is this for?

This page documents our test environments and the process a Feature/Change follows from being developed to being released to Live.

These practices will be reviewed and updated rapidly as we work to reduce dependencies and blockers in the development, test, and deployment cycle.

## Guiding Principles

!!! note

    There is no inherent link between test environment type and development lifecycle stage. 
    
    We must avoid principles such as "QA is for testing, then it goes to stage, before it can go live".
    
    We must ensure we perform good testing, but should not be constrained by imagined barriers. 


- The many "QA environments" can be used for any type of testing, including PO
- Turn on and off your QA environments when you start and finish using them - they cost money to keep on!
- Always ensure every component (i.e. each microservice) within a QA environment has the latest main branch (i.e. live) deployed to it before deploying the feature(s) under test.


## Test Environment Overview

We currently have 10 QA environments (namely QA & QA-1 thru 9)

The environment 'QA', refletcs Live and is not used for new features

The remaining environments (QA-1...9) are predominately used by the Delivery Team to test the Feature/Change

Only environments that are currently in use are ever switched on

## Deploying to Test Environments
### Delivery Team Testing

A Feature/Change has been developed and is ready for testing -

1. Switch on a QA environment
1. Deploy the latest microservices along with the Feature/Change under test to the QA-n environment
1. Test the Feature/Change
1. Any defects raised at this phase are fixed and released to same QA-n environment
   * On release, ensure the latest microservices are deployed along with the Feature/Change
1. Once the feature/change is complete, check all deployed microservices are the same version as Live
   * If the microservices remain the latest, the Feature/Change can e considerd for deployment to Live
   * If the microservices no longer match Live:
     * Deploy the latest versions to the QA environment
     * Smoke Test
     * Move to the next phase

For further information on the release process, please see [Deploying to Test Environments](https://knowledgebase.platformdev.amdigital.co.uk/Platforms/Quartex/Release/Deploying-to-Test-Environments/).

### PO Sign-Off
PO Sign-Off takes place on the QA-n environment with the latest versions of the microservices deployed (i.e. as close to Live as possible)

Ideally, PO will be able to sign-off the release promptly to prevent further smoke testing should the microservices fall out of sync with Live.

* Any defects raised at this phase are fixed and released to same QA-n environment
* On release, ensure the latest microservices are deployed along with the Feature/Change

### Following Release to Live

On completion of the release:

1. Follow the [branching strategy guidelines](/Delivery-Practices/Build-and-Release/Engineering/Source-Control,-Versioning-&-Branching-Strategy) to ensure the main branch is updated
1. Once feature is merged to Main, Main must be deployed to QA
1. The relevant QA environment must be switched off