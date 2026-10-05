# Knowledgebase review

A wholesale review of the internal Knowledgebase (amdigital-co-uk/docs-knowledgebase): what goes, what stays, what is added, what is updated, and how it should be structured. Written 2026-10-05 by Claude (Fable 5.1) from a page-by-page catalogue of all 687 pages on the `docs/playbook-migration` branch (main plus the 26 pages migrated from the Playbook in #687), the git history, a build, and a close read of every team ways-of-working page. Companion to [knowledgebase-handover.md](knowledgebase-handover.md), which it supersedes in places.

## 1. The Knowledgebase today

| | |
|---|---|
| Pages | 687 (377,000 words), 357 images |
| Largest areas | Platforms 201, Decision Hub 177, Ways of Working 89, WIP 47, Tools and Providers 41, Support 37, Directory 33, Onboarding 26, Runbooks 16 |
| Where the edits go | Over the last year: Ways of Working 121 file changes, Decision Hub 102, Platforms 67, Runbooks 57, Tools 56, Support 12, Onboarding 11, Directory 11. Ten contributors. |
| Build | Passes with 118 warnings. Four plugins (`tags`, `blog`, `gen-files`, `macros`) and seven scripts exist only to serve the Decision Hub. |
| Hosting | Azure Static Web App behind Entra ID sign-in, Terraform in the repository. |

Three patterns run through it. **A migration that was never finished**: around 90 Platform pages still carry the 2023 banner "this page has been migrated and needs to be reviewed". **Working notes that never became documentation**: WIP (47 pages), the team Projects folders, and several Decision Hub pages hold facts about live systems that appear nowhere else. **Pages that describe a model we no longer run**: the Support Hub team, runway and project-register planning, Problem Owner and Product Lead roles, two retired Azure DevOps projects.

The healthy parts are easy to name: Runbooks (recent, owned, well written), Synthetic Monitoring, Disaster Recovery, the Azure landing zone pages, the AM UI Applications pages, the Quartex deep-dive onboarding series, Testmo, and the engineering practices written in 2026 (regression policy, guardrails, conventional commits, Claude-first).

## 2. What goes

About 260 pages, taking the site from 687 to roughly 430. Nothing is deleted before the facts it holds have a home; the "salvage" column says where.

| What | Pages | Why | Salvage first |
|---|---|---|---|
| **Decision Hub** (ADRs, RFCs, SDR templates, Open Decisions, Tags, index) | 177 | Decisions now live in the SharePoint decision log and library. The migration log records 114 migrated and 14 deliberately not (RFCs concluded by an ADR). | Confirm the last records made it: ADR-098 to ADR-102 and RFC-029 to RFC-031 were written in June to September 2026, close to the migration date. Move `Test-Strategies/Access-Test-Strategy.md` to Test Engineering. The `Quartex/RFC-Backend-SSO-Integration` file is covered by ADR-071. Re-point the four pages that link into the hub (S3 content runbook, networking diagrams, AM UI how-to guides, Tools directory) at the SharePoint library. |
| Decision Hub plumbing | | `tags`, `blog`, `gen-files` and `macros` plugins, `scripts/` (seven files), `extra.decisions_relative`, the `_migrated-decision-records/` folder at the repository root (119 untracked Word and Excel files) | Keep the two Excel migration logs in SharePoint next to the library, then delete the folder. |
| Five decision records under `Platforms/Quartex/Architecture/Decision-Records/` | 5 | Same reason; they were never in the hub. | Migrate to SharePoint. |
| **WIP** | 47 | Objective working notes from 2023 to 2024. Nothing outside WIP links in. Most pages are investigations whose outcome was decided long ago. | Insights and Reporting (33 pages) holds the only description of the live analytics architecture: Matomo, Azure SQL star schema, Data Factory, Power BI, the import Azure Function. Write one Platforms/Insights architecture page from it. Test Data Replication (7): confirm whether TDR is live (the Indigo testing page treats it as a real thing); if so, its design belongs under Platforms/Quartex. HTR upgrade options and the shared developer environment plan: one page each under Platforms/Quartex if still relevant, else gone. Access Management (3), Lambdas, React integration, deployment audits: gone (delivered or superseded, per ADR-020 and the live pages). |
| **Support Hub ways of working** | 10 | Describes a team and a model that no longer exist ("15 hours per sprint on the Support Desk", boards in two retired Azure DevOps projects). Two pages are empty, one is lorem ipsum. | Nothing. The three-line model is in the SharePoint runbooks. |
| **Directory: Teams** | 5 | Lists historical teams, misses current ones, links a dead Playbook anchor. You do not find them valuable. | A one-paragraph "Teams" note on the Ways of Working index: current teams, their objective, and the Teams channel tags. |
| Directory: Documentation, Platforms | 2 | 2023, superseded by the home page and the Platforms index. | Fold the one useful table (where things are documented) into the home page. |
| Blog plumbing | 3 | Template, "how to create a post", empty index. Six posts since 2024, one in the last year. | Keep the six posts as plain pages under Engineering/Articles; drop the plugin. |
| Empty and placeholder pages | 8 | `Support/Escalation-process`, `Onboarding/Product-Team`, `Platforms/Insights/index`, `Infrastructure/MySql-DBs/index`, `Support-Hub/refinement` and `validation`, `WIP/.../Summary`, `Blog/index` | Nothing. |
| Historical and duplicate pages | ~12 | `AM-UI-Applications/The-Pipeline/the-pipeline-old.md`; `White-Label/Test/*` (7 pages, 2023, "needs review"); `Quartex/Infrastructure/MySql-DBs/Character-sets.md` (a redirect stub); `Demos/parallel-experiences-demo.html`; the 14 unreferenced images; the `.order` files left by a previous navigation plugin; `.DS_Store` | Nothing. |
| Team records that are not agreements | ~10 | Health check snapshots (Blue 2026-03, Indigo 2024-03), Blue Projects/2025 (5 pages), Indigo sprint retrospective record | Move the Asset Consolidation test strategy and architecture overview under Platforms/Quartex. Health checks: keep the last one per team in a dated Records subfolder, or delete. |
| Papercuts | 1 | Uses Problem Owner and Product Lead, names two individuals, tracks a 2025 spreadsheet. | If the programme continues, rewrite with current roles; if not, delete. |

## 3. What stays

The spine of the Knowledgebase, kept as it is or with light edits:

- **Runbooks** (16): the model for everything else. Owned, dated, step by step.
- **Quartex Disaster Recovery** (14) and **Synthetic Monitoring** (12): current and complete.
- **Quartex Environments** (4), **How-to guides** (11), **CI/CD** (2), **Infrastructure** (10, see updates).
- **Quartex Architecture: Documents List State** (4), **Storage**, **Flagsmith** (7), **Lean Entry Points** (5), **Workload Discovery**, **Integrations/LibLynx**.
- **AM UI Applications** (15): the best-maintained platform area, with "last reviewed" dates in every page.
- **White Label: Authentication** (3, current to April 2026), **Postgres** (8), **Mirror** (6), **Infrastructure**, **Site Deployment**, **AM Explorer**.
- **Insights**: custom scripts on published sites (4,800 words, current), product ID update runbook.
- **Custom Tooling**.
- **Tools and Providers**: Azure landing zones (9), Testmo (2), Code Health Tools, Kubectl (3), Telepresence, Kibana, Elasticsearch, Volta and Node, package sources, Podman, accessibility testing tools, remote devices, Keeper, Stack Overflow.
- **Support: Publication Go-Live** (13) and **Support Tasks** (9): still the procedures for go-lives and common support fixes, moved under Runbooks (section 6).
- **Onboarding**: the Quartex deep dive (14), Kubernetes access, infrastructure access (3), Chocolatey scripts, leavers checklist, the two manager pages.
- **Engineering practices written in 2026**: Regression Testing Policy, Engineering Guardrails, Conventional Commits (2), Claude-First, Claude Code Guardrails.
- **The 26 pages migrated from the Playbook** in #687.
- **Test Engineering**: test health reporting, supported browsers and devices, tagging (2), test notes guidance, plus the migrated Playwright, BDD and exploratory pages.
- **Directory: People** (23 working-with-me pages). Three have not been touched since 2023 and two are 33-word stubs; ask their owners.
- **DevOps Team** (4), **Indigo** manifesto and PR practices, **Yellow** definition of ready and done, **Blue** readying and sprint planning: see section 5 for how team pages are reshaped.
- The six blog posts, as articles.

## 4. What must be added

In priority order. The first four are promises the rewritten Playbook now makes.

1. **Shared expectations page** (`Engineering/Shared-Expectations.md`). The ten department-wide expectations the Playbook states, in one list, each linking to the Playbook page and to the Knowledgebase procedure that implements it. Every team page links here instead of restating them. See section 5.
2. **Test plan guide and template** (`Test-Engineering/Test-Plans.md`). The Playbook says the test plan is a design output, derived from the solution design and iterated with it, and a required artefact before a feature is ready. Nothing in the Knowledgebase says what one contains or where it lives. Yellow's definition of done, Indigo's test prep tasks and Blue's example-mapping habit are three team-level answers to the same question; the guide should draw on all three.
3. **Delivery documents and dashboards index** (replacing `Tools-and-Providers/AMPFlow-Governance.md`). One page listing every SharePoint artefact the Playbook mentions, with owner and when it is used: proposal, canonical objective document, outcome specification, solution design, release plan, release dashboard, outcome dashboard, roadmap, deployment log, deployment communication guide, decision log and library, service desk runbooks.
4. **Service desk section** (`Service-Desk/`). An index of the SharePoint runbooks (first, second and third line, prioritisation, P1, known error log, escalated issue template, shadow roles) plus the engineer-facing material that belongs in the Knowledgebase: what a second-line engineer and a shadow do day to day, the deployment notice periods, and the diagnostic resources page that already exists under Support.
5. **Platforms/Insights architecture**, written from WIP (see section 2).
6. **One index page for every Platforms folder that lacks one.** Seventeen Quartex operations pages and all eleven how-to guides are reachable only through search.
7. **A current teams page** (section 2) and **one folder per current team** (section 5). The service desk rota names an Emerald team that has no page.
8. **Glossary alignment**: the three Dictionary pages become one Glossary of domain and platform terms that defers to the Playbook glossary for operating-model terms and drops retired ones.
9. **Contributing page** replacing the eight-page User Guide: the four-field frontmatter, no spaces in filenames, one H1, strict build, review cadence, where things belong (the table from the Playbook README).
10. **Architecture model links.** The Quartex Architecture index says the canonical model is the `qtdoc-architecture` repository; the Playbook says architecture lives in a shared model. Each platform index should say which it is and link it.

## 5. Team ways of working: self-determination without undoing shared expectations

### What the team pages say today

I read every team page. The good news: none of them contradicts the Playbook on substance. Indigo's manifesto (small PRs reviewed by at least one person, conventional commits, shift-left testing, deploy constantly, two items in progress at most), Blue's readying rules (test methods in the implementation plan, example mapping as the first test plan, releases as small as possible, 10% of capacity reserved for the service desk), Yellow's definition of done (100% pass rates, exploratory checks, accessibility tab, results in Testmo) and the DevOps definition of done (runbooks and documentation updated, peer reviewed) all sit comfortably inside the shared expectations. In places they are stronger than the Playbook.

The problems are different ones:

- **Framing.** Blue and Indigo both open with "these serve as a reminder of how we have mutually agreed to work together, but are not rules to which we must adhere". That is right for a team's own agreements and wrong if a reader takes it to cover peer review, regression coverage or the deployment log. Nothing on the page distinguishes the two.
- **Restating instead of linking.** Each team has its own sprint planning, stand-up, retrospective and readying page (three versions of sprint planning, three of retrospectives). The departmental ceremony guides migrated in #687 now sit beside them. Most of the team text is generic Scrum guidance that could be one shared page, with the team's specific choices (time, facilitator rota, capacity rule, WIP limit) as a short list.
- **Stale references.** Blue's runway planning updates the Project Register, which no longer exists. Indigo's testing page is built on TestRail, with a link to a Knowledgebase TestRail page that does not exist; the department tool is Testmo. Yellow and Indigo link dead Playbook URLs. Yellow's runway page tells the PM to add RAID items "to delivery governance". Papercuts uses Problem Owner and Product Lead.
- **Timing of the test plan.** Indigo creates test preparation tasks per backlog item at refinement; Blue builds the initial test plan through example mapping in stand-ups; Yellow checks for "the existence and relevance of a test strategy" at done. All three are honest attempts at the same thing. The Playbook now says the test plan is a feature design output, before the feature is ready. The team pages should align with that or say explicitly how their practice delivers it.
- **Naming drift.** The Blue folder's index is titled "Ways of Working - Quartex Objectives"; the Teams directory calls the team "Objectives"; the rota calls it Blue. Indigo and Yellow are listed under "Published-Sites-" prefixes in the directory and without them in Ways of Working.

### The proposed shape

One page per team as the norm, two or three where a team has genuinely distinct material, and a fixed structure that makes the boundary visible:

```
Teams/
  index.md                 current teams, their objective, channel tags, link to Shared Expectations
  Blue/index.md            Team agreements
  Emerald/index.md
  Indigo/index.md
  Yellow/index.md
  DevOps/index.md
```

Every team page follows the same template:

1. **Who we are and what we are on.** Two sentences and the current objective.
2. **Shared expectations.** One line: "We work to the department's [shared expectations](../../Engineering/Shared-Expectations.md). The rest of this page is what we have chosen within them." No restating.
3. **Our choices.** The things the Playbook leaves to the team: iteration length and cadence, ceremony times and facilitation, capacity rules, work-in-progress limit, definition of ready and done at backlog item level, which environments and clients the team uses, how test tasks are organised, channels and tags, tools the team has chosen within the department's defaults.
4. **Our experiments.** What the team is currently trying, with a date and an end date.
5. **Records.** A link to a dated subfolder for health checks and retrospective outputs, or nothing.

Rules that keep the balance: a team page may add to a shared expectation or make it stricter; it may not weaken, omit or contradict one. Anything generic (what a stand-up is for, how to run a retrospective) lives once in `Engineering/Ceremonies/` and is linked. The team's "not rules" sentence applies to section 3 only and says so.

Indigo's manifesto and PR practices, Yellow's definition of ready and done, and Blue's readying page are good enough to become department-level examples or to seed the shared pages, with the team keeping a short "our choices" list.

## 6. What needs updating

| Area | Pages | What |
|---|---|---|
| Quartex Architecture | ~35 | Pages still marked "migrated and needs review" since June 2023: COUNTER (17), Microservices (10), Structure and Patterns (9), JFD toolkits, Uploader. Assign an owner per component to confirm, correct or delete. COUNTER and the microservice patterns are almost certainly still true and worth the hour each. |
| Quartex Release | 7 | Automated Release Process, Deploying to Production and Test Environments are 2021 documents that predate continuous deployment, Argo Rollouts and the deployment log. Rewrite as "how a change reaches production today" and link the Playbook's release page. |
| Quartex Infrastructure | 10 | Anti-Virus (2019 references), Redis and Standalone Servers ("needs review"), OCR licensing (Windows Server 2012), empty MySQL index. Review with DevOps. |
| Quartex Test | 3 | Move to Test Engineering. The Quartex Functional Test Strategy references warranty and predates the Playbook's testing page; align it. |
| White Label | ~34 | Pages marked "needs review" since 2023, mainly AD new module (9) and site creation (3). Decide whether new White Label sites or modules are still created. If rarely, collapse to one "White Label: legacy procedures" page per topic and label the platform legacy on its index. |
| Tools and Providers | ~10 | Six pages are a URL and nothing else (BrowserStack, Chromatic, Flagsmith, GitHub, Pactflow, Postman): one "Tools and access" table instead. AWS, AWS CLI and Deployment Manager are 2023; confirm Deployment Manager is still used. Confirm TestRail is retired in favour of Testmo and say so. |
| Support | 22 | Move Publication Go-Live and Support Tasks under Runbooks (section 7). Three pages say "Support Hub"; fix the wording. Thirteen go-live pages carry the 2023 migration banner; the go-live owner should review them once. |
| Onboarding | 3 | Index (2023) rewrite; fill or remove the two deep-dive stubs (Site Configuration, Styles); check the Chocolatey scripts page. |
| Links to the Playbook | 26 | All deep links are dead; most were dead before the rewrite. Targets are in the handover document. |
| Frontmatter and dates | all | Mixed forms (`reviewed: [date]`, `reviewer:`, two date formats, "Last Reviewed" in body text on AM UI pages). Normalise to the Playbook's four fields. 36 pages have review dates in 2023 to 2025 that have passed. |
| Site | | Rename "Platform Development Knowledgebase" to "AM Technology Knowledgebase". Rename `AM no tag.png` (the CI check for spaces would reject it). Add `--strict` to the build once the warnings are cleared. Run a link check in CI. |

## 7. How it should be structured

Organise by what the reader is trying to do, not by who wrote it. Eight top-level sections instead of thirteen.

```
Home                     what this is, where things belong, how to contribute (link)
Platforms/               how each platform is built
  Quartex/               Architecture (by component), Infrastructure, Environments, Developer guides, Published sites (new experience: the AM UI Applications pages and Documents List State)
  White-Label/           labelled legacy: Authentication, Postgres, Mirror, Infrastructure, Site deployment
  Insights/              architecture (new), custom scripts, product IDs
  Access-Management/     if the product is live; otherwise gone
Runbooks/                how to operate them, by platform then topic
  Quartex/               Disaster recovery, Release and deployment, Go-live, Support tasks, FTP, OCR, Troubleshooting
  Published-Sites/       Front Door logs, certificates
  White-Label/
  Tooling/               Checkly, Cloud Storage Security, MySQL, Telepresence
Engineering/             how we build, department-wide
  Shared-Expectations    (new)
  Standards/             conventions by language and platform
  Practices/             PRs, commits, guardrails, regression policy, Claude-first, READMEs, estimation, time recording, RAID, technical design workshops
  Ceremonies/            the shared guides
  Templates/
  Articles/              the former blog posts
Test-Engineering/        strategy, test plans (new), tagging, test health, browsers and devices, Playwright, BDD, exploratory, Testmo
Teams/                   one page per current team (section 5)
Service-Desk/            index of SharePoint runbooks plus engineer-facing notes (new)
Tooling-and-Access/      the former Tools and Providers plus the onboarding access pages; one table of tools and how to get access
Onboarding/              engineering setup, Quartex deep dive, leavers
People/                  working-with-me pages
Glossary.md
Contributing.md
```

Two principles behind it. **Platforms describe, Runbooks operate**: an architecture page explains how the OCR service is built; the runbook says how to restore it. Today both are mixed under Platforms. **One home per topic**: Support tasks, Quartex how-to guides and Runbooks currently split operational procedures three ways by accident of authorship.

## 8. Sequence

1. Merge #687 (the Playbook migration) so the baseline is stable.
2. Decision Hub: confirm the late records, move the Access test strategy, re-point four links, delete the hub, its plugins, scripts and the untracked folder. This alone removes 177 pages and most of the build warnings.
3. Write the four Playbook promises: shared expectations, test plan guide, delivery documents index, service desk section.
4. Teams: new template, one page per current team, Support Hub and Teams directory removed, Papercuts resolved.
5. Restructure: the folder moves in section 7, with redirects for Runbooks and Platforms pages people have bookmarked, and index pages for every folder.
6. WIP: salvage into Platforms/Insights and Platforms/Quartex, then delete.
7. Platform review by owners: Quartex Architecture (2023 banners), Release, Infrastructure, White Label.
8. Housekeeping: links, frontmatter, filename, strict build, link check, site name, Glossary, Contributing.

Steps 2 to 4 are a few days of work and deliver most of the value. Step 7 is the long tail and depends on owners.

## 9. Decisions and facts I could not settle

- **Access Management**: ADR-001 to ADR-007 and a WIP folder describe a PAM product on Identity Server; Platforms has one demo page. Is it live?
- **Test Data Replication**: designed in WIP; referred to as a real constraint on Indigo's testing page. Live?
- **Papercuts**: still running?
- **White Label**: are new sites or modules still created, or is it maintenance only?
- **Deployment Manager** (home-grown Node tool, documented 2023): still used?
- **TestRail**: retired in favour of Testmo?
- **Emerald**: a current team with no pages, or a rota label?
- **Architecture model**: is the canonical model the `qtdoc-architecture` repository, IcePanel, or both?
