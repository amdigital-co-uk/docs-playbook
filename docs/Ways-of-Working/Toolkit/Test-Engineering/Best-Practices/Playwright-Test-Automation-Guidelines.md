---
title: Playwright Test Automation Guidelines
authors: 
- Jees Mathew 
- Karen Farrell 
- Mihajlo Stojanovski 
- James Perry
tags:
    - Default
    - Test
---

## Introduction

This document outlines best practices to follow when writing Playwright test scripts.

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


If an element cannot be located by any of these, then we look for data-test IDs (for more info click [here](https://playwright.dev../../locators#locate-by-test-id)).  **Software Engineers will support creating the data-test-IDs where needed.**

Playwright recommended built-in locators when using data-test-IDs:

- page.getByTestId() to locate an element based on its data-testid attribute

For further examples of these locators, please follow the Playwright documentation found [here](https://playwright.dev../../locators)


We **NEVER** use CSS or XPath locators.  CSS and XPath are not recommended as the DOM can often change leading to non resilient tests. Instead, we use a locator that is close to how the user perceives the page such as role locators or define an explicit testing contract using test ids as described above.

**Keep selectors up-to-date:** Regularly review and update your selectors to ensure they are still accurate and efficient. When the application under test changes, be proactive in updating the selectors in your page files to prevent your tests from breaking

## Use of annotations for skipping tests

When writing tests, it is important to use the correct annotations to skip or fail tests as required.  This is to ensure that the test suite is not unnecessarily run and to prevent false negatives. Integrating annotations into our Playwright workflow can dramatically improve our testing efficiency and enable us to gain precise control over which tests run and how they behave.

For whichever annotation we use, it is imperative that we put a comment above the text to justify why the annotation is being used. This is to ensure that the annotation is not forgotten about and that it is clear to other team members why the annotation is being used.

For further examples of these annotations, please follow the Playwright documentation found [here](https://playwright.dev/docs/test-annotations)

In summary:

- Use `test.skip` to skip a test that is not yet implemented or is not relevant to the current test run. Playwright will not run the test and it will be skipped. 

This should be used in instances where we want to bypass a test temporarily in order to focus on other tests. For example, the logic in the test would fail at this particular instance in time, but we want to keep the test in the codebase for future reference. We should **NEVER** merge tests with `test.skip` annotations into the main branch.

- Use `test.fixme` to mark a test that is known to be failing and needs to be fixed. Playwright will not run the test and it will be skipped



- Use `test.fail` to mark a test that is known to be failing and should fail. Playwright will run the test and it will fail.

This should be used in instances where we have a bug in the test that needs to be fixed. Its imperative we include a comment above the `test.fixme` annotation to explain why the test is failing and include a the reference ID of the Halo ticket. We can merge tests with `test.fixme` annotations into the main branch, but it is important that we rever this back to `test` once the bug is fixed.