---
title: Playwright Test Automation Guidelines
authors: 
- Karen Farrell 
- James Perry
tags:
    - Default
    - Test
---

## Introduction

This document outlines best practices to follow when writing Playwright test scripts.

## Locating selectors

When planning testing at the readying phase of a work item, locators must be considered.  This allows Engineers to plan any additional work needed in order to enable our best practices.

It is important to use a locator that is robust and does not depend on the DOM structure.

To make our tests resilient, we prioritise user-facing attributes and explicit contracts when locating elements on a page.  This could be text, a button name, an element's aria-label etc.

Playwright recommended built-in locators:

- page.getByRole() to locate by explicit and implicit accessibility attributes.
- page.getByText() to locate by text content.
- page.getByLabel() to locate a form control by associated label's text.
- page.getByPlaceholder() to locate an input by placeholder.
- page.getByAltText() to locate an element, usually image, by its text alternative.
- page.getByTitle() to locate an element by its title attribute.


If an element cannot be located by any of these, then we look for data-test IDs (for more info click [here](https://playwright.dev../../locators#locate-by-test-id)). 
 
 **Some Test Engineers can support creating the data-test-IDs where needed, otherwise a Software Engineer can assist.**

Playwright recommended built-in locators when using data-test-IDs:

- page.getByTestId() to locate an element based on its data-testid attribute

For further examples of these locators, please follow the Playwright documentation found [here](https://playwright.dev../../locators)


We **NEVER** use CSS or XPath locators.  CSS and XPath are not recommended as the DOM can often change leading to non resilient tests. Instead, we use a locator that is close to how the user perceives the page such as role locators or define an explicit testing contract using test ids as described above.

**Keep selectors up-to-date:** Regularly review and update your selectors to ensure they are still accurate and efficient. When the application under test changes, be proactive in updating the selectors in your page files to prevent your tests from breaking


## Use of annotations for skipping tests with Native Playwright

This relates to working on these repo's:

- Eden (DAM E2E tests)

- Qts-Clients (Client Manager E2E Tests)

- Qtui-front-end (Front-End E2E Tests)

When maintaining tests, it is important to use the correct annotations to handle test logic effectively as required, ie, skipping tests.  This is to ensure that the entire test suite is not unnecessarily run and to prevent false negatives. Integrating annotations into our Playwright workflow can dramatically improve our testing efficiency and enable us to gain precise control over which tests run and how they behave.

For whichever annotation we use, it is imperative that we put a comment above the annotation to justify why it's being used, to ensure it's clear to other team members.

For further examples of annotations playwright support, please follow the Playwright documentation found [here](https://playwright.dev/docs/test-annotations)

**In summary:**

- Use `test.only` to run a single test. (Playwright will only run the test with the `test.only` annotation applied to it).

This should be used in instances where we want to focus on a single test and ignore all other tests. 

**We should **NEVER** merge tests with `test.only` annotations into the main branch, but it has it's uses when executing tests locally or on work / feature branches at times.**

- Use `test.fixme` to mark a test that is known to be failing and requires a fix. (Playwright will not run the test and it will be skipped).

This should be used in instances where the test logic is fine but the test is failing due to a known defect. There should be a BLI in place to fix this within the next 2 sprints and we are aware a fix is in the works. Its imperative we include a comment above the `test.fixme` annotation to explain why the test is failing, along with a reference ID of the DevOps BLI or the halo ticket ID so there is some form of traceability.

**We can merge tests with `test.fixme` annotations into the main branch, but only temporarily. This should then be reverted back to `test` once the test is fixed.**

- Use `test.skip` to skip a test. (Playwright will not run the test and it will be skipped).

There are 4 main instances why we would use this annotation:

1 - To skip a test temporarily in order to focus on other tests. This can be beneficial when running tests *locally* or on work / feature branches, but shouldnt be merged to main in these instances. 

2 - To skip a work in progress test, whereby the logic in the test would fail at this particular instance in time because it's not ready for testing yet, but we want to keep the test in the codebase for future reference or enhancement. (Instances of this are rare and we should be wary of merging incomplete work into the main branch, therefore its important to review the skipped test frequently and to have a plan of action to complete the test logic so it can be included in the test suite).

3 - To skip a test under certain conditions, such as not running the test on a specific browser if it is flaky. For example:

            import { test, expect } from '@playwright/test';

            test('Safari-only test', async ({ page, browserName }) => {
            test.skip(browserName !== 'webkit', 'This feature is Safari-only');
            // ...
            });

4 - To skip a failing test, under instances when we are unsure of the timeframe of the fix. Again, its imperative we include a comment above the `test.skip` annotation to explain why the test is failing, along with a reference ID of the associated created DevOps BLI on our test engineer minmi board [here](https://dev.azure.com/AMDigitalTech/Platform%20Development/_boards/board/t/Minmi/Backlog) so there is some form of traceability. In the instance of a failing test with a known fix in the works, we should use `test.fixme` instead, explained above.

**We can merge tests with `test.skip` annotations into the main branch, but it is important that we review these tests frequently to ensure they are not forgotten.**


!!! info "Use of `test.fail` or `@fail`"
    We do **NOT** support the use `test.fail` or `@fail` to mark a test that is known to be failing. Playwright will run the test and it will fail in this instance but we put emphasis on fixing the test rather than marking it as a failure. Instead we use SKIP or FIXME annotations dependent on the circumstances, as explained above.


## Use of annotations for skipping tests with Playwright BDD (Cucumber)

This relates to working on these repo's:

- Eden (regression tests)

- Qtui-front-end (Front-End regression Tests)

The theory is the same as explained above, however the logic works slightly differently:

- Instead of `test.only`, we use the `@only` tag in the feature file

- Instead of `test.skip`,  we use the `@skip` tag in the feature file

- We do **NOT** support the use of `@fail` to mark a test that is known to be failing.

![Example](1.png)  