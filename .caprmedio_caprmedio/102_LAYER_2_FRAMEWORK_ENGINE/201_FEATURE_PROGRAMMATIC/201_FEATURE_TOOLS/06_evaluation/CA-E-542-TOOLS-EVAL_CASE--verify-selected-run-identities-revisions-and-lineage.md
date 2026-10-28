---
atom_id: CA-E-542
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Provenance
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1822
tier: 4
---
# Summary

Verify selected Run identities, revisions and lineage

## Scope

Canonical selected-Run evidence for actual nested and standalone invocation.

## Claim

Every actual selected Run remains reconstructable with its distinct identity,
exact definition revisions, and real lineage.

## Test case

Execute one selected Workflow containing two Actions with one nested/handoff
edge, then one standalone read-only Action. Capture start and terminal events,
definition bindings, Initiative/action identities, and reconstructed Process
Log view.

## Acceptance criteria

- The Workflow, every actual Step, and every Action have distinct Run
  identities and exact admitted definition ID/Version/path/digest bindings.
- Nested evidence names only actual parents and predecessors/successors.
  Ending one Run neither creates nor implies successor authorization.
- The standalone Action has no fictitious Workflow/Step parent, and recovery or
  duplicate report delivery adds no new Run.
- The reconstructed view references canonical event identities and retains the
  same Initiative without replacing it by session, queue, or adapter identity.

## Details

The fixture must use exact captured source revisions, not reconstructed current
definitions, so it can distinguish preserved bindings from later source drift.
The checked assertion is the Claim above.

## Failure disposition

Reject collapsed identities, missing revisions, invented parents, or a view
that cannot reconstruct the captured canonical evidence.
