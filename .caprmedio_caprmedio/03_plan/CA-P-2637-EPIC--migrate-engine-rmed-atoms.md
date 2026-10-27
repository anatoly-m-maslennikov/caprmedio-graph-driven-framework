---
atom_id: CA-P-2637
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
version: 6
updated_at: 2026-10-26 23:25:22 +0400
relations: {}
tier: 3
---
# Summary

Migrate Engine RMED Atoms

## Objective

After the Methodology migration is complete, revise the Engine Subject system
and Scope Unit structure, then migrate all Current Engine RMED Atoms,
including PROGRAMMATIC, APPS, TOOLS and the other Engine descendants.

## Details

### Engineering Subject cleanup — next prerequisite

[P2665](CA-P-2665-EPIC--refine-engineering-subject-branch.md) now owns the focused Engineering Subject cleanup across the Current RMEDO source set. It reviews Continuant, Occurrent and Aspect placement, duplicate Git Subjects and scattered Implementation topics before drafting and applying accepted corrections. Consume its checked branch and source mappings here; do not repeat the same review or treat it as completion of this Engine Epic. Broader Scope Unit revision and the remaining Engine migration stages remain pending.


### First task completed — checked source application

P2638 applied the approved Subject structure and Domain/Engineering temporal
distinction. Readback checks3,961 Current PRMEDO sources:3,886 updates with normal
predecessors and75 unchanged heads. Only the three required taxonomy/Subject
definitions and this Epic/Task's progress bodies changed; other content stayed
unchanged. R2149's operative Subject reference follows the same rename without
changing its condition.

The actual Core, project Methodology and Engine Subject projections were
regenerated with stable IDs006–008 and source counts800/411/1027. C603 is
Resolved2 with the Operator's dual Domain/Engineering decision. Pure Engineering
topics remain direct Engineering where no temporal classification was justified.
The164 noncanonical source literals retain their prior dispositions; this
structural task neither invents their meanings nor reports them migrated.

No other Engine migration stage, Scope Unit change, code, runtime, MCP, test
suite, release or Git operation was executed. Existing Drafts/Archives were not
migrated; newly created predecessor archives are the normal update history.

### Approved runtime distinction — first-task update

The Operator resolved C603: Domain and Engineering both have Continuant and
Occurrent branches. Modeled Action/Step/Workflow Runs belong to Domain/Occurrent;
technical sessions and actual tool/app runtimes belong to Engineering/Occurrent.
Technical components and carriers use Engineering/Continuant. UX remains a
Graph Node branch for MCP interface and health-page appearance, not backend code.

This supersedes the earlier temporary deferral and extends only this first
structural task. It does not start the other Engine migration stages. Abstract
Engineering policy topics may stay directly under Engineering; do not invent
temporal classifications for them. Generic Node and Node.Type move to Graph
Node and Graph Node.Type, not to Domain-specific properties.

### First task — reshape the Subject graph roots

Execute [CA-P-2638](CA-P-2637-EPIC--migrate-engine-rmed-atoms/done/01-CA-P-2638-TASK--reshape-subject-graph-roots.md)
before the remaining Engine migration stages. The Operator approved this structure:

```text
Subject
    Graph Node
        Domain
            Continuant
            Occurrent
        Engineering
        Documentation
        Product
    Graph Relation
    Graph Rule
```

Migrate the corresponding canonical prefixes in Current P/R/M/E/D/O Subjects
across the actual source set so the graph has one coherent root structure.
Update only the defining taxonomy rules needed by this approved change and
rebuild the three existing Subject projections. Keep the Product specialization
and all remaining path suffixes. Do not turn this into general content,
instance-name, Terms Graph, Scope Unit, code, tool or runtime migration.
Preserve existing Drafts and Archives; create normal predecessors for Current
updates. This explicit first task permits the bounded cross-selection prefix
change; the rest of this Epic remains Engine RMED-only and follows the order below.

### Coordinated authority cutover — accepted 2026-10-25

The Operator approved Core for reusable authority definitions and Project
Configuration for this project's application. The connected Engine Evaluation
changes belong to this later Epic, not an ancestry waiver in CA-P-1959.

Carry this bounded Methodology follow-up with the Engine consumer migration:

- Review R029's project-application placement in Project Configuration and
  R030's reusable strict-mode authority placement in Core. Keep their stable
  identities unless Summary or Content Role changes.
- Inspect the complete connected authority closure, including R037/R038,
  R1430/R833 and Core R1671/R1672. Local ownership is not content applicability.
  Preserve generic Core independence from a project-specific application;
  retain, rebind or remove links only when their actual governing meanings
  support it. Do not infer a new parent or permission from folder placement.
- Repair the Engine evaluation consumers E120/E122/E149 as part of that
  coordinated cutover. They currently target Project-root R030 as an ancestor;
  moving R030 alone to Core would make those links invalid across branches.
- Re-read all incoming and outgoing current endpoints before publication.
  Keep ancestry and numeric Tier constraints, the sole admitted Config→Core
  prerequisite, coverage and applicability intact. Add no broader waiver.
- Preserve predecessors and rebuild the affected source-derived views after
  the complete accepted cutover. Record actual effects separately from Drafts.

R029→R1430 and R030→R833 remain known present conflicts until this work is
performed. Neither is reported applied or passing by its Methodology transfer.
No source cutover, Engine change, code or runtime action is authorized by merely
recording this follow-up. Existing Methodology-first ordering remains.

This is a separate Epic from CA-P-1959. Do not start Engine migration while
Methodology is unfinished. Preserve previous applied work and existing proposals.

First review the Subject system and Scope Units. Propose their boundaries and
placement before moving or rewriting Atoms; do not infer Subjects from Roles
or folders. Do not introduce new Domain entities without the Operator.

Then execute in order:

1. Migrate Subjects under the reviewed Subject and Scope Unit model.
2. Add missing RMED Atoms.
3. Archive obsolete RMED Atoms with affected consumers accounted for.
4. Fix properties and the necessary Governing Configuration data.
5. Update Content last.

Use new Drafts and refine them in iterations. Record source application
separately from preparation. Preserve existing Drafts, Archives, protected
owners, Terms/instance-name deferrals and unrelated changes. A Current update
creates its usual predecessor archive; existing history is not migrated.

No code, tools, tests, runtime, MCP deployment or release implementation is
included. Existing C/A and Engine P instance migration are not added by this
RMED-only scope. Spec needs no named Selection: directly select Active RMED
Atoms in the specified Scope Unit.

## Definition of Done

- Methodology completion is recorded before Engine migration starts.
- Engine Subjects and Scope Units are reviewed and their accepted model saved.
- All Current Engine RMED sources are accounted for as migrated, retained,
  archived or explicitly deferred; proposals are not counted as application.
- The five migration stages and affected Subject views have checked evidence.
- No code/runtime implementation is included or implied.
