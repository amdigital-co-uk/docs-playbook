---
title: Peer Reviewing
authors: 
- Dave Arthur
- Ed Earle
- Rhodri Hewitson
reviewed: 
reviewer:
next-review: 2021-11-01
---

## Overview

The purpose of a peer review is to identify mistakes as early as possible and ensure that the way a solution is implemented is:

1. Understood by more than one member of the team - creating a shared understanding of our platform
1. Inline with our **quality standards**

Peer reviewing must not be left until last minute, or performed as a one-time event. Instead, we should be working closely with our colleagues to share our approach throughout the development cycle. This allows for early feedback around the way a solution is built, and allows for the reviewer to gain a greater degree of context.

The final stage of peer reviewing is when code is [merged into a parent branch](/Delivery-Practices/Build-and-Release/Engineering/Source-Control,-Versioning-&-Branching-Strategy) (e.g. Work Branch --> Feature Branch, or Feature Branch --> Release Branch). This process allows for in depth reviewing of the full solution.

## Pair Programming & WIP Reviewing

Think about potential review points as a team during sprint planning! Creating discrete review tasks will help track progress and remind the team of the need to review.

Pair programming, screen share walk throughs, or simply reviewing a work branch are some ways to perform peer reviews of WIP.

Any member of the team can perform a peer review for anyone else, not just a more senior member!

### Providing Feedback for WIP

Feedback should be given directly to the original engineer by the reviewer. The reviewer should feel free to ask questions and provide their honest perspective. It is wise to support feedback with rationale;

- in what way could the solution be improved?
- how will these improvements help us improve quality?

The original engineer is not obliged to act upon all feedback, but an open discussion will be very beneficial.

### Reviews whilst pair programming

A review should still be performed for any code written during a pair programming session. However, it may be helpful for the two engineers to perform the review together at the end of the pairing session. E.g. the engineer that has been screen sharing/writing the code should check everything in, and then the other engineer lead the review. However both engineers would be encouraged to discuss whether or not the code they have written together fulfils the guidelines.=

## Submitting code for a review

It is best to submit code to be reviewed frequently, both to get early feedback and to ensure that the reviewing engineer can get a good picture of the changes without being overwhelmed by a huge amount of changes all at once. In other words, follow the principle of little and often!

When submitting a PR the engineer should follow the [Pull Request Guidelines](/Delivery-Practices/Build-and-Release/Engineering/Source-Control,-Versioning-&-Branching-Strategy/Pull-Requests), and should ensure to provide some context of what the code being reviewed is try to achieve and how it is structured.

If refactoring existing code (in preparation for subsequent changes), the refactoring should be performed separately and submitted for review in isolation. It would otherwise be much harder for the reviewing engineer to understand how the refactoring has been done if there are also additional changes and new functionality mixed in.
