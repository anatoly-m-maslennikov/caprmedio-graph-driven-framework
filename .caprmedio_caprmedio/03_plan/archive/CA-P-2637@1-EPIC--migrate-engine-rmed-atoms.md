---
atom_id: CA-P-2637@1
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
version: 1
updated_at: 2026-10-25 01:18:41 +0400
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
