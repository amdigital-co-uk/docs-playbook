This is a documentation repository for the department's playbook.

The Playbook is a public-facing guide to the fundamental ways we work. This sits alongside the internal-facing [Knowledgebase](https://knowledgebase.platformdev.amdigital.co.uk/), which contains specific details of how our technologies and toolkits are built and configured.

## Structure

The Playbook is structured into sections to promote a clear and simple narrative to the reader.

Playbook settings, including look and feel, plugins etc, are defined in the mkdocs.yml at the root.

The Playbook documentation resides in the /docs folder. This includes markdown files and assets such as images or supporting documents. Additionally styling overrides are included in CSS files in the /docs/stylesheets folder, and the .pages file outlines the navigation structure. 

## Tooling & Technologies

This Playbook is written using [Markdown](https://www.markdownguide.org/), a simple text editor designed for documentation.

More specifically, it is built on [MKDocs](https://www.mkdocs.org/), using the [Material for MKDocs](https://squidfunk.github.io/) theme. MKDocs and Material for MKDocs extend the functionality of Markdown, allowing you to include visually richer content.

It is stored and version controlled using Git in GitHub, and published with using GitHUb actions into an Azure WebApp.

## Contributing

A full guide on how to contribute to the Playbook can be found in the [Knowledgebase](https://knowledgebase.platformdev.amdigital.co.uk/Knowledgebase-User-Guide/)

You can make small changes within GitHub, and will be able to view basic markdown rendering when you do. This will include all of MKDocs or Material for MKDocs rendering. 

Whilst this can be useful for basic content updates (e.g. single paragraph updates), it is critical when making larger or more complex changes (e.g. multiple page changes, styling or configuration updates) that you are able to properly validate your work before you create a pull request.

!!! note "Ownership"

    When you create, review, or modify a document, **you are responsible** for ensuring that it is _well written_ and has been _peer reviewed_, and that _review date is set_.

### Local Running

To achieve this you will need to clone the repository and run Playbook on your local machine. 

#### Requirements

Running locally requires the following tooling to be installed and available:

- [Visual Studio Code](https://code.visualstudio.com/)
- [pip](https://pypi.org/project/pip/)


#### Starting and Stopping

To run the playbook via Visual Studio Code, simply hit the `<F5>` key. VSCode will ensure all plugins are installed, and start a local instance of MKdocs.

You should then be able to open a browser window at http://localhost:8000/ to view the locally running version of the playbook.

To stop it again, simply select the VSCode window, and press `<Shift>+<F5>`.

!!! note
    These keystrokes map to the **Start Debugging** and **Stop Debugging** commands from the **Run** menu.
