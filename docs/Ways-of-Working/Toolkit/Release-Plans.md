---
title: Release Plans
authors: 
- Dave Arthur
reviewed: 
reviewer:
next-review: 2025-02-01
---

Any releases to production environments that are not fully automated must be acompanied by a release plan. This is to ensure that software is released smoothly and efficiently, with minimal disruption to users. A deployment plan can help in the following ways:

- **Reduce the risk of errors** by ensuring engineers performing it know exactly what to do
- Ensuring engineers can perform the release quickly and efficiently and thereby **reducing downtime**
- **Improve quality** by having a smoke test plan in place to quickly assert that the release has been successful
- **Mitigate potential risks** by explicitly identifying risks and having rollback plans and mitigation plans

In addition to these benefits, any changes to platforms that are subject to SOC2 _**must**_ be documented to maintain compliance.

!!! info
    See also: **[Release Notifications](./Release-Notifications.md)**

## What types of release need a release plan?

Any release that changes production infrastructure in any way and is _not_ fully automated requires a release plan. This can include

- Deploying code to existing infrastructure
- Adding or creating new infrastructure
- Modifying existing infrastructure

## What types of release do not need a release plan?

Any release that is fully automated via some kind of pipeline, requiring little to no manual intervention does not need a release plan to be created. These types of release are usually initiated by merging a Pull Request which kicks off the pipeline. Fully automated releases include:

- Changes to infrastructure that is managed via Terraform
- Applications that have a full CI/CD pipeline

In these instances, the associated Pull Request, pipeline logs and source control changes are sufficient documentation to satisfy the SOC2 requirement to document any changes to production infrastructure.

!!! note
    Deployments to non-production environments or deployments of not-yet-live platforms also do not require any kind of release plan.

## Documenting Release Plans

Regardless of how they are documented, a release plan should include at least the following:

- Stakeholders to communicate with
- Risks associated with the release
- Steps required to perform the release
- Smoke test plan
- Rollback plan where applicable

### Simplified release plans

For any simple, low-risk release that only involves components from a single repository, teams may document their release plan within with the Pull Request (PR) that merges the changes being released into the `main` branch. There is a template for this which can be applied when merging to main.

Documenting and performing the release can then be done by following these steps:

- Create PR to main, adding the `release` label to the PR
    - Automation populates updates the PR details with the template
- Engineer updates the release plan with risks, steps and smoke test plan
- Plan is reviewed by another engineer. Approving the PR records the fact of the plan being approved
- Perform release steps manually as we currently do
- Check off steps using checkboxes in the PR as they are performed
- Merge to main once all complete

!!! info
    Adding the template for simplified release plans to a repository is as straightforward as adding this **[shared workflow](https://github.com/amdigital-co-uk/workflows/blob/main/OTHER.md#create-release-plan-template)**

    Note that GitHub repositories don't automatically have the `release` label created, so simply create it manually the first time.

### Full release plans

For any higher-risk releases, or ones that involve the simultaneous deployment of multiple components from different repositories, teams must use our existing full release plan template.

This takes the form of a Word Document saved within the **Technology** `>>` **General** `>>` **Deployment Plans** folder in Sharepoint.

Teams must create their release plan from the template, and save it within the relevant Platform & Year subfolder as appropriate.