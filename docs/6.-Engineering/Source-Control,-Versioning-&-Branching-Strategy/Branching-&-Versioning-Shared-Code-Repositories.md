---
title: Branching & Versioning Shared Code Repositories
authors: 
- Dave Arthur
reviewed: 
reviewer:
next-review: 2021-11-06
---

# Versioning

Our shared code packages use Semantic Versioning (or [SemVer](https://semver.org/)) compatible version numbers. These are of the format `MAJOR.MINOR.PATCH`, and one should increment different parts the version depending on the type of changes being made:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

Our CI workflows will only trigger when you merge a pull request into the `main` branch, and will not overwrite an existing package with an identical version. In practice this means that you **must** ensure the version number of a package is update every time you make a pull request. As part of the pull request, you should indicate how the version number is changing, and why.

## When to update version numbers

### Supporting new feature development

When working on a new feature, the most likely types of updates that need to be made to shared code will be one of the following:

* Creating new Request and Response classes for microservice communication
* Updating shared schema definitions (e.g. adding a column to a table)
* Adding new capabilities to other pieces of shared code

In this case you should increment the _MINOR_ version and reset the _PATCH_ to 0. If incremental changes need to be made as part of the same feature .e.g as part of peer review comments, or to address defects raised as part of signing), simply increment the _PATCH_ number for each incremental change that needs to be made.

### Implementing Fixes

When working on a fix of some description (e.g. a fix to an extension method) that should be backwards compatible, simply increment the _PATCH_ number.

### Breaking Changes or Major Updates

Examples of a _MAJOR_ update would include:

* Wholesale refactoring of the package (e.g. splitting some functionality out into a new package)
* Framework version upgrades (e.g. updating the package to be compatible with .NET 5)

**IMPORTANT:** in addition to the examples noted above, should any change that would usually be a _MINOR_ or _PATCH_ change break compilation on any solution depending on the package, then you should instead increment _MAJOR_ version. A breaking change can be thought of as any change the _requires_ code that depends upon it to be updated.

# Updating Packages

Once a pull request has been approved and merged into `main`, any updated packages will be automatically built and published to GitHub Packages, ready to be pulled in by any other repositories that need them.

# Updating Repositories

Once a new version of a package has been created, you need to ensure that the relevant other repositories are updated to use it.

## Applying MAJOR or MINOR version updates

Usually, any update to packages that requires a _MAJOR_ or _MINOR_ version change will be made with one or more repositories in mind. E.g. if creating new Request & Response classes to implement a new endpoint, at least the microservice implementing the new endpoint and one or more other microservice will need to access the new classes.

For each repository that needs the new code, update the relevant `csproj` files within the codebase as follows:

```xml
<ItemGroup>
  <PackageReference Include="Quartex.Package.A" Version="MAJOR.MINOR.*" />
</ItemGroup>
```

This will ensure the service is built against the _MAJOR.MINOR_ version, whilst automatically ensuring it is pulling in any fixes and updates.

## Applying PATCH version updates

Since we are using wildcard versioning, there is no need to explicitly update repositories to pull in the latest _PATCH_ number. 

# Branching

## Source Control
Code is managed and stored using [Git](https://git-scm.com/docs) and GitHub.

## Strategy Basics

Our [versioning strategy](#versioning) means that every change produces a unique package version, and [dependant repositories](#updating-repositories) can specifically target known versions of each package. This means our branching strategy for shared code can be much simpler than the one used for other repository types.

| **Branch** | **Key Purpose** | **Naming** |
|--|--|--|
| **Main** | Reflects the state of the code that produced the last published package.  | `main` |
| **Work** | Contains only the work of an individual within the team. Work is only ever done against a work branch | `work/{Engineer Name}/{Change Name}`|

1. Each engineer who needs to make changes to a package must create their own **Work** branch off **Main**, against which they can commit all changes. Regular and small [commits](https://git-scm.com/docs/git-commit) are recommended, and should be regularly [pushed](https://git-scm.com/docs/git-push). 
1. Each commit must be accompanied by a useful description of the change made.
1. When changes to the package have been completed, and a new version of the package built, the engineer should submit a **Pull Request** back to **Main**.
    - Follow the [pull request](/6.-Engineering/Peer-Reviewing/Pull-Requests#creating-a-pull-request) instructions
    - Fill in the details requested as part of the template pull request
1. Another member of the team should then perform a [peer review](/6.-Engineering/Peer-Reviewing) on the work
    - Any changes requested as part of the peer review should be committed to the **Work** branch.
1. When the review is completed (including any agreed changes, as above), the pull request can be merged into **Main**, and new package versions will be automatically created
