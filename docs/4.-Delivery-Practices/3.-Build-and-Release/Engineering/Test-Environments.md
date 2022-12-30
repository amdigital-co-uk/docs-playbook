---
title: Test Environments
authors: 
- Karen Farrell
- Rhod Hewitson
- Ed Earle
- Dave Arthur 
reviewed: 
reviewer:
next-review: 2022-02-01
---

## Who is this for?

This page documents our test environments and the process a Feature/Change follows from being developed to being released to Live.

These practices will be being reviewed and updated rapidly as we work to reduce dependencies and blockers in the development, test, and deployment cycle.

## Guiding Principles

!!! note

    There is no inherent link between test environment type and development lifecycle stage. 
    
    We must avoid principles such as "QA is for testing, then it goes to stage, before it can go live".
    
    We must ensure we perform good testing, but should not be constrained by imagined barriers. 


- The many "QA environments" can be used for any type of testing, include PO
- The single "Stage" environment is used for Business Acceptance Testing (BAT) only. This is because BAT has specific test data in it at present, so the QA environments are not sufficient
- Turn on and off your QA environments when you start and finish using them - they cost money to keep on!
- Always ensure every component (i.e. each microservice) within a QA environment has the latest main branch (i.e. live) deployed to it before deploying the feature(s) under test.


## Test Environment Overview

We currently have 6 QA environments (namely QA & QA-1 thru 5) and one Stage environment (Note: We plan to soon have 10 QA environments – QA & QA-1 thru 9).

The QA environments are predominately used by the Delivery Team to test the Feature/Change

The Stage environment is used by Stakeholders for BAT

Only environments that are currently in use are ever switched on

## Deploying to Test Environments
### Delivery Team Testing

A Feature/Change has been developed and is ready for testing -
1. Switch on a QA environment
1. Deploy the latest microservices along with the Feature/Change under test to the QA environment
1. Test the Feature/Change
1. Any defects raised at this phase are fixed and released to same QA environment
   * On release, ensure the latest microservices are deployed
1. On completion of this test phase, check all deployed microservices are the same version as Live
   * If the microservices remain the latest, the Feature/Change can move to the next phase i.e. PO Sign-Off
   * If the microservices no longer match Live:
     * Deploy the latest versions to the QA environment
     * Smoke Test
     * Move to the next phase i.e. PO Sign-Off

For further information on the release process, please see [Deploying to Test Environments] in the Knowledge Base

### PO Sign-Off
PO Sign-Off takes place on the QA environment with the latest versions of the microservices deployed (i.e. as close to Live as possible)

Ideally, PO will be able to sign-off the release promptly to prevent further smoke testing should the microservices fall out of sync with Live.

* Any defects raised at this phase are fixed and released to same QA environment
* On release, ensure the latest microservices are deployed

Once PO Sign-Off is obtained, the next phase depends on whether BAT is required or not



### BAT Phase Not Required
Testing is complete and PO have signed off the Feature/Change against the latest microservices.  The Feature/Change is now ready to be released to Demo & Live.

### BAT Phase Required

Testing is complete and PO have signed off the Feature/Change against the latest microservices.  The Feature/Change is now ready to be released to Stage for BAT.

1. Check no BAT session is currently taking place on the Stage environment
1. Switch on the Stage environment
1. Deploy the latest microservices along with the Feature/Change under test to the Stage environment
1. Smoke test where required
1. BAT can commence

Following sign-off from Stakeholders, a smoke test may be required should the microservices no longer be up to date (i.e. release to Live occurred during this time).

The Feature/Change is now ready to be released to Demo & Live.

### Following Release to Live

On completion of the release:

1. Follow the [branching strategy guidelines](/6.-Engineering/Source-Control,-Versioning-&-Branching-Strategy) to ensure the main branch is updated
1. The relevant QA environment and Stage (if not being used by another BAT session) must be switched off

### WorkFlow Diagram

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbkFbRGV2ZWxvcG1lbnQgQ29tcGxldGVdIC0tPiB8U3dpdGNoIG9uIFFBIEVudmlyb25tZW50fCBCW0RlcGxveSBsYXRlc3QgbWljcm9zZXJ2aWNlc11cbkIgLS0-IENbRGVwbG95IENvZGUgQ2hhbmdlc11cbkMgLS0-IER7RGVmZWN0cyBGb3VuZH1cbkQgLS0-IHxZZXN8IEFcbkQgLS0-IHxOb3wgRXtMYXRlc3QgbWljcm9zZXJ2aWNlcyBzdGlsbCBkZXBsb3llZD99XG5FIC0tPiB8Tm98IEZbRGVwbG95IGxhdGVzdCBNaWNyb3NlcnZpY2VzXVxuRiAtLT4gR1tTbW9rZSBUZXN0XVxuRyAtLT4gSFtQTyBTaWduIE9mZl1cbkUgLS0-IHxZZXN8IEhcbkggLS0-IEl7RGVmZWN0cyBGb3VuZH1cbkkgLS0-IHxZZXN8IEFcbkkgLS0-IHxOb3wgSntMYXRlc3QgbWljcm9zZXJ2aWNlcyBzdGlsbCBkZXBsb3llZD99XG5KIC0tPiB8Tm98IEtbRGVwbG95IGxhdGVzdCBNaWNyb3NlcnZpY2VzXVxuSyAtLT4gTFtTbW9rZSBUZXN0XVxuTCAtLT4gTXtCQVQgUmVxdWlyZWQ_fVxuSiAtLT4gfFllc3wgTVxuTSAtLT4gfE5vfCBOW1JlbGVhc2UgdG8gRGVtbyAmIExpdmVdXG5NIC0tPiB8WWVzfCBPW1N3aXRjaCBvbiBTdGFnZSBFbnZpcm9ubWVudF1cbk8gLS0-IFBbRGVwbG95IGxhdGVzdCBtaWNyb3NlcnZpY2VzXVxuUCAtLT4gUVtEZXBsb3kgQ29kZSBDaGFuZ2VzXVxuUSAtLT4gUltCQVQgU2lnbmVkIE9mZl1cblIgLS0-IHxZZXN8IFN7TGF0ZXN0IG1pY3Jvc2VydmljZXMgc3RpbGwgZGVwbG95ZWQ_fVxuUyAtLT4gfE5vfCBUW0RlcGxveSBsYXRlc3QgTWljcm9zZXJ2aWNlc11cblQgLS0-IFVbU21va2UgVGVzdF1cblUgLS0-IE5cblMgLS0-IHxZZXN8IE4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGFyayJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid.live/edit#eyJjb2RlIjoiZ3JhcGggVERcbkFbRGV2ZWxvcG1lbnQgQ29tcGxldGVdIC0tPiB8U3dpdGNoIG9uIFFBIEVudmlyb25tZW50fCBCW0RlcGxveSBsYXRlc3QgbWljcm9zZXJ2aWNlc11cbkIgLS0-IENbRGVwbG95IENvZGUgQ2hhbmdlc11cbkMgLS0-IER7RGVmZWN0cyBGb3VuZH1cbkQgLS0-IHxZZXN8IEFcbkQgLS0-IHxOb3wgRXtMYXRlc3QgbWljcm9zZXJ2aWNlcyBzdGlsbCBkZXBsb3llZD99XG5FIC0tPiB8Tm98IEZbRGVwbG95IGxhdGVzdCBNaWNyb3NlcnZpY2VzXVxuRiAtLT4gR1tTbW9rZSBUZXN0XVxuRyAtLT4gSFtQTyBTaWduIE9mZl1cbkUgLS0-IHxZZXN8IEhcbkggLS0-IEl7RGVmZWN0cyBGb3VuZH1cbkkgLS0-IHxZZXN8IEFcbkkgLS0-IHxOb3wgSntMYXRlc3QgbWljcm9zZXJ2aWNlcyBzdGlsbCBkZXBsb3llZD99XG5KIC0tPiB8Tm98IEtbRGVwbG95IGxhdGVzdCBNaWNyb3NlcnZpY2VzXVxuSyAtLT4gTFtTbW9rZSBUZXN0XVxuTCAtLT4gTXtCQVQgUmVxdWlyZWQ_fVxuSiAtLT4gfFllc3wgTVxuTSAtLT4gfE5vfCBOW1JlbGVhc2UgdG8gRGVtbyAmIExpdmVdXG5NIC0tPiB8WWVzfCBPW1N3aXRjaCBvbiBTdGFnZSBFbnZpcm9ubWVudF1cbk8gLS0-IFBbRGVwbG95IGxhdGVzdCBtaWNyb3NlcnZpY2VzXVxuUCAtLT4gUVtEZXBsb3kgQ29kZSBDaGFuZ2VzXVxuUSAtLT4gUltCQVQgU2lnbmVkIE9mZl1cblIgLS0-IHxZZXN8IFN7TGF0ZXN0IG1pY3Jvc2VydmljZXMgc3RpbGwgZGVwbG95ZWQ_fVxuUyAtLT4gfE5vfCBUW0RlcGxveSBsYXRlc3QgTWljcm9zZXJ2aWNlc11cblQgLS0-IFVbU21va2UgVGVzdF1cblUgLS0-IE5cblMgLS0-IHxZZXN8IE4iLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGFya1wiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)
