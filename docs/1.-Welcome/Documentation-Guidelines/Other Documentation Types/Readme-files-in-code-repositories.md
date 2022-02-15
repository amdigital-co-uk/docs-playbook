---
title: README files in code repositories
authors: 
- Dave Arthur 
reviewed: 
reviewer:
next-review: 01-05-2022
---

# README files

Every repository must have a file called `README.md` in the root folder. Using [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) files instead of a plain text file allows us to format documentation, add links and images to enrich the documentation. As an added bonus, they get rendered nicely when browsing the repository via the GitHub web UI.

## Why include a README at all?

Every repo must include a README file so that viewers know what the code does and how they can get started using it. Most importantly a README should serve to significantly reduce or remove friction when a new engineer starts working with a repository, so that they can start being productive as quickly as possible.

## Required sections

!!! note

    The layout for our README files is based loosely on the [Best README Template](https://github.com/othneildrew/Best-README-Template) project.

    The Azure DevOps [README guidelines](https://docs.microsoft.com/en-us/azure/devops/repos/git/create-a-readme?view=azure-devops) are also a useful reference.

Every README file must have the following sections:

- Overview
- Built with
- Getting started
- Usage
- Contributing

Whilst these sections are a minimum, and must appear on the README for every repository we manage, they don't need to be lengthy! A brief summary or link out to existing documentation elsewhere is acceptable.

### Overview

Provide a brief overview of the repository, and the problem it aims to solve.

### Built with

List the major technologies and frameworks used within the repository, as a bullet-point list. Ideally link out to some documentation for each item, this is especially important for technologies and frameworks outside our usual tech stack.

### Getting started

This section must **clearly** describe how someone who has just downloaded the repository can get started running/using it. It must include any pre-requisites or frameworks that must be installed locally, and any additional installation steps where relevant.

- Never make any assumptions about the engineer's local environment or tools.
- Make sure the instructions are step-by-step

### Usage

Use this space to show useful examples of how a repository can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

The exact contents here will be different depending on the type of repository in question. A microservice repository must document the endpoints it implements, whilst a shared code repository must explain how to include any packages/modules and give examples of how to use the classes/libraries exposed.

### Contributing

How should an engineer who wishes to contribute to the repository do so? In most cases, a link out to the relevant branching strategy will usually be sufficient.

## Template

If starting from a blank slate, you could use this template as a starting point for a new `README.md` file.

```markdown
# ACME project

## Overview

The ACME project is a thing that does stuff.

## Built with

This repository is built using the following technologies:

- technology
- etc

## Getting started

How does a new user get up-and-running with the project? What dependencies do they need to have installed?

## Usage

Describe how to use the application/project under standard use-cases.

## Contributing

How should an engineer get started contributing to the project.
```
