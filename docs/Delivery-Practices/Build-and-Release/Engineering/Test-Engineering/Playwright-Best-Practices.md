---
title: Best Practices when using Playwright
authors: 
- Jees Mathew & Karen Farrell
reviewed: [yyyy-mm-dd]
reviewer:
next-review:
---

## Introduction
This document outlines best practices to follow when writing Playwright test scripts.

## Identifying locators
1. The main rule-of-thumb when selecting a locator for an element, is to try an use one that is either visible to the user or one the user interacts with. This approach allows the test to fail when any change that is visible to the user occurs on the webpage.\
 __Example__\
    Scenario: A button with text is visible to the user and the button element has an unique ID in the HTML.\
    Locator: The test should use the button with text rather than refer to the ID. 


1. It is important to use a locator that is robust and does not depend on the DOM structure.

1. The best locators to use for elements are label names, button name, text etc.

1. The above can be difficult to achieve if the interested element is an icon or an image. In these cases, it is advisable to look for Aria-Labels. This is because although the user does not see an Aria-Label, it is the next best thing when using assistive technologies and therefore are elements that are used to directly interact with the webpage.

1. If an element does not have any labels, text or Aria-Labels then it is advisable to look for data-test IDS (see references for more info).

1. It is **not advised** to use element IDs, names, CSS locators or any other locators that is not visible to the user.  Such locators must only be used as a last resort.

## BDD
### Writing test scenarios using Cucumber
// TO DO

### Creating Step Definitions
// TO DO

## References
- [Best Practices - Locators](https://playwright.dev/docs/best-practices#use-locators)
- [Using Test IDs](https://playwright.dev/docs/locators#locate-by-test-id)

