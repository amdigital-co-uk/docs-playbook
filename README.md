This is a documentation repository for the department's playbook.

The Playbook is the public statement of how AM's Technology department works: what we value, how we turn ideas into released software, and the standards we hold ourselves to. It sits alongside the internal [Knowledgebase](https://knowledgebase.platformdev.amdigital.co.uk/), which holds the procedures, tooling and platform detail behind it.

## Structure

The Playbook has five sections, each a folder under `docs/`:

| Section | Folder | What it covers |
|---|---|---|
| How we work | `How-we-work/` | The operating model: roadmap and objectives, discovery, design, delivery, release, operation and support, teams and roles |
| Quality | `Quality/` | Shared quality, testing, engineering standards, security, privacy and accessibility, reliability, decision records |
| Culture | `Culture/` | Values and tenets, collaboration, autonomy and guardrails, continuous improvement, leadership, meetings, hackathons |
| People | `People/` | Onboarding, the buddy guide, the progression framework, hybrid working, training |
| Glossary | `Glossary.md` | The vocabulary, defined once |

Navigation is defined by a `.pages` file in `docs/` and in each section folder (the awesome-pages plugin). Site settings, theme and plugins are in `mkdocs.yml`. Styling overrides are in `docs/stylesheets/extra.css`.

Every page carries the same frontmatter: `title`, `authors`, `reviewed` and `next-review`. Pages state principle and shape; procedures, templates and tooling detail belong in the Knowledgebase, not here.

The design and plan for the 2026 rewrite, including where every earlier page went, is in `plans/`.

## Tooling & Technologies

This Playbook is written using [Markdown](https://www.markdownguide.org/), a simple text editor designed for documentation.

More specifically, it is built on [MKDocs](https://www.mkdocs.org/), using the [Material for MKDocs](https://squidfunk.github.io/) theme. MKDocs and Material for MKDocs extend the functionality of Markdown, allowing you to include visually richer content.

It is version controlled in GitHub and published to GitHub Pages by a GitHub Actions workflow on every push to `main`.

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
- [Python](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)

To install pip, ensure that Python has been installed and then run `python -m ensurepip`. This will ensure pip is installed and available.

#### Starting and Stopping

To run the playbook via Visual Studio Code, simply hit the `<F5>` key. VSCode will ensure all plugins are installed, and start a local instance of MKdocs.

You should then be able to open a browser window at http://localhost:8000/ to view the locally running version of the playbook.

To stop it again, simply select the VSCode window, and press `<Shift>+<F5>`.

!!! note
    These keystrokes map to the **Start Debugging** and **Stop Debugging** commands from the **Run** menu.
