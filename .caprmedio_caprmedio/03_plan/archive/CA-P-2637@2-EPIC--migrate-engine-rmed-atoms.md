---
atom_id: CA-P-2637@2
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
version: 2
updated_at: 2026-10-25 15:52:51 +0400
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
