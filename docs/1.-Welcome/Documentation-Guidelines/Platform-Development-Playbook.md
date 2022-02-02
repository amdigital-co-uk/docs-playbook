---
title: Playbook Documenation
authors: 
- Ed Earle 
- Dave Arthur 
reviewed: 2021-09-29
reviewer:
next-review:
---


## Who is this for?
This playbook outlines the continually evolving frameworks, processes, and practices that are used by the Platform Development Division to enable us to reliably deliver against [our collective mission](/1.-Welcome/Mission).

All members of the Platform Development Division - Product Management, Software Engineering, Test Engineering, Platform Support.

## Ownership and Responsibility
Every member of the division is responsible for ensuring that this playbook is up to date and accurate.

!!! note "Ownership" 

    When you create, review, or modify a document, **you are responsible** for ensuring that it is _well written_ and has been _peer reviewed_, and that _review date is set_.

## Tooling

This playbook is build using [Markdown](https://www.markdownguide.org/) documents, a simple text editor designed for documenation.

Specifically, it is build on [MKDocs](https://www.mkdocs.org/), using the [Material for MKDocs](https://squidfunk.github.io/) theme.

It is stored in GitHub, and published with [GitHub Pages](https://pages.github.com/)

MKDocs and Material for MKDocs extend the functionality of Markdown, allowing you to include visually richer content.

You can edit the documents usng any markdown editor, incuding GitHub. Read [How to Contribute](#how-to-contribute) for a step by step guide.

## Structure

### Page header

You must always provide a _page header_, using the following YAML heading set at the very top of each document in the playbook. 

```
---
title: [Fascinating subject]
authors: 
- [Given name] [Family name]
- [John] [McWriter]
reviewed: [yyyy-mm-dd]
reviewer:
next-review:
---
```

!!! note 

    Dates must be formatted yyyy-mm-dd (e.g. 2022-08-31, [following ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)) 

    You can insert as many authors reqired, each author on a new line. Please make sure you use full name


The only exception if child pages, when they are used specifically for breaking down larger subjects, where the authors are the same, and where they would naturally be reviewed alongside the parent. This this instance you must still include a title.

```
---
title:
---
```

### Headings

The main heading (e.g. H1) for each page is automatically generated from the title field. Therefore you should not add any top level headings to the page content 

Use structured headings starting at H2 using ##. For subheading, increment the hashes (### for H3, ### for H4).

```
## First section
Lorum ipsum UI pipeline, or herding cats, blue sky thinking, yet we need to leverage our synergies.

## Second section
Lorum ipsum enough to wash your face, put a record on and see who dances. Bob called an all-hands this afternoon offline this discussion deliverables for deep dive but land it in region.

### First child of second section
Lorum ipsum who's responsible for the ask for this request? run it up the flag pole so disband the squad but rehydrate as needed.

```

!!! warning "Table of contents"

    The table of contents is automatically generated, but will always exclude top level headings (i.e. H1). This is why you should start at H2! See the one on this page for example!

## General tips

* Start by explaining who and what the document is for
* Use sub pages if your content is large
* Use bullet lists to simplify key points
* Use diagrams to express more complex ideas, such as processes


## Reviewing
Documents should be peer reviewed after initial publication, and following significant revisions. They should also be subject to periodic reviews to ensure they are up to date, relevant, and accurate.

### Peer Reviewing
The primary purpose of a review is to ensure that the documentation is as useful as it can be. 

- The peer reviewer should carefully read and understand the content of the document. Consider the audience of the document and its purpose. 
- Ensure the page header is populated and accurate, and that a review date has been provided.
- Check for typos and errors if possible, although this is not the primary purpose of review. 
- Provide constructive feedback to the author for revision.

### Periodic Reviews
On or around the review date, the document should be checked for validity. 

The purpose of a review is to ensure that the document is still as useful as it can be, or deleted if it is no longer required.

Updates may happen at any time, but it is possible that changes to frameworks, processes, and practices have happened and not been documented. 

- After a review, ensure that the Next Review Date in the page header is updated, regardless of whether any changes have been made.
- If a major revision is performed, add the name of the revising author(s) to the page header, and ensure that the revision is peer reviewed.

## How to Contribute

// TODO: Create contributing guide, including tooling and submitting pull requests

Oh no! This bit hasn't been done yet!

Perhaps you could do it?
