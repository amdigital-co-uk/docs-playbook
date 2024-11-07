---
title: Estimation & ROM
tags: 
- Delivery Planning
- Workflow Management
- Estimation
- Default
---

This document outlines an approach to normalising the outputs from software estimation, for each of layers of the [workflow hierarchy](../Governance/Delivery-Governance/Workflow-Management.md#workflow-hierarchy).

## Estimation vs Rough Order of Magnitude 

It is often necessary to provide an indication of likely scale of work early on the the problem lifecycle, sometimes even before a solution has been determined. This is a Rough Order of Magnitude (ROM), *not an Estimate.*

Estimation, on the other hand, is used to determine the effort required to perform some work or deliver some outcome. Estimates a coupled to a scope. Therefore, as the scope changes the estimate must also change. 

!!! Warning "ROMs are not Estimates"
    The term “Estimate” should be dropped completely when referring to Rough Order of Magnitude, so as to prevent conflation and to make them "safer". Instead refer to them only as “Rough Order of Magnitudes” or “ROMs”.
    e.g. "No, we haven't estimated this yet, there is a ROM though."

## Outcome

Outcomes may require ROMS and Estimates at different points in their lifecycle. 

Both use an ***_Outcome Size_*** as the estimate value, which represent a range of weeks it will take to complete.

### Rough Order of Magnitude

This is an early form of estimation provided when design has not been performed. Estimating “problems” is not possible,  we must at some point make a leap to assume solutions, so ROM estimates must be accompanied by a “ROM Rationale” which would typically detail the assumptions made and the risks associated with those assumptions, by way of caveat.

ROMs have inherently low confidence, so confidence does not need to be captured.

### Estimate

This estimate is iteratively refined throughout the design process, however no Estimate should be produced until it has a high level of confidence, e.g: 75%+. Where no estimate can be produced a ROM must be provided instead. If an estimate can be produced before a ROM has been created, then there is no need to produce a ROM. 

It is possible in some situations that estimating Outcomes directly is impractical, and that ROMs are enough for Outcomes. This aligns well with a continuous discovery approach, but may be less favourable in project based work.

#### Ready to Estimate 

*“Ready to Estimate”* means you can estimate with 75%+ confidence, which can be described as: 

> We express strong confidence in the accuracy of the estimate, grounded in the information available and the team's expertise. We expect the actual time spent delivering this to be no more than 25% over the estimate provided, given the scope as it is stated.

Ready to Estimate Status indicates the item's readiness. A traffic light (RAG) value is used, where:
-  Red indicates little design progress has been made. 
-  Amber indicates a solution has been determined and agreed, with limited detailed specifications.
-  Green indicates there is enough detail to perform an estimate. 

Therefore Green indicates “Ready to estimate” with at least 75% confidence.

### Outcome Size

Outcome Sizes include:

| Size | Time-frame |
|---|---|
| XS | 0-2 weeks |
| S | 2-4 weeks |
| M | 4-8 weeks |
| L | 8-16 weeks |
| XL | 16-32 weeks |
| Unmeasurable | NA  |

_Unmeasurable_ infers that there is not enough information to determine or assume a possible solution, or that the Outcome is too large and must be broken down.

## Feature

Features have two types of estimates, _Rough Order of Magnitude_, and _Estimate._

Both use a _Feature Size_ as the estimate value, which represent a range of weeks it will take to complete, however is a different scale to the Outcome Size.

### Rough Order of Magnitude

Same as Outcome. ROMs are used when there is not enough information to provide an Estimate, e.g. a solution has not been designed.

The same traffic light system applies, to indicate readiness and ability to estimate with high confidence.

### Estimate

Same as Outcome. 

As features belonging to an Outcome are estimated, the Outcome estimate should be updated.

A Feature’s Estimate must be updated when the child BLIs are estimated. As BLIs may have different scales, the team must agree on and consistently use a mapping between their BLI scales and the Feature Size scale, e.g. if using Story Points 0 -1 = XS, 2 = S, 3-5 = M etc.

### Feature Size

Feature Sizes include:

| Size | Time-frame |
|---|---|
| XS | 0-1 weeks |
| S  | 1-2 weeks |
| M  | 2-4 weeks |
| L  | 4-6 weeks |
| XL | 6-10 weeks |
| Unmeasurable | NA  |

!!! Note 
    The *Feature Size* scales are smaller than *Outcome Size*. XL caps at 10 weeks, and it (almost) uses a Fibonacci scale, whereas the Outcome Size uses a doubling sequence. 
    
    A lower cap should force very large features to be disaggregated. *Side note:* Future measurements can provide insights to show whether smaller features are delivered more predictably.    

## Backlog Items & Tasks

It is up to teams to determine what the appropriate estimation scales are. Estimation is not necessarily required at these levels, but may enhance planning, accuracy, and analysis.

Backlog Items and Tasks contain a ***Numeric Estimation*** field which can be used for different types of estimation – points, hours, days, weeks. ***Numeric Estimate Type*** is used to specify the scale being used.

Backlog items also include a ***Backlog Item Size*** field, as a possible alternative to the numeric estimate options.

 Teams can use whichever approach they like, being mindful that consistency will enable better analysis. Other types of estimate can be added later, and a unified approach may be considered.