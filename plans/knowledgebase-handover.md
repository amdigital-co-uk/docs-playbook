# Knowledgebase handover and tidy-up

What the Playbook overhaul moves into the Knowledgebase, what it now assumes the Knowledgebase holds, and what the survey of the Knowledgebase turned up along the way. Written 2026-10-02 by Claude (Fable 5.1) as input to a wider Knowledgebase tidy. Companion to [playbook-overhaul.md](playbook-overhaul.md).

## 1. Where things belong

The overhaul applied one rule, and the tidy should apply the same one.

| Home | Holds | Test |
|---|---|---|
| **Playbook** (public) | Principle and shape: how we work, what we value, the standards we hold | Would an outsider or a new joiner need it to understand us? Does it survive a tool change? |
| **Knowledgebase** (internal) | Procedure, standards detail, runbooks, templates, team agreements, platform and tooling documentation, decision records | Does it name a repository, a tool, a person, a path, a step? |
| **SharePoint** (internal) | Live documents and lists that are worked in day to day: proposals, canonical objective documents, outcome specifications, the roadmap and dashboards, the deployment log, release plans, service desk runbooks | Is it a record that changes as work progresses, owned by someone outside engineering, or needed by the wider business? |

The grey area is between the last two. The Knowledgebase should not duplicate SharePoint documents, but it should be the place an engineer goes to find them: one index page per area with links, owners and a sentence on when each is used. Today that index does not exist.

## 2. Moved in this overhaul

All in amdigital-co-uk/docs-knowledgebase#687. Each page kept its content and authors, gained the standard frontmatter, lost its Playbook framing and had retired role names replaced.

| From the Playbook | To the Knowledgebase | Why it moved |
|---|---|---|
| Quality Standards: Coding Conventions, Endpoint Naming, Exceptions, Logging, React, Unit and Integration Testing | `Ways-of-Working/Engineering/Standards/` | Language and platform conventions; name repositories, an S3 bucket and a KMS key; linked from repositories |
| Pull Requests, Repo READMEs | `Ways-of-Working/Engineering/` | Mechanics (base branches, work item link format, templates) |
| Technical Design Workshops | `Ways-of-Working/Engineering/` | A session how-to; the Playbook now says only that collaborative design sessions exist |
| Performing a Peer Review, Release Plan Review | `Ways-of-Working/Engineering/` | Checklists; the principle stays in the Playbook |
| Workflow Item Definition | `Ways-of-Working/Engineering/` | Azure DevOps state and field configuration |
| RAID | `Ways-of-Working/Engineering/` | Ratings, workflow diagrams and templates; the Playbook keeps one paragraph |
| Estimation sizes and ready-to-estimate RAG (new page from Estimation and ROM) | `Ways-of-Working/Engineering/Estimation-Sizes.md` | Scales and thresholds; the Playbook keeps ROM versus estimate |
| Time recording detail (new page from Time Tracking) | `Ways-of-Working/Engineering/Time-Recording.md` | How teams record; the Playbook keeps why |
| Backlog Refinement, Sprint Review, Example Mapping, Team Health Checks | `Ways-of-Working/Engineering/Ceremonies/` | Team-level ceremony guides and facilitator notes |
| Security and Reliability Impact Assessment Template | `Ways-of-Working/Engineering/Templates/` | A template. See section 3 on where it should end up |
| BDD best practices, Playwright guidelines, Playwright parameterisation, Testing workflow, Exploratory Testing | `Ways-of-Working/Test-Engineering/` | Tool how-tos naming repositories and workflows; exploratory testing charter steps |
| Line Manager Duties for New Starters, Onboarding for Managers | `Onboarding/Engineering/` | Internal checklists linking a SharePoint document |
| Absence and Leave | `Ways-of-Working/Department-Policies/` | HR procedure naming the HR system |

Dropped rather than moved: the Decision Record template (the Knowledgebase Decision Hub already has ADR, RFC and SDR templates), and the empty or stub pages.

## 3. What the Playbook now assumes the Knowledgebase holds

Each Playbook page says "the detail lives in our internal Knowledgebase" rather than linking. These are the promises that sentence makes, and whether the Knowledgebase keeps them today.

| Playbook says | Knowledgebase today | Action |
|---|---|---|
| Every team writes down its working agreements, cadence and definition of done | Folders for Blue, Indigo, Yellow, Support Hub, DevOps, Papercuts. The Support Hub pages are lorem ipsum placeholders. The service desk rota names an Emerald team with no folder. The Teams directory lists "Objectives" as a team with no page and still lists historical teams | One folder per current team, with the minimum set the Playbook names. Delete placeholder pages. Rewrite `Directory/Teams/index.md` |
| Conventions for each language and platform, linked from repositories | Now in `Engineering/Standards/` | Check each repository README links the right page |
| Regression testing policy, engineering guardrails, conventional commits | `Engineering/Regression-Testing-Policy.md`, `Engineering-Guardrails.md`, `Conventional-Commits/` exist | Policy says "each sprint" and names the Lead Test Engineer; fine for internal |
| Test health visible every day | `Test-Engineering/Process-Reporting-Test-Health.md` exists; four of its images are missing | Restore images |
| Supported browsers and devices | `Test-Engineering/Supported-Browsers,-Devices-&-Operating-Systems.md` exists | Fine |
| The test plan is a design output, derived from the solution design and iterated with it | No test plan guidance or template in the Knowledgebase. The Functional Test Strategy that held the readying and planning steps was condensed into the Playbook | **Gap.** Write a test plan guide and template under `Test-Engineering/` that reflects the new stance |
| Security and reliability impact assessment on every architectural, design and scope decision record | The SRIA template is now a standalone page under `Engineering/Templates/`. The Decision Hub ADR, RFC and SDR templates have no impact assessment section | **Gap.** Fold the SRIA into the decision record templates and retire the standalone template, or keep it and link it from every template |
| Decision records in a versioned, commentable store, indexed in a decision log | Two systems: the Knowledgebase Decision Hub (99 ADRs, 33 RFCs, 3 SDRs, generated tag pages) and the SharePoint decision log and library the old Playbook described. An untracked `_migrated-decision-records/` folder of 119 files sits at the repository root, which looks like a migration from SharePoint in flight | **Decision needed.** One home. Finish or abandon the migration, then say which it is on the Decision Hub index |
| Procedures and templates: proposal, canonical objective document, outcome specification, solution design, release plan, deployment log | All in SharePoint; the Knowledgebase has no index of them. `Tools-and-Providers/AMPFlow-Governance.md` (retitled "Delivery document templates") points at Loop templates for the retired governance artefacts | Replace that page with a "Delivery documents and dashboards" index: each SharePoint artefact, its owner, when it is used |
| Service desk runbooks, prioritisation, known error log, P1 process, shadow roles | All in the SharePoint Service Desk folder. `Support/Escalation-process.md` is empty. `Ways-of-Working/Support-Hub/` describes a Support Hub team model with "15 hours per sprint" of support desk work, which the current three-line model has replaced | Either move the runbooks into `Support/` or make `Support/index.md` the index of the SharePoint folder. Rewrite or remove the Support Hub ways-of-working pages |
| "Working with me" pages | `Directory/People/` exists | Fine |
| Manager onboarding | Moved | The SharePoint onboarding checklist it links should be checked |
| Glossary: the words we use, defined once | `Dictionary/` (three pages, about 2,000 words) predates the Playbook glossary | Align: either the Dictionary holds the internal and platform terms only and defers to the Playbook for operating-model terms, or it is removed |

## 4. Knowledgebase content the overhaul has made stale

**Links to the Playbook.** 26 Knowledgebase pages link to the Playbook. Fifteen link to the root, which is fine. The rest link to paths that no longer exist, and most of those were already dead: they point at an even older Playbook structure (`Ways-of-Working/Guides/...`, `3.-Delivery-Framework`, `4.-Delivery-Practices`, `Delivery-Practices/Team-Behaviours/...`, `Playbook-User-Guide`). Nobody has followed these links for some time.

