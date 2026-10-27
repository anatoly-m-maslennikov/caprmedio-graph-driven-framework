---
atom_id: CA-R-1822@5
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 01:37:42 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Workflow Run.Provenance
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Initiative
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Execution Identity/Source Binding
relations:
  relates_to:
  - CA-R-1525
  - CA-R-1720
  - CA-R-1728
tier: 3
type: Rule
---
# Summary

Bind selected Run identities, revisions and lineage

## Scope

Actual Run provenance produced through shared RUN_SUPPORT for the selected
scope. Definition Atoms and their execution records remain distinct.

## Claim

RUN_SUPPORT **must** retain distinct actual Workflow Run, Step Run, and Action
Run identities with their exact admitted definition bindings and actual
lineage in the canonical Events Journal.

## Details

- A Workflow Run records its Workflow definition and the ordered admitted
  Workflow graph, Step definitions, and Action definitions with exact Atom
  IDs, Versions, paths, and sealed digests. A Step Run records its exact Step
  definition and its real parent Workflow Run. An Action Run records its exact
  Action definition and its real parent Step/Workflow Run when one exists.
- A standalone actual Action Run has its own Action Run identity and no
  fictitious Workflow Run or Step Run. Nested invocations record only their
  actual parent Run/Step and any actual predecessor/successor Run relation;
  ending a predecessor never starts, approves, or completes a successor.
- The stable action identity, Run identity, definition identity, event
  identity, and Initiative identity have different meanings and must not be
  collapsed. Repeated report delivery, recovery, or Tool transport does not
  manufacture another Run identity.
- Completed effects retain their original bindings and lineage. Revalidation
  of remaining work may record a new decision but must not rewrite history,
  reset retry allowance, or replay a completed effect.
- Projection Action Runs additionally retain target Projection, exact selected
  source Atom revisions and Journal selection, generator/configuration
  reference, and produced revision only when it exists, as required by
  CA-R-1728.
