---
title: Quality Standards
authors: 
- Dave Arthur
- Ed Earle
- Rhodri Hewitson
reviewed: 
reviewer:
next-review: 2021-12-01
---

# Who is this for?
Outlines the standards to which Software Engineers and Test Engineers must adhere when writing code.

# Overview
Quality means more than simply the way code is structured! Great quality solutions cover many facets, including:

- Readability & Maintainability
- Security & Compliance
- Robustness & Performance
- Architectural integrity
- Cost & environmentally friendly

This is why it is important to share our approach to solutions early! Peer reviews should be looking to improve any/all of these areas, and it may often be too late by the time you have working code ready to merge.

# Guiding Principles

- Code must be easy to read and understand
- C# Code must follow OO patterns and SOLID principles
- Coding and naming conventions must be followed
- Unit and integrations test coverage must be maintained or improved
- Event logging must be used to provide useful diagnostic information
- Code must be self describing, and must not rely on code commenting to demystify chaos
- Code must be well documented, and must use code commenting and READMEs to enable rapid discovery
- User interfaces must be accessible and conform to WCAG AA
- Code must be secure and follow industry recommended practices
- Code must be performant, and able to handle live-like datasets and load
- Code should be [green](https://principles.green/)

# Guidelines for high-quality code

## Readable and Maintainable

First and foremost, high-quality code must be easy to read and understand. Code must also follow our in-house [coding conventions](/6.-Engineering/Quality-Standards/Coding-Conventions). The names of methods and classes etc. must clearly indicate what they do, and methods and classes must not be too lengthy.

Code must also follow the [SOLID principles](https://www.youtube.com/watch?v=pTB30aXS77U), which will help to make it better structured, more readable and keep methods and classes manageable sizes.

When creating new endpoints on microservices, ensure that they follow the [endpoint naming conventions](/6.-Engineering/Quality-Standards/Endpoint-Naming-Conventions).

Making code more _maintainable_ is effectively the practice of minimising the amount of times you have to _update_ it. Avoid using hardcoded values in code, as these values can only be changed by changing the code. Instead, consider making the behaviour of the code configurable by offloading these values to configuration.

Similarly, do not repeat yourself (DRY)! Avoid copy/pasting code; instead consider how and where to share it. For smaller snippets of re-usable code, consider putting it in a helper class or extension method. Also consider the scope of any shared code; is it specific to the current repository, or is it more general code that might benefit from living in a shared code library for re-use across other repositories too? Following the Single Responsibility Principle (one of the SOLID principles, see above) should help with this.

Do not commit commented-out code. It makes code less readable, and also causes confusion. When commented-out code is committed to a repository, it is not clear whether it should simply be deleted, or the code needs to be adapted and integrated, i.e. is it a cryptic TODO?


## Unit & Integration Tests

Code must be well covered by [unit & integration tests](/6.-Engineering/Quality-Standards/Unit-&-Integration-Testing). Unit & integration testing not only increases our chances of catching bugs, increases engineer confidence in any changes being made, but is also an indication that the code is well-structured.

To meet quality guidelines, all .NET code must be covered by Unit and/or integration tests with the aim of achieving 80% code coverage. For legacy repositories that do not meet this threshold, the aim should be to _increase_ the coverage coverage percentage when writing new code, so as to incrementally meet the desired threshold. For repositories that are already well-tested, all new code must be sufficiently well tested so as to not bring the average coverage down.

> **NOTE:** code coverage is not a perfect metric. It is entirely possible to write poor tests that achieve an arbitrary coverage without providing any of the real benefits.

Code repositories must measure and report on code coverage metrics as part of Continuous Integration. If not already present, add the [code coverage testing](https://github.com/amdigital-co-uk/quartex-ci/blob/main/docs/code-coverage.md) tools to the repository being worked on. As engineers write tests for a repository, they must ensure the `tests.yml` file is updated with the latest coverage level.

## Observability & Logging 

Building observable systems enables development engineers to measure how well the application is behaving. Observability serves the following goals:

- Provide holistic view of the application health.
- Help measure business performance for the customer.
- Measure operational performance of the system.
- Identify and diagnose failures to get to the problem fast.

A critical part of this is ensuring that services are logging useful events and errors. Log messages need to contain enough information to help an engineer understand what was happening, including for example Website Key or Client Key, ID of an asset or document affected, action being performed etc.

See more information about [logging in Quartex](/6.-Engineering/Quality-Standards/Logging-Best-Practise), and further reading on general [best practices](https://microsoft.github.io/code-with-engineering-playbook/observability/pillars/logging/#best-practices) for logging.

## Documentation

Every software development project requires documentation. [Agile Software Development](https://agilemanifesto.org/) values _working software over comprehensive documentation_. However, repositories must include the key information needed to understand the development and the use of the generated software. Good documentation should work towards these goals:

- Facilitate the onboarding of new team members
- Improve communication and collaboration between teams
- Enable other engineers to successfully work with the software

Every repository must have a README, which should succinctly explain:

- The purpose of the repository
    - For a service, this boils down to "what is the service responsible for?"
    - Otherwise explain the use-cases for using or modifying the repository
- Any external dependencies that are not automatically imported
- Additional steps required to build or debug the code
- Any processes that are unique to this repository

Further reading on [documentation guidelines](/1.-Welcome/Documentation-Guidelines/Documentation-Guidelines/).

Documentation must never include any passwords or other sensitive configuration. These should be stored and documented in a secure manner, such as in a Password Manager (_TODO - setup password management for division_) or in a Secrets Manager.

Any hacks or shortcuts or TODOs must be documented, as these all represent the addition of different types of technical debt. Engineers must be mindful of any technical debt being committed, and must have a plan to resolve it. This might include creating a backlog item to address the technical debt, with a plan to bring it into a subsequent sprint.

## Accessibility

Any new UI elements must be made accessible, and conform to WCAG AA. This includes making the UI usable via Screen Reader, including adding `aria` tags where relevant. The UI must also be usable with the keyboard.

## Secure Code

Engineers must ensure that code adheres to industry-recommended standard practices for secure design and implementation of code. For practical purposes, engineers must be familiar with the [OWASP top 10 vulnerabilities](https://owasp.org/www-project-top-ten/). The OWASP [secure coding practices guide](https://owasp.org/www-pdf-archive/OWASP_SCP_Quick_Reference_Guide_v2.pdf) is also a useful reference.

Ensuring software is secure relies not just on the software being written, but also the Frameworks and Libraries it depends on; which makes keeping these updated is important. Secure software also needs to be run on infrastructure, which must itself be up-to-date and configured securely.

When writing and committing code, engineers must ensure they are **never** commit secrets (i.e database passwords, access keys or other sensitive config) into source control or documentation.

New endpoints and pages must have the correct authentication and authorisation checks in place.

## Package Dependency Management

When including packages/dependencies (internal or external) developers must not use a floating package version, e.g. :
- Do:
  - Node.js: ```"dependencies": { "ExamplePackage": "2.0.1" }```
  - C#: ```<PackageReference Include="ExamplePackage" version="2.0.1" />```
- Don't: 
  - Node.js: ```"dependencies": { "ExamplePackage": "^2.0.1" }```
  - C#: ```<PackageReference Include="ExamplePackage" version="2.0.*" />```

## Performant Code

Engineers must ensure the code they write is performant. This refers both to ensuring individual actions and pages are loaded within an acceptable timeframe, _and_ ensuring that functionality does not degrade with large datasets. In particular it is important to perform testing with live-like datasets to ensure the software will behave as expected.

> _NOTE: specific non-functional requirements for acceptable performance will be defined at a later date._

The Microsoft article on [.NET Core performance best practices](https://docs.microsoft.com/en-us/aspnet/core/performance/performance-best-practices?view=aspnetcore-5.0) is very helpful.

### General performance tips

Use caching where ever it is possible and appropriate. The Quartex [caching guidelines](/6.-Engineering/Structure-and-Patterns/Caching) contain mechanisms for a range of different types of caching, including the caching service calls for retrieving data, and output caching to cache entire pages. The fastest way of doing work is to not have to do the work at all! 

Use `async`/`await` calls wherever possible. The async pattern allows the operatic system to assign idle CPU capacity to a thread that has work to do, instead of keeping the thread busy. Whilst it may be difficult to see much of a difference when developing locally, using `async`/`await` allows a webserver to handle many more requests in parallel.

### Entity Framework tips

When retrieving data from databases, use `.Include()` calls only where strictly necessary. Whilst it might be quite convenient, it is likely that with a large dataset, the increased amount of data returned will have a performance impact which may not be apparent when developing locally. This simply further re-enforces the need to test with live-like datasets.

Avoid using queries that Entity Framework will not be able to convert to SQL. A common mistake is to use `.ToLowerInvariant()` in a `.Where()` clause to perform a case-insensitive search. In these scenarios, Entity Framework will translate as much as possible into SQL, but then retrieve the rest of the data set and perform the rest of the query in memory - potentially resulting in a huge dataset being retrieved from the database.

E.g. consider the following fictitious query which retrieves an asset that matches a given path, where deleted is false.

```cs
var children = _unitOfWork.Assets.Where(a => a.Deleted == false && a.Path.ToLowerInvariant() == pathToSearchFor);
```

In this example, since EF is unable to translate `.ToLowerInvariant()` into SQL, it will effectively run a query like `select * from Assets where Deleted=0` and then run the `Path.ToLowerInvariant() == pathToSearchFor` comparison in memory, on every single returned row. For a very large database, this sort of subtlety can be cripplingly slow!

Avoid calling `ToList()`/`ToListAsync()` to early as this will result in a call to the database to retrieve data, ensure that as much as possible can be filtered out, using `Where()` 

```cs
var qry = _uow.Assets.GetAll() //still just a query at the moment, no call to the database

if(someClause)
	qry = qry.Where(…);
if(someClause)
	qry = qry.Where(…);

var list = qry.ToList() //now call is made to the database with applied filters

```
