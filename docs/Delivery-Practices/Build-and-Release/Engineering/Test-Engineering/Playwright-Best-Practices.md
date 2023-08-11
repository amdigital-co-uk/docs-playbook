---
title: Best Practices when using Playwright
authors: 
- Jees Mathew & Karen Farrell
reviewed: [yyyy-mm-dd]
reviewer:
next-review: 01/09/2024
---

## Introduction
This document outlines best practices to follow when writing Playwright test scripts.

## Locating elements
It is important to use a locator that is robust and does not depend on the DOM structure, therefore we have the following best practices in place.

To make our tests resilient, we prioritise user-facing attributes and explicit contracts when locating elements on a page.  This could be text, a button name, an element's aria-label etc.

Playwright built-in locators:

- page.getByRole() to locate by explicit and implicit accessibility attributes.
- page.getByText() to locate by text content.
- page.getByLabel() to locate a form control by associated label's text.
- page.getByPlaceholder() to locate an input by placeholder.
- page.getByAltText() to locate an element, usually image, by its text alternative.
- page.getByTitle() to locate an element by its title attribute.


If an element cannot be located by any of these, then we look for data-test IDS (for more info click [here](https://playwright.dev/docs/locators#locate-by-test-id)).  **Software Engineers will support creating the data-test-IDs where needed.**

Playwright built-in locators:

- page.getByTestId() to locate an element based on its data-testid attribute


We use CSS or XPath locators as **absolute last resort**.  CSS and XPath are not recommended as the DOM can often change leading to non resilient tests. Instead, we try to use a locator that is close to how the user perceives the page such as role locators or define an explicit testing contract using test ids as described above.

If you absolutely must use CSS or XPath selectors, you can use

- page.locator()

For further examples of these locators, please follow the Playwright documentation found [here](https://playwright.dev/docs/locators#quick-guide)


## BDD
### Writing test scenarios using Cucumber
// TO DO

### Creating Step Definitions
// TO DO

## References
- [Best Practices - Locators](https://playwright.dev/docs/best-practices#use-locators)
- [Using Test IDs](https://playwright.dev/docs/locators#locate-by-test-id)