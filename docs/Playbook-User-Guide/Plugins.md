---
title: Managing Plugins
authors: 
- Dave Arthur 
next-review: 2023-03-31
---

# Managing Plugins

MkDocs allows the use of plugins to extend the basic functionality for a wide variety of purposes. Adding plugins to this playbook is not expected to be frequent, but if doing so consult the MkDocs [guide to using plugins](https://www.mkdocs.org/dev-guide/plugins/), and consult the documentation for whatever plugin is to be used.

When adding plugins to this playbook, they must also be included in the following locations:

- The publish site workflow: `<REPO>/.github/workflows/publish-site.yml`
- The local run script: `<REPO>/run.bat`

!!! danger
    
    Failing to update the workflow when adding a plugin will break the build, and cause playbook updates to not get published.

