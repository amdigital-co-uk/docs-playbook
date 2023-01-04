---
title: Branching for Functions as a Service
authors: 
- Robert Cloutman
reviewed: 2022-04-01
reviewer:
next-review: 2022-11-01
---

Our Functions-as-a-Service (Faas) are deployed and managed on AWS using [Serverless](https://www.serverless.com/framework), and with that comes the concept of `stages`; the ability to create different stacks of the same service. 

This concept works really well when you need to provide different types of environments for the software development lifecycle of your team or organisation, as it allows you to deploy development code to a development environment using a development stage.

## Source Control
Code is managed and stored using [Git](https://git-scm.com/docs) and GitHub.

## Strategy Basics

| **Branch** | **Key Purpose** | **Naming** |
|--|--|--|
| **Main**  | Reflects the state of the code that produced the *live* version of the function.  | `main` |
| **Stage** | Used to manage instances of a function for testing and development. | `stage/{Stage-Name}` |
| **Work**  | Contains only the work of an individual within the team. Work is only ever done against a work branch | `work/{Engineer Name}/{Change Name}`|

1. When work is started on a feature a **Stage** [branch](https://git-scm.com/docs/git-branch) is created from the **Main** branch.
1. Each engineer who needs to make changes to that branch must create their own **Work** branch, against which they can commit all changes. Regular and small [commits](https://git-scm.com/docs/git-commit) are recommended, and should be regularly [pushed](https://git-scm.com/docs/git-push). 
1. Each commit must be accompanied by a useful description of the change made.
1. If multiple engineers are working concurrently on a single feature, and their work is interdependent (i.e. could not be usefully tested independently), each should use their own **Work** branch and one **Work** branch should be merged into another, via a [pull request (PR)](#merging-and-pull-requestss).
1. When the engineer has completed their work, and it is ready for testing, a [PR](#merging-and-pull-requestss) can be submitted to merge it into the **Stage** branch.
1. The [PR](#merging-and-pull-requestss) should be actioned by another member of the team, who should perform a [peer review](/6.-Engineering/Peer-Reviewing) at this time.
1. Changes required should be performed by the original engineer against the merging **Work** branch, but any other member of the team should do this in their absence.
1. When a [PR](#merging-and-pull-requestss) is completed and the **Stage** branch has been updated, a build will be automatically kicked off and the function will be deployed if successful.
1. When a feature has passed testing and PO review, the **Stage** branch can be merged into the **Main** branch, by performing a [PR](#merging-and-pull-requests).
  > This will trigger a build and deployment to the **live** version of a function.
1. Once **Main** has been updated, **communicate the change to all Platform Development teams** so that any WIP branches can be updated and regression tests can be performed.