| Dead link target | Pages | New target |
|---|---|---|
| Problem Ownership role pages (Problem Owner, Product Lead, UX Lead, Engineering Owner) | `Engineering/Workflow-Item-Definition.md` | `How-we-work/Teams-and-Roles/` |
| Toolkit/Staff-Engineering | `Support-Hub/index.md` | `How-we-work/Teams-and-Roles/` |
| Functional Test Strategy, Exploratory Testing (several old paths) | `Platforms/Quartex/Test/Quartex-Functional-Test-Strategy.md`, `Decision-Hub/Test-Strategies/Access-Test-Strategy.md`, `Indigo-Team/Testing/index.md` | `Quality/Testing/` or the moved Knowledgebase page |
| Coding Conventions anchors | `Decision-Hub/ADRs/ADR-014`, `ADR-021` | `Engineering/Standards/Coding-Conventions.md` |
| Architectural Decision Records, Request for Comments, Documenting Decisions | `Decision-Hub/index.md`, `SDRs/index.md`, `SDRs/2-SDR-Template.md` | `Quality/Decision-Records/` |
| Backlog Refinement Guidelines | `Indigo-Team/Indigo-Team-Backlog-Refinement.md` | `Engineering/Ceremonies/Backlog-Refinement-Session-Guidelines.md` |
| Engineering Leadership Guide, Role of Value Stream Engineering Lead | `Directory/People/*` | `Culture/Leadership/` |
| 3.-Delivery-Framework, 4.-Delivery-Practices, 5.-Department-Policies, Playbook-User-Guide | `Directory/Teams/index.md`, `Directory/Documentation.md`, `Onboarding/index.md`, `Yellow-Team/index.md`, `Knowledgebase-User-Guide/Local-Running.md` | `How-we-work/`, `People/`, or remove |

**Pages.** `Directory/Teams/index.md` (historical teams, dead anchor, wrong team list). `Tools-and-Providers/AMPFlow-Governance.md` (retitled in #687; filename and the `raid-ampflow-workflow.png` image name still carry the old word). `Ways-of-Working/Support-Hub/*` (placeholder text and a superseded model). `Support/Escalation-process.md` (empty). `Ways-of-Working/index.md` and 15 other pages with a 2025 or 2026 review date already passed, and five with 2023 dates.

## 5. Wider tidy candidates

Found while building and surveying; not caused by the overhaul.

- **118 build warnings.** 20 in `Decision-Hub/Open-Decisions.md`, about 35 in the generated `Decision-Hub/Tags/` pages (broken `../RFC/` links), 4 missing images in `Process-Reporting-Test-Health.md`, 3 in `Runbooks/index.md`, 2 macro syntax errors, the rest scattered across Indigo, DevOps, Conventional Commits and Claude Code Guardrails pages.
- **`WIP/`**: 47 pages of 2025 objective working notes (Access Management, HTR transcripts, Insights and Reporting, Microservice Consolidation, Test Data Replication, and loose pages). Archive, or move what is still true under `Platforms/`.
- **`Runbooks/TODO/`**: a folder literally named TODO, with FTP runbooks that have broken links.
- **`_migrated-decision-records/`**: 119 untracked Word and Excel files at the repository root. Decide, then delete from the working tree.
- **`Demos/`**: empty.
- **`assets/images/AM no tag.png`**: a filename with spaces in a repository whose CI rejects them.
- **Frontmatter**: a mix of `reviewed: [date]` and `reviewed: date` forms; `reviewer` fields; dates in two formats. Pick the Playbook's four-field convention.
- **`Platforms/`** is 201 pages and was not surveyed. It is the largest section and the most likely to hold stale material.

## 6. Suggested order

1. Fix the dead Playbook links (one pass, half a day) so nothing in the Knowledgebase points at a 404.
2. Decide the home for decision records and finish or abandon the migration folder.
3. Write the two gap documents the Playbook now implies: the test plan guide and template, and the impact assessment section in the decision record templates.
4. Replace the templates page and the empty escalation page with two index pages: delivery documents and dashboards; service desk runbooks.
5. One folder per current team, placeholders deleted, Teams directory rewritten.
6. Archive `WIP/`, resolve `Runbooks/TODO/`, delete `Demos/`, rename the one file with spaces.
7. Fix the build warnings and normalise frontmatter, then turn on `mkdocs build --strict` in CI so they do not come back.
8. Survey `Platforms/`.

Steps 1 to 4 are the ones the Playbook depends on. The rest is housekeeping that can follow at any pace.
