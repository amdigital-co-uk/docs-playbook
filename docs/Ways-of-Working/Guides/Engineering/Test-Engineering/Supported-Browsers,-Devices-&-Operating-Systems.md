---
title: Supported Browsers, Devices & Operating Systems
authors: 
- Karen Farrell
reviewed: [2023-12-20]
reviewer:
next-review: [2025-01-31]
---


## Who is this for?

This page documents the browsers, devices and operating systems we support and therefore test against.  These must be considered when designing, coding, as well as testing AM applications.

## Introduction

With such a wide range of browsers, devices and operating systems available, cross browser testing has become a crucial part of the Software Development Lifecycle.

It is important to compare a web applications functionality and design across multiple browsers and platforms to ensure consistent behaviour, functionality and user experience.

Styling and effects such as mouse-over, pop-ups and fonts can vary significantly across browsers as well as features such as page navigation.  Whilst some of these differences can be impossible to resolve, by cross-browser testing we can ensure our users are able to access all content and execute all functionality without any major issues.

## Testing Considerations

As there are so many combinations of screen sizes, devices, operating systems and browsers to choose from, and limited time and resource to test, it is important that we establish the intended range of configurations that we support to ensure the best coverage of our users.
Ideally, it is best to view and test these applications on physical devices with the same configuration as the end user.  However, in practice this is not always possible and therefore we use BrowserStack.  BrowserStack is a cloud-based cross-browser testing tool that enables us to test our websites across various browsers on different operating systems and mobile devices without having to install virtual machines or emulators.

The testing we can perform via BrowserStack is limited (e.g. running our accessibility tooling can be tricky) therefore, we also have a Macbook Mini available that we can remotely access to test against Safari (see KnowledgeBase for guidance).

## What we support

Evaluating the analytics available to us, it has been agreed to support the following as a minimum:

### Quartex Applications

### DAM & CMS

Browsers:

* Chrome / Edge (latest and preceding versions)
* Firefox (latest and preceding versions)
* Safari (latest and preceding versions)

Operating Systems:

* Windows
* MacOS

Devices:

* Desktop
* Laptop

### Published Sites

Browsers:

* Chrome / Edge (latest and preceding versions)
* Firefox (latest and preceding versions)
* Safari (latest and preceding versions)

Operating Systems:

* Windows
* Android
* MacOS
* iOS
 

Devices:

* Desktop
* Laptop
* Tablet
* Mobile Phone

### Other Applications

### Internal Applications

This covers applications such as the Admin tool and AM Portal

Browsers:

* Chrome (latest version)

Operating Systems:

* Windows

Devices:

* Desktop
* Laptop

### Framework & White Label

Browsers:

* Chrome / Edge (version TBC)
* Firefox (version TBC)
* Safari (version TBC)

Operating Systems:

* Windows
* MacOS

Devices:

* Desktop
* Laptop
