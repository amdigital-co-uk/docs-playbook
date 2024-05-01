---
title: AMPFlow Terminology
tags:
    - draft
---

This section describes the meaning and purpose of the structural components of the delivery system.

## Goals & Tenets

**AMPFlow** is guided by Goals and Tenets. 

*Goals* set out the purpose of the delivery system and provide a way of qualifying if the system is effective. 

*Tenets* set out the values that guide what goes into a system and how we behave. Tenets can include:

1. Principles: Quantitative and controllable values. We can define practices that cause them, and we can assert that they are happening.
2. Ideals: Qualitative and influenceable values. We can influence and enable them, and measure them with indicators. 
   
## Zones

The delivery system is broken down into familiar “zones”, which encapsulate parts of the whole system, and each of which has an objective. 

The zones are sequentially placed to reflect the initial order they would typically occur. However the model does not prohibit information or action flowing from any zone to another nor action occurring simultaneously in any zone.

In typical delivery systems (or SDLCs) zones may be referred to as “Phases”. Given that phases infers a linear sequence, **AMPFlow** replaces this terminology.

## FLOW

FLOW is the core and primary component of the delivery system. Illustrating the high level direction of information and action within the delivery system, aiding in planning and navigation (where).

Flow is agnostic of how, who, or what. It simply aids planning and navigation.

## Governance

Governance outlines the mechanisms that actors **must** adhere to in each of the delivery system’s zones. Governance provides the **controls** of the delivery system. 

The more artefacts, responsibilities and mechanisms that exist within the system’s Governance, the more closed a system is.

The governance may also specify has interfaces between each of the zones. Zone interfaces outline the criteria that must be met in order to commence work in that zone. Zone interfaces help enforce controls, and enable downstream work to occur more effectively. However, such interfaces are gates which reduce adaptability and Implementation linearity, and therefore should be minimised.

## Toolkit

The Toolkit contains all of the mechanisms that **may** be used in one or more zones by actors as they see fit.

The toolkit is not controlled and continually evolves. Actors will determine the tools they wish to use based on experience and experimentation and the nature of the problem, and may be guided by consultation with stakeholders and peers. New tools can be added at any time as appropriate.

The toolkit provides flexibility in how a problem is solved, leading to a more open system.

Note: here “tool” does not refer to a software tool or service, often also referred to as tools or tooling. The mechanisms within the Delivery System toolkit may leverage software and describe how it is used.

!!! note "Minimum Viable Guardrails"

    Minimum Viable Guardrails (or MVGs) is a principle where a system or mechanism provides only the **controls** absolutely necessary prevent specific failures, while promoting autonomy. 

    MVGs balance standardisation, adaptability and autonomy by promoting lean practices that enable teams to start solving problems with just the minimum amount of information required.

    [Governance](../Governance/index.md) in **AMPFlow** can be considered MVGs.

## Mechanisms 

Mechanisms are the operating techniques or practices which make up our toolkit. They provide guidance or instruction.

## Artefacts

Artefacts are the tangible outputs which are produced by the mechanism we use, such as UI designs, technical designs, specifications, or other documents.

## Responsibilities

Responsibilities define who must or should have ownership of the mechanisms or artefacts, or of outcomes. Responsibility can be categorised in different ways, such as responsible or accountable. Responsibilities are part of Governance, but also used in the toolkit.  