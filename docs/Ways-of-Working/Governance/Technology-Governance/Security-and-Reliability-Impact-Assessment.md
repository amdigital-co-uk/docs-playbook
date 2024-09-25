---
title: Security & Reliability Impact Assessment
---

## Objective

Security & Reliability Impact Assessments (SRIA) ensure that product and system security and reliability is considered and evaluated during the technical design of solutions, to ensure that the impact to security and reliability is well known, and to enable mitigations to be designed for.

## Security

- includes threat analysis and modelling
- impact on security tests
- impact on known issues and vulnerabilities
- impact on maintenance / maintenance strategy 
  
## Reliability

- includes performance of systems under load (user, data) - see relevant NFRs
- includes how graceful failure
- ability to recover from failures, including DR
- observability, including logging, monitoring, and alerting

## Reliability Impact Assessment

An SRIAs is specific to the implementation of a solution. Once a solution has been delivered, future changes to that solution would require new SRIAs. 

SRIAs should be produced during and as part of solution design. Producing during allows for iteration of the solution design, and emerging and shared understanding and alignment.

Once the solution design, including arch design, has been determined, the SRIA must be documented. The SRIA must be updated if the design changes throughout the implementation.

## Responsibilities

| Owner                 | Responsibility |
|---|---|
| Engineering Owner     | The Engineering Owner  **accountable** for the impact assessment and **responsible** for ensuring that it is created and documented, and that appropriate technical stakeholders are involved. |
| Delivery Team         | The Delivery Team are collectively **responsible** for supporting the creation of the impact assessment |
| Technical Stakeholders| Various technical stakeholders, such as VP Engineering, Principal Engineer, are **accountable** for the overarching reliability and security of of our technology estate. |

## Triggers

- all work
- inheriting upwards (parent project SRIAs cover work within)
- IA template ensures that assessments are quick if no impact is perceived

#### Toolkit

!!! toolkit "Toolkit"

    <!-- material/tags { include: [SRIA] } -->