# Playbook overhaul: page inventory and disposition

Companion to [playbook-overhaul.md](playbook-overhaul.md). One row per existing page. Actions:

- **Keep**: stays, light edit (department name, frontmatter, tone).
- **Rewrite**: content survives in a new page named in the target column.
- **Move**: goes to the Knowledgebase at the folder named.
- **Cull**: deleted. The note says what, if anything, is carried forward.

Word counts are approximate.

## Home and section indexes

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| index.md | 220 | Keep | Home | Mission and values stay. Rename department. Reword "who this is for". Keep jobs widget. |
| Ways-of-Working/index.md | 100 | Cull | How we work/Overview | AMPFlow image goes. |
| Ways-of-Working/AMPFlow/index.md | 1,400 | Cull | How we work/Overview | Four phases and their purpose survive. Zones, FLOW, open-closed system framing go. |
| Ways-of-Working/AMPFlow/AMPFlow-Terminology.md | 650 | Cull | Glossary | "Guided not forced" and minimum viable guardrails survive in Culture/Autonomy and guardrails. |
| Ways-of-Working/Governance/index.md | 150 | Cull | | The three governance aims (prevent critical flaws, information flow, autonomy) become one sentence in Overview. |
| Ways-of-Working/Toolkit/index.md | 380 | Cull | Culture/Autonomy and guardrails | "Defaults" and tag listings go. |
| Ways-of-Working/Theory/index.md | 60 | Cull | | |
| Ways-of-Working/Tenets/index.md | 600 | Rewrite | Culture/Values and tenets | Six principles and six ideals trimmed to one page. "Permission to play" framing kept. |
| Ways-of-Working/Tenets/Continuous-Quality/index.md | 0 | Cull | | Empty. |
| Progression-Framework/index.md | 40 | Cull | | Section index no longer needed. |

## Tenets, theory, leadership

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Tenets/Continuous-Autonomy.md | 320 | Rewrite | Culture/Autonomy and guardrails | Six autonomy principles kept. Add guardrails as conversation triggers (from Knowledgebase Engineering Guardrails). |
| Tenets/Continuous-Collaboration.md | 450 | Keep | Culture/Collaboration | Eight principles are good as they are. |
| Tenets/Continuous-Improvement.md | 750 | Rewrite | Culture/Continuous improvement | Halve. Absorbs health checks, experiments, communities of practice, hit squads. |
| Tenets/Value-Focus.md | 650 | Rewrite | How we work/Roadmap and objectives; Culture/Values and tenets | Value framing and "be realistic, say no" go to Roadmap. Rest trimmed into Values. |
| Tenets/Continuous-Quality/Security-by-design.md | 450 | Keep | Quality/Security, privacy and accessibility | Ten principles kept, condensed. |
| Tenets/Continuous-Quality/Privacy-by-design | 400 | Keep | Quality/Security, privacy and accessibility | File has no extension so has never rendered. Seven principles kept, condensed. |
| Theory/Business-Value.md | 700 | Cull | | Miro embed and reading list go. One sentence on "all work must trace to business value" in Roadmap. |
| Theory/DevOps-3-Ways.md | 700 | Cull | Quality/Reliability and operations | One paragraph on flow, feedback and learning plus the three book titles as further reading. |
| Theory/Problem-Discovery.md | 600 | Rewrite | How we work/Discovery | Product trio plus specialists, activity types, Torres reference kept. |
| Leadership/Engineering-Leadership-Guide.md | 650 | Rewrite | Culture/Leadership | Merged with manifesto. |
| Leadership/Engineering-Leadership-Manifesto.md | 600 | Rewrite | Culture/Leadership | Merged with guide. Keep the identity statements, drop the manifesto links list to a single line. |
| Technical-Design-Workshops.md | 1,100 | Move | KB `Ways-of-Working/Engineering/` | Design page says collaborative design sessions exist and links the section. |

## Governance: Problem

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Problem-Governance/index.md | 300 | Cull | How we work/Discovery | |
| Problem-Governance/Problem-Definition.md | 400 | Rewrite | How we work/Roadmap and objectives | Problem statement and stakeholder map now live in the canonical objective document. Validation canvas goes. |
| Problem-Governance/Research-and-Exploration.md | 450 | Rewrite | How we work/Discovery | Problem, technical and viability discovery become the viability and feasibility checks. |
| Problem-Governance/Requirements-Definition.md | 500 | Rewrite | How we work/Design | Functional, UI and non-functional requirements survive as the content of outcome specifications and feature requirements. MoSCoW and "three months before delivery" go. |
| Problem-Governance/Solution-Design.md | 550 | Rewrite | How we work/Design | Iterative design, impact assessments, decision records, "design is complete when the team can start" survive. |
| Problem-Governance/Measuring-Success.md | 300 | Rewrite | How we work/Roadmap and objectives; Operation and support | Becomes key results and measuring outcomes after release. |
| Problem-Governance/Success-Planning.md | 0 | Cull | | Empty. |
| Problem-Governance/Release-Planning.md | 350 | Rewrite | How we work/Release and deployment | Release vs deployment, rollout plans, communication. |
| Problem-Governance/RAID-management.md | 850 | Rewrite | How we work/Delivery | One paragraph: capture risks, assumptions, issues and dependencies continuously and own them. Detail moves (see RAID toolkit page). |

## Governance: Problem ownership

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Problem-Ownership/index.md | 150 | Cull | How we work/Teams and roles | Succession and absence cover sentence kept. |
| Problem-Ownership/Problem-Owner.md | 120 | Cull | | Replaced by Product Owner. Contains `[[TableReplace]]`. |
| Problem-Ownership/Delivery-Owner.md | 60 | Cull | | No current equivalent. |
| Problem-Ownership/Product-Lead.md | 130 | Cull | How we work/Teams and roles | Responsibilities folded into Product Owner. |
| Problem-Ownership/UX-Lead.md | 110 | Cull | How we work/Teams and roles | UX as a specialist role. Title is truncated to "UX L". |
| Problem-Ownership/Engineering-Owner.md | 100 | Rewrite | How we work/Teams and roles | Role survives with the same name. |
| Problem-Ownership/Delivery-Team.md | 80 | Rewrite | How we work/Teams and roles | |
| Problem-Ownership/Other-Responsibilities.md | 30 | Cull | | Stub. |

## Governance: Delivery

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Delivery-Governance/index.md | 60 | Cull | | |
| Delivery-Governance/Workflow-Management.md | 900 | Rewrite | How we work/Delivery | Hierarchy updated to Objective, Outcome, Feature or Design, Backlog Item or Bug, Task. Item definitions kept short. Planning horizons rewritten around the roadmap. Three PNGs go. |
| Delivery-Governance/Delivery-Modelling.md | 500 | Cull | | Replaced by the roadmap and Now/Next/Later. The ROM caution survives in Delivery. |
| Delivery-Governance/Delivery-Planning.md | 550 | Cull | How we work/Design | Replaced by high-level and detailed design plus the incremental delivery plan. |
| Delivery-Governance/Responsibility-Assignment.md | 350 | Cull | | Replaced by stakeholder map in the canonical document. |
| Delivery-Governance/Delivery-Status-Reporting/index.md | 400 | Cull | How we work/Release and deployment | Replaced by the dashboards and "push and pull" communication. |
| Delivery-Governance/Delivery-Status-Reporting/Stakeholder-Engagement.md | 600 | Cull | | Malformed frontmatter. One sentence on two-way engagement survives. |
| Delivery-Governance/Time-Tracking.md | 700 | Rewrite | How we work/Delivery | One paragraph (D5). Detail to KB `Ways-of-Working/Engineering/`. |
| Delivery-Governance/Warranty.md | 350 | Cull | | D4. |
| Delivery-Governance/Support-Handover.md | 260 | Cull | How we work/Release and deployment | D4. "Service desk is ready for the release" survives as a line. |
| Delivery-Governance/After-Action-Review.md | 280 | Rewrite | How we work/Operation and support | Lessons learned after incidents and milestones. |

## Governance: Technology

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Technology-Governance/index.md | 50 | Cull | | |
| Technology-Governance/Architectural-Design.md | 250 | Rewrite | How we work/Design | Architecture described in a shared model, decisions recorded, reviewed with technical leadership. |
| Technology-Governance/Security-and-Reliability-Impact-Assessment.md | 350 | Rewrite | Quality/Security, privacy and accessibility; Quality/Reliability and operations | What an impact assessment covers. |
| Technology-Governance/Code-Peer-Review.md | 450 | Rewrite | Quality/Engineering standards | Every production change reviewed by someone else and recorded. |
| Technology-Governance/Deployment-Logs.md | 300 | Rewrite | How we work/Release and deployment | Updated to the deployment log and notice tiers. |
| Technology-Governance/Technical-Validation-Review.md | 250 | Cull | Quality/Engineering standards | One sentence: long-running work is periodically checked against standards by a principal engineer. |
| Technology-Governance/Test-Plan.md | 0 | Cull | | Empty. |
| Technology-Governance/Testing-and-Test-Reporting.md | 0 | Cull | | Empty. |

## Toolkit

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Toolkit/Quick-Start-Guide.md | 30 | Cull | | Stub. |
| Toolkit/RACI.md | 0 | Cull | | Empty. |
| Toolkit/After-Action-Review.md | 210 | Rewrite | How we work/Operation and support | Merged with the governance page. |
| Toolkit/Backlog-Refinement-Session-Guidelines.md | 1,000 | Move | KB `Ways-of-Working/Engineering/Ceremonies/` | Team-level ceremony guide. |
| Toolkit/Community-of-Practice.md | 240 | Rewrite | Culture/Continuous improvement | One paragraph. |
| Toolkit/Estimation-and-ROM.md | 1,200 | Rewrite | How we work/Delivery | ROM vs estimate and "accuracy improves as work nears" stay. Size tables and ready-to-estimate RAG move to KB `Ways-of-Working/Engineering/`. |
| Toolkit/Example-Mapping.md | 1,000 | Move | KB `Ways-of-Working/Engineering/Ceremonies/` | Design page mentions it as a technique. Two images go with it. |
| Toolkit/Hit-Squads.md | 1,400 | Rewrite | Culture/Continuous improvement | One paragraph: cross-team groups for ways-of-working problems. |
| Toolkit/Meeting-Guidelines.md | 2,100 | Rewrite | Culture/Meetings | Cut to about 500 words. SharePoint link goes. |
| Toolkit/Project-Register.md | 450 | Cull | | Replaced by the roadmap and dashboards. |
| Toolkit/Pull-Requests.md | 650 | Move | KB `Ways-of-Working/Engineering/` | Principle stays in Quality/Engineering standards. Mechanics (base branches, AB# links, draft PRs) move. |
| Toolkit/RAID.md | 2,500 | Move | KB `Ways-of-Working/Engineering/` | Principle stays in Delivery (one paragraph). Workflow diagrams, ratings and the named SME move; drop the sprint-planning variant. |
| Toolkit/Release-Notifications.md | 550 | Cull | | Superseded by the release dashboard and deployment log. The "what a good notification says" list survives in Release and deployment. |
| Toolkit/Release-Plans.md | 1,500 | Rewrite | How we work/Release and deployment | When a release plan is needed and what it contains. SharePoint location and simplified template move to KB `Ways-of-Working/Engineering/`. |
| Toolkit/Repo-Readmes.md | 2,200 | Move | KB `Ways-of-Working/Engineering/` | Standards page says every repository has a README to a standard and links it. |
| Toolkit/Runway-Planning.md | 450 | Cull | How we work/Delivery | Replaced by "keep a few weeks of ready work ahead". |
| Toolkit/Security-and-Reliability-Impact-Assessment-Template.md | 1,200 | Move | KB `Ways-of-Working/Engineering/Templates/` | |
| Toolkit/Sprint-Review-Guidence.md | 400 | Move | KB `Ways-of-Working/Engineering/Ceremonies/` | Fix the filename spelling on the way. |
| Toolkit/Staff-Engineering.md | 1,300 | Rewrite | How we work/Teams and roles | Staff engineers as cross-team specialists, about 150 words. |
| Toolkit/Structure-Experiments.md | 1,200 | Rewrite | Culture/Continuous improvement | Parameters and outcomes in about 200 words. |
| Toolkit/Team-Health-Checks.md | 1,100 | Rewrite | Culture/Continuous improvement | What and why, quarterly. Facilitator guide moves to KB `Ways-of-Working/Engineering/Ceremonies/`. |
| Toolkit/Workflow-Item-Definition.md | 1,100 | Move | KB `Ways-of-Working/Engineering/` | Azure DevOps state configuration. |
| Toolkit/Decision-Records/index.md | 2,200 | Rewrite | Quality/Decision records | Why, decision types, authority levels, RFC, in about 500 words. SharePoint log and library detail moves to KB Decision Hub. |
| Toolkit/Decision-Records/Architectural-Decision-Records.md | 850 | Rewrite | Quality/Decision records | When to write an ADR and who decides. |
| Toolkit/Decision-Records/Decision-Record-Template.md | 300 | Cull | | KB Decision Hub already has templates. |
| Toolkit/Peer-Reviewing/index.md | 450 | Rewrite | Quality/Engineering standards | Early feedback, little and often, refactors separate. |
| Toolkit/Peer-Reviewing/Performing-a-Peer-Review.md | 250 | Move | KB `Ways-of-Working/Engineering/` | Checklist. |
| Toolkit/Peer-Reviewing/Release-Plan-Review.md | 300 | Move | KB `Ways-of-Working/Engineering/` | Checklist. Principle (an independent senior reviewer) stays in Release and deployment. |

## Toolkit: Quality standards

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Quality-Standards/index.md | 1,800 | Rewrite | Quality/Engineering standards | Seven principles and the bars (coverage, WCAG AA, OWASP, pinned dependencies) stay. Detail links to KB. |
| Quality-Standards/Coding-Conventions.md | 1,200 | Move | KB `Ways-of-Working/Engineering/Standards/` | Contains repo, bucket and KMS names. |
| Quality-Standards/Endpoint-Naming-Conventions.md | 950 | Move | KB `Ways-of-Working/Engineering/Standards/` | |
| Quality-Standards/Exceptions-Best-Practices.md | 200 | Move | KB `Ways-of-Working/Engineering/Standards/` | |
| Quality-Standards/Logging-Best-Practise.md | 200 | Move | KB `Ways-of-Working/Engineering/Standards/` | References an internal library. |
| Quality-Standards/React-Best-Practises.md | 2,500 | Move | KB `Ways-of-Working/Engineering/Standards/` | |
| Quality-Standards/Unit-Integration-Testing.md | 700 | Move | KB `Ways-of-Working/Engineering/Standards/` | Coverage bar stated in Quality/Testing; CI mechanics move. |

## Toolkit: Test engineering

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Test-Engineering/Functional-Test-Strategy.md | 1,500 | Rewrite | Quality/Testing | Test levels, types, design techniques and exit criteria condensed. TODO sections dropped. |
| Test-Engineering/Exploratory-Testing.md | 650 | Rewrite | Quality/Testing | Charter, time box, pairing, debrief in one section. |
| Test-Engineering/Testing-workflow/index.md | 650 | Move | KB `Ways-of-Working/Test-Engineering/` | Repository and GitHub Actions specifics. Image goes with it. |
| Test-Engineering/Best-Practices/BDD-best-practices-for-writing-test-scenarios/index.md | 2,200 | Move | KB `Ways-of-Working/Test-Engineering/` | Seventeen images go with it. |
| Test-Engineering/Best-Practices/Playwright-Test-Automation-Guidelines.md | 1,900 | Move | KB `Ways-of-Working/Test-Engineering/` | |
| Test-Engineering/Best-Practices/Playwright-Best-Practices-For-Parameterization-With-Gherkin.md | 330 | Move | KB `Ways-of-Working/Test-Engineering/` | Three images go with it. |

New content for Quality/Shared quality and Quality/Testing comes from the Knowledgebase Regression Testing Policy and the shadow test engineer role in the service desk documents, neither of which the Playbook mentions today.

## Progression, policies, onboarding

| Page | Words | Action | Target | Notes |
|---|---|---|---|---|
| Progression-Framework/engineering-progression-framework.md | 2,800 | Keep | People/Progression framework | Rename department. Spreadsheet stays. |
| Department-Policies/Absence-Leave.md | 1,200 | Move | KB `Ways-of-Working/Department-Policies/` | D3. References YouManage and sprints; fix on the way. |
| Department-Policies/Flexible-Working.md | 250 | Keep | People/Hybrid working | |
| Department-Policies/Hackathons.md | 1,400 | Keep | People/Hackathons | Trim by a third. SharePoint link goes. |
| Department-Policies/Training.md | 900 | Keep | People/Training | Trim. Replace HR system name with "the HR system". |
| Onboarding/Engineering/index.md | 650 | Rewrite | People/Onboarding | Four phases kept, shorter. Knowledgebase people-directory link goes. |
| Onboarding/Engineering/Engineering-Buddy-Guide.md | 850 | Keep | People/Onboarding | Merged into the onboarding page as a section, or kept as a second page if it reads better. |
| Onboarding/Engineering/Line-Managers-Duties-For-New-Starters.md | 950 | Move | KB `Onboarding/Engineering/` | Links a SharePoint checklist. |
| Onboarding/Engineering/Onboarding-for-managers.md | 450 | Move | KB `Onboarding/Engineering/` | |

## Totals

| Action | Pages | Words today |
|---|---|---|
| Keep | 9 | ~7,700 |
| Rewrite into new pages | 39 | ~29,300 |
| Move to Knowledgebase | 24 | ~25,100 |
| Cull | 36 | ~10,200 (empty pages, stubs, indexes and the superseded governance layer) |

Target after rewrite: about 31 pages and under 18,000 words.

## Assets

- `docs/Ways-of-Working/assets/*.png` (12 AMPFlow and governance diagrams): cull.
- `docs/Ways-of-Working/Toolkit/assets/*` (example mapping, RAID): move with their pages.
- `docs/Ways-of-Working/Toolkit/Test-Engineering/**/*.png|jpg`: move with their pages.
- Fonts, logo, favicon, stylesheet: keep.
- `docs/Progression-Framework/*.xlsx`: keep.
