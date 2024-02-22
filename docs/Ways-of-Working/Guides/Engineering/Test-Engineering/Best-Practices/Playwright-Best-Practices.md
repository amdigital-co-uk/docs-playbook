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

**Keep selectors up-to-date:** Regularly review and update your selectors to ensure they are still accurate and efficient. When the application under test changes, be proactive in updating the selectors in your page files to prevent your tests from breaking