---
title: Sections and Structures
authors:
  - Ed Earle
reviewed:
reviewer:
next-review: 2023-02-01
---

## Structure

The markdown documentation is structured into folders and subfolders. All documentation lives within the docs folder of the repository.

The Playbook homepage lives in the docs folder and is called index.md.

The folders within the docs folder represent each of the Playbook's Sections.

``` none
.
├─ docs/
    └─ index.md                 <-- this is the Playbook homepage
    ├─ 1.-Section-Name/
        └─Topic-One/            <-- this is the Subsection without a homepage
        |   └─Topic-Document.md
        └─Topic-Two/   
        |   └─index.md          <-- this is the Subsection with a homepage
        |   └─Topic-Two-Document.md
        └─index.md              <-- this is the Section Homepage
        └─Another-Document.md   
        └─Topic/
```

## Sections

Sections refer to the top level groups of content, e.g. [6. Playbook User Guide](../6.-Playbook-User-Guide/).

Sections are numbered so that they are displayed in a specific order.

Each Section _may_ have multiple other pages or subsections.

Each Section _must_ have a Section homepage, this will be called index.md.

## Subsections

Subsections are folders within a Section.

A subsection _may_ have a homepage, in which case is must be named index.md.

If a subsection does not have a homepage, the subsection name will appear in the Playbook navigation menu as a grouped header for the pages within it.

Subsections are useful for grouping topic documentation where one page would not suffice.

## Creating and Managing Sections

