---
title: BDD best practices for writing test scenarios
authors: 
- Mihajlo Stojanovski & James Perry
reviewed: [yyyy-mm-dd]
reviewer:
next-review: 01/09/2024
---

## Introduction
This document outlines Behavior-Driven Development best practices to follow when writing test scenarios

### <u>Behavior-Driven Development (BDD)</u>
BDD test scenarios play a crucial role when creating and maintaining the test suite in Adam Matthew Digital. The BDD scenarios are written in the Gherkin format which is a DSL (Domain Specific Language) that allows you to describe the application's behavior in a human-readable format, and also allows these scenarios to be reused later in multiple test suites.


Let’s first cover the basic principles of writing BDD test scenarios using Gherkin syntax.

### <u>Understanding Gherkin syntax - Creating feature files</u>


Gherkin is a very simple language that uses a set of keywords to define the structure and behavior of your tests. It is easily readable by both non-technical and technical members of the team.

These are the primary components of Gherkin syntax:

•	**Feature**: A high-level description of a software feature or functionality being tested. It is always located on the top of the feature file.

•	**Scenario**: A specific use case of the feature that is being tested.

•	**Given**: Describes the initial state or preconditions of the system before the scenario.

•	**When**: Describes the action or event that triggers the scenario.

•	**Then**: Describes the expected outcome or postconditions of the system after the scenario.

•	**And**: Successive step

The BDD test scenarios reside in the appropriate feature files, that reside in a special folder called **‘features’**, and have the **‘.feature’** file extension associated with them.

Here is an example of a feature file:

**Feature**: User authentication on the AMD website

  **Scenario**: Successful login

**Given** the user is on the AMD login page

**When** the user enters valid username and password

**And** clicks on the Login button

**Then** the user should be redirected to the dashboard


### <u>Writing meaningful Feature descriptions</u>
The feature file starts with the feature description. The purpose of the Feature keyword is to provide a clear understanding of the software feature that is being tested, and to group related scenarios.

The first primary keyword in a Gherkin document must always be Feature, followed by a : and a short text that describes the feature.

These description lines are ignored by Cucumber at runtime, but are available for reporting.

•	Be concise and descriptive, focusing on the functionality being tested.
•	Avoid technical jargon and write in a language that both technical and non-technical stakeholders can understand.

### <u>Defining clear and concise Scenarios</u>
Each Scenario represents a single, specific example of the feature's behavior. Please follow these guidelines when writing the scenarios:

•	Use simple language that is easy to understand for both technical and non-technical stakeholders.

•	Focus on one specific aspect or use case of the feature being tested.

•	Ensure that the Scenario can be executed independently and does not rely on the state of other Scenarios.


### <u>Creating reusable and modular Step Definitions</u>
One of the greatest benefits of using BDD is the reusable scenarios or to be more precise the reusable step definitions, and this is important to understand to fully grasp the significance of the BDD approach.

Let’s start off with explaining the approach.

As we have already seen, **Given, When, Then,** And represent test steps in each scenario.

Each of these steps has a description or a step definition, for an example:

**Given** the user is on the AMD login page

In this case a step definition would be ‘a user is on the AMD login page’.

Behind this step definition there is code that is executed.
This code is in the step definition file, which resides in the ‘step-definition’ folder.
The grouping of these step definitions in the AMD case are based on the functionality’s location.
In the hypothetical example above that would be something like the step-definition file “LoginPageDefinitions.ts”

This step definition in the feature file can be reused elsewhere as well, in other scenarios.






For an example:

**Scenario**: Successful login from the staging site 

**Given** a user is on the staging site

**When** clicks on the staging site Login button

**Then** the user should be redirected to the AMD login page

**When** the user is on the AMD login page

**And** the user enters valid username and password

**And** clicks on the Login button

**Then** the user should be redirected to the dashboard

As you can see in this hypothetical scenario, the ‘the user is on the AMD login page’ was moved to the When step.

That said, this just shows the infinite capabilities of these tests and how different scenarios can be made by combining these test steps.

<u>**To create reusable and modular Step Definitions, follow these best practices:**</u>

•	Write Step Definitions that are concise, focused, and implement only the necessary actions for the given step. 

In the example above, a clear distinction was made:
‘clicks on the staging site Login button’
‘clicks on the Login button’

This is because, the selectors or the actions taken, for the login button, might be different on the staging site.

•	Use expressive and clear language in your Step Definitions to ensure they are easy to understand and maintain.

By following these best practices, you can create BDD test scenarios that are easy to read, understand, and maintain, allowing both technical and non-technical stakeholders to collaborate effectively on the testing process.

### <u>Creating and Organizing Step Definition Files</u>
As we said earlier, the Step definition files contain the code that connects the Gherkin steps in your feature files to the actual implementation of the test. These files are crucial for maintaining the readability and modularity of your BDD test suite. Here are some best practices for creating and organizing step definition files:

1.	Naming convention: Use a consistent naming convention for your step definition files. A common approach is to name them based on the feature or page they are associated with, followed by the word "Definitions" (e.g., DocumentsListDefinitions.ts, ListPageDefinitions.ts).

2.	Folder structure: Store step definition files in a dedicated folder, typically named step-definitions. This keeps your test code organized and makes it easier to locate step definitions.

3.	One-to-one mapping: Create a one-to-one mapping between feature files and their corresponding step definition files. This approach simplifies the process of locating the code related to specific scenarios. (Example: If you have a loginPage.ts create a LoginPageDefinitions.ts step-definition file).

4.	Modularity: Write modular step definitions by breaking down complex actions into smaller, reusable functions. This practice promotes maintainability and enables you to reuse code across multiple steps and scenarios.

5.	Parameterization: Use parameters in your step definitions to make them more flexible and reusable. This allows you to write more concise and expressive test scenarios. In the example below, “QA”, “QA members” and “<SearchName>” are the parameters that can be changed. 


Here is an example hypothetical step definition to fully understand the explanation above 

![Example](1.png) 

Let’s take the ‘User conducts a search for "<SearchName>" filter input’.

This is how the code looks like in the step-definition file. Please notice the parametrization “{string}” for "<SearchName>". The same would apply for “QA” or “QA members”:

![Example](2.png)

As you can see we have a searchForValue method in the step-definition file.

This method resides in the membersDetailsPage.ts, which is located in the ‘pages’ folder.

![Example](3.png)


### <u>Page files</u>
A "page file" in the context of automated testing and the Page Object Model (POM) is a file that represents a specific page or a part of a web application. The page file contains a class or an object that encapsulates the selectors and actions specific to that page. This abstraction allows you to interact with the web application in a more maintainable, reusable, and readable way within your test suite.

As we saw with the example above, that is where we right the actions or methods that interact with the web elements.

Here are samples of methods that might reside in the pages file:

![Example](4.png) 

this.LoginButton is the selector for the login button, that also resides in the Page file.



## References
// TO DO