---
title: Local Running
authors: 
- Dave Arthur 
next-review: 2023-03-31
---

# Local Running

It is possible to run the playbook locally, which allows a user to see the changes being made in context. Whilst this can be useful for basic content updates, it is critical when making style or configuration changes to the playbook as a whole.

## Requirements

Running locally requires the following tooling to be installed and available:

- [Visual Studio Code](https://code.visualstudio.com/)
- [pip](https://pypi.org/project/pip/)


## Starting and Stopping

To run the playbook via Visual Studio Code, simply hit the `<F5>` key. VSCode will ensure all plugins are insalled, and start a local instance of MKdocs.

You should then be able to open a browser window at http://localhost:8000/ to view the locally running version of the playbook.

To stop it again, simply select the VSCode window, and press `<Shift>+<F5>`.

!!! note
    These keystrokes map to the **Start Debugging** and **Stop Debugging** commands from the **Run** menu.

