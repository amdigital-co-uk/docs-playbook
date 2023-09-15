---
title: Best Practices when using Playwright
authors: 
- Jees Mathew & Karen Farrell & Mihajlo Stojanovski & James Perry
reviewed: [yyyy-mm-dd]
reviewer:
next-review: 01/09/2024
---

## Introduction
This document outlines best practices to follow when writing Playwright test scripts.


## Selectors - all you need to know
Selectors play a crucial role in automation testing, as they are used to identify and interact with elements on a web page. Writing efficient and maintainable selectors is essential for creating a robust test suite. Here are some best practices and guidelines to follow when writing selectors:

1.	Use meaningful and descriptive names for selectors: Assigning clear and descriptive names to your selectors helps make your code more readable and maintainable. For example, instead of using a generic name like button, use a specific name like loginButton.

2.	Prioritize unique and stable attributes: When selecting an element, prioritize using unique and stable attributes, such as title, name, or unique id. These attributes are less likely to change and are more reliable for locating elements on the page. If unique attributes are not available   , use the data-test-ids to pinpoint the element.

3.	Avoid using absolute and complex XPath expressions: Absolute XPath expressions are fragile and more likely to break if there are changes to the page structure. Use relative XPath or CSS selectors when possible, as they are generally more maintainable and easier to read. 

4.	Leverage Playwright's built-in selector engines: Playwright provides a variety of built-in selector engines like css, xpath and id that can be combined to create powerful and maintainable selectors. Use these engines to build reliable and efficient selectors for your page elements.

5.	Group related selectors together: In your page files, group selectors related to a specific section or component together for better organization and easier maintenance. This can help improve the readability of your code and make it easier to locate selectors when you need to update them.

6.	Keep selectors up-to-date: Regularly review and update your selectors to ensure they are still accurate and efficient. When the application under test changes, be proactive in updating the selectors in your page files to prevent your tests from breaking.


## Locating selectors
When planning testing at the readying phase of a work item, locators must be considered.  This allows Software Engineers to plan any additional work needed in order to enable our best practices.

It is important to use a locator that is robust and does not depend on the DOM structure.

To make our tests resilient, we prioritise user-facing attributes and explicit contracts when locating elements on a page.  This could be text, a button name, an element's aria-label etc.

Playwright recommended built-in locators:

- page.getByRole() to locate by explicit and implicit accessibility attributes.
- page.getByText() to locate by text content.
- page.getByLabel() to locate a form control by associated label's text.
- page.getByPlaceholder() to locate an input by placeholder.
- page.getByAltText() to locate an element, usually image, by its text alternative.
- page.getByTitle() to locate an element by its title attribute.


If an element cannot be located by any of these, then we look for data-test IDs (for more info click [here](https://playwright.dev/docs/locators#locate-by-test-id)).  **Software Engineers will support creating the data-test-IDs where needed.**

Playwright recommended built-in locators when using data-test-IDs:

- page.getByTestId() to locate an element based on its data-testid attribute

For further examples of these locators, please follow the Playwright documentation found [here](https://playwright.dev/docs/locators)


We **NEVER** use CSS or XPath locators.  CSS and XPath are not recommended as the DOM can often change leading to non resilient tests. Instead, we use a locator that is close to how the user perceives the page such as role locators or define an explicit testing contract using test ids as described above.

## Testing, committing code and PR reviews
The tests are developed locally, on your local environment. 

To ensure that the tests are in order prior to sending them for a PR review, we need to make sure that they are compatible with the latest version of the main branch.

We either write git commands or use GitHub desktop. If you are not comfortable with GitHub, please ask for help from a fellow Engineer. 

To run the tests be aware that if you are using a MacOS, there is a separate command. Here are the commands for the Regression suite:

**Windows:**
npm run test features/ theFeatureFile.feature --env=qa;

**MacOS:**
npm run test:mac features/theFeatureFile.feature --env=qa;


After your local tests pass you need to do the following:

**1.**	Commit your latest code on the branch you have created.

Here are the git commands, but you can also use [Github desktop for all these steps](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/keeping-your-local-repository-in-sync-with-github/syncing-your-branch-in-github-desktop#merging-another-branch-into-your-project-branch)

git checkout your-branch
git add .
git commit -m "Your commit message"
git push


**2.**	Checkout on the main branch and pull the latest changes.

git checkout main
git pull

**3.**	Go back to your local branch and merge the latest changes from main

git checkout your-branch
git merge main

**4.**	Run the tests again and make sure that they pass. 

After you are done with the tests, a good practice is to click through all the files in the VS Code Explorer just to double check for any undetected errors. For an example, if you are working on the Regression suite, check through, by simply clicking on the files in the step-definitions folder, the pages folder and the features folder, and look out for any errors. This is just a precautionary measure.

## Code reviews
When all the tests are done and tested on your local environment, then you will need to commit the code, and push it to GitHub, where you need to create a Pull Request.

You can create the pull request from GitHub Desktop or directly on GitHub.

Here are the git commands, but you can also use [Click here for more information on how to create a PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request)

Enter a title with a short description for the PR. Also please make sure you add two reviewers. The reviewers usually are your fellow Engineers. 

After the PR is confirmed and approved, you can merge it via GitHub and delete the branch i.e. just simply follow the procedure on GitHub. 

## Resolving Conflicts in Pull Requests

Conflicts can sometimes arise when attempting to merge your branch into the main branch, especially if multiple team members are working on the same files. Certain code might overlap etc. 

Be very cautious with the merging process if conflicts happen. it is essential to resolve these conflicts before the PR can be approved and merged. Tools like VS Code with prompt you all the conflicts and will ask of you to resolve them.

Here are some tips and tricks for effectively resolving conflicts during PRs:

**1.**	Stay up-to-date: Regularly sync your branch with the main branch to minimize the chances of conflicts arising. This allows you to address any potential issues early on and helps to keep your code compatible with the latest changes in the main branch.

**2.**	Understand the conflict: Before attempting to resolve a conflict, make sure you understand the changes made in both branches and how they conflict with each other. This will help you make informed decisions when resolving the conflict and ensure that the correct code is preserved.

**3.**	Communicate with your team: If you are unsure about how to resolve a conflict or need clarification on the changes made by another team member, reach out to them for assistance. Open communication between team members can help prevent misunderstandings and ensure that the best possible solution is implemented. If not sure, please set up a resolving conflict meeting and go step by step to check conflicting code and work the issue out together.

**4.**	Be cautious with automatic resolution: While some conflicts can be resolved automatically by Git, it is important to review the changes made during the automatic resolution process. Make sure that the merged code is correct and does not introduce new issues or inconsistencies.

**5.**	Test your changes: After resolving the conflict and merging the branches, thoroughly test your changes to ensure that everything is working as expected. This will help catch any issues that may have been introduced during the conflict resolution process and ensure that the merged code is stable and functional.

**6.**	Document your resolution: In the PR, explain how you resolved the conflict and why you chose that particular solution. This documentation can be helpful for your reviewers to understand your thought process and can serve as a reference in case similar conflicts arise in the future.

By following these tips and tricks for resolving conflicts during PRs, you can help maintain the integrity and stability of your codebase, while ensuring a smooth and efficient merging process.



## References
- [Playwright - Locators](https://playwright.dev/docs/locators)
- [Playwright Best Practices - Using Locators](https://playwright.dev/docs/best-practices#use-locators)
- [Using Test IDs](https://playwright.dev/docs/locators#locate-by-test-id)