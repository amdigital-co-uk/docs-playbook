---
title: Source Control, Versioning & Branching Strategy
authors: 
- Ed Earle
- Rob Cloutman
- Dave Arthur
reviewed: 
reviewer:
next-review: 2021-01-06
---

## Who is this for?

Outlines the current source control techniques for our codebases, referred to as our "branching strategy". 

This is targeted at any member of the team who performs work against any of the codebases, including code changes and reviews. 

## Source Control
Code is managed and stored using [Git](https://git-scm.com/docs) and GitHub.

## Branching Strategy

**IMPORTANT NOTE:** This strategy applies to all repositions with the **exception of any shared code repositories** which generate NuGet packages which are  dependencies of multiple other repos/solutions. Please see the specific [Branching & Versioning Shared Repositories](/6.-Engineering/Source-Control,-Versioning-&-Branching-Strategy/Branching-&-Versioning-Shared-Code-Repositories) documentation. 

| **Branch** | **Key Purpose** | **Naming** |
|--|--|--|
| **Main** | Reflection of production environments. At any point you should be able to branch from Main absolutely confident that it will match what is  | `main` |
| **Release** | A release branch is used when EITHER of following conditions are met: <br> 1. multiple features are being released together <br> 2. BAT is required. | `release/{Release-Name]` |
| **Feature** | Contains all the changes required for a specific feature or bug, only. Note that the term "feature branch is used as it is common practice, but it is synonymous with a backlog item - an independent, releasable, valuable product increment. | `feature/{Feature-Name}` <br> OR <br> `bug/{Bug-Name}` |
| **Work** | Contains only the work of an individual within the team. Work is only ever done against a work branch | `work/{Engineer Name}/[feature|bug]/{Feature Name}`|

### Strategy Basics

1. When work is started on a feature a **Feature** [branch](https://git-scm.com/docs/git-branch) is created from the **Main** branch.
1. Each engineer who needs to make changed to that branch must create their own **Work** branch, against which they can commit all changes. Regular and small [commits](https://git-scm.com/docs/git-commit) are recommended, and should be regularly [pushed](https://git-scm.com/docs/git-push). 
1. Each commit must be accompanied by a useful description of the change made.
1. If multiple engineers are working concurrently on a single feature, and their work is interdependent (i.e. could not be usefully tested independently), each should use their own **Work** branch and one **Work** branch should be merged into another, via a [pull request (PR)](#merging-and-pull-requestss) . 
1. When the engineer has completed their work, and it is ready for test, a [PR](#merging-and-pull-requestss) can be submitted to merge it into the **Feature** branch.
1. The [PR](#merging-and-pull-requestss) should be actioned by another member of the team, who should perform a [peer review](/6.-Engineering/Peer-Reviewing) at this time.
1. Changes required should be performed by the original engineer against the merging **Work** branch, but any other member of the team should do this in their absence. 
1. When a [PR](#merging-and-pull-requestss) is completed and the **Feature** branch has been updated, a build will be automatically kicked off and a releasable package created. This can then be deployed into any available QA environment for testing or PO review.
1. When a feature has passed testing and PO review, the **Feature** branch can be merged into either a **Release** branch, the the **Main** branch, by performing a [PR](#merging-and-pull-requests):
    1.  **Release Branches:** 
        > Do this if:  the feature will be released alongside other features, **or** is required to undergo BAT.

        1.  `TBC- A Test Engineer will review and assess the PR to ensure that only the correct features are included for a release`
        1. A new **Release** branch is created by branching from the **Main** branch if one does not already exists. 
        1. Ensure that the feature branch is up-to-date with the **Main** branch and regression tested before merging it into the **Release** branch
        1.  When a merge into the **Release** branch is completed, a build will again be started and a releasable package will be created. This can then be deployed into any BAT environment for PO signoff and Business Acceptance Testing. 
        1. A [release plan]() should be created (or updated), including the package ID. 
        1. When BAT is completed, the package can be deployed to production environments.
        1. Once the release to production environments is complete, the **Release** branch can be merged into **Main** via a PR.
    1. **Main Branch** 
        > Do this if: the feature is released independently **and** does _not_ require BAT. Merge to Main only occurs _after_ the changes are successfully released into the production environments.        
        
        1. Ensure that the feature branch is up-to-date with the **Main** branch and regression tested before merging it into the **Release** branch.
        1. A [release plan]() should be created, including the package ID. 
        1. Once the release to production environments is complete, the **Feature** branch can be merged into **Main** via a PR.
1. Once **Main** has been updated, **communicate the change to all Platform Development teams** so that any WIP branches can be updated and regression tests can be performed.

`// TODO: include images of each step and overall map view`


### Creating a Feature Branch

### Creating a Release Branch

### Merging and Pull Requests

#### Merging Upstream
Upstream merges occur when changes need to pulled into a parent branch. When this is done, a [Pull Request (PR)](https://git-scm.com/docs/git-request-pull) must be submitted and a [peer review performed](/6.-Engineering/Peer-Reviewing) by another member of the team.

You should only merge _good work_ upstream. I.e. it should already be known to pass all quality standards and tests.

#### Merging Downstream 
Downstream mergers occur when changes need to be pulled from a parent branch into a child branch. For example, a release has occurred while a feature is being worked on. In this case the master branch has changed since the feature branch was created, so the feature branch must be updated with the changes. Any work branches relating to that feature branch would also need to be updated.

These changes should be merged and tested prior to attempting a merge up to the parent.

## Deploying Packages

## Tooling
`// TODO:  Recommended source control tooling such as Source Tree/ VS Code Plugins etc
`// TODO:  High-level GitHub overview

## Related Training
You should have a good understanding of Git principals. Our branching strategy details the usual activities, but you may need to perform more advanced git commands occasionally.

### Pluralsight
[Course: Managing Source Code with Git](https://app.pluralsight.com/paths/skill/managing-source-code-with-git)
This course contains a series of training videos from beginner to advanced user need.

### Git Documentation
The [reference documentation](https://git-scm.com/docs) can provide quick information on commands and their purpose. and there is an advanced user book [Pro Git](https://git-scm.com/book/en/v2) available online as well

