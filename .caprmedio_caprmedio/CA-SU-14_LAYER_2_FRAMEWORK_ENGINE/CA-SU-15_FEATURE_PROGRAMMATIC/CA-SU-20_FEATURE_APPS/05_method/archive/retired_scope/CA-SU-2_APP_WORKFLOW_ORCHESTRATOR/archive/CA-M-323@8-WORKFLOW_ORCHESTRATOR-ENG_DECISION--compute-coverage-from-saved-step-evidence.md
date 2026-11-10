---
atom_id: CA-M-323@8
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run.Coverage
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
type: Eng Decision
tier: 3
---
# Summary

Compute coverage from saved Step evidence

## Scope

RMED Atoms Base Revise execution in WORKFLOW_ORCHESTRATOR.

## Claim

the Coverage Gate **must** derive its accounting from the frozen request **and** saved results without another semantic Atom evaluation.

## Details

- compare gather identities, ordered paths **and** frozen source/rule observations.
- check every required slot for concluded status **and** evidence; retain coverage gaps **and** blockers.
- use existing finding-disposition **and** completion predicates for fix coverage.
- record the gate once per phase in the existing Run state, Journal **and** full report; recovery reuses the same evidence rather than replaying completed effects.
- run gates as durable DBOS Steps; keep coverage interruption distinct from scheduler failure.
