---
title: Page Layouts
authors:
  - Ed Earle
reviewed:
reviewer:
next-review: 2023-02-01
---

## Structure

Good page structures make reading and maintaining documents easy, and ensure that the documenation displays correctly. There are only a few rules that need to be follow so please take care to do so.

## Page Header

You **must** always provide a _page header_. This adds metadata which use used to improve the presentation of the page and support maintenance.

A YAML heading should appear at the very top of each document in the playbook. Parent pages will have need more meta-data, child pages (which extend the topic of the parent to support easier navigation) only require a simple heading.

### Parent Pages

Parent pages should have a full header block. A section may have many parent pages, and a parent page may not have any child pages.

``` yaml
---
title: [Fascinating Subject] <-- Always specify, this will become the page heading and show in the nav
authors: 
- [Given name] [Family name] <-- Always specify
- [John] [McWriter]
reviewed: [yyyy-mm-dd] <-- Only specify after first review
reviewer: [Given name] [Family name] <-- Only specify after first review
next-review: [yyyy-mm-dd] <-- Always specify
---
```

!!! note
    Dates must be formatted yyyy-mm-dd (e.g. 2022-08-31, [following ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)).
    You can insert as many authors required, each author on a new line. Please make sure you use full name.

### Child Pages

For use with child pages, which are used specifically for breaking down larger subjects, where the authors are the same, and where they would naturally be reviewed alongside the parent. This this instance you must still include a title.

``` yaml
---
title:
---
```

## Headings

The main heading (e.g. H1) for each page is automatically generated from the title field (as specified in the page header).

Never include a top level heading on a page like this:

``` md
# Top level headings should not be Used
```

Use structured headings starting with a second level heading using ##. For subheading, increment the hashes (### for level 3, ### for level 4).

``` markdown
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

- Start with a simple summary of the document purpose
- Use sub pages if your content is large
- Use bullet lists to simplify key points
- Use diagrams to express more complex ideas, such as processes
- Use a spell checker in whatever editor you are using, set it to UK English. In VSCode there numerous plugins.
