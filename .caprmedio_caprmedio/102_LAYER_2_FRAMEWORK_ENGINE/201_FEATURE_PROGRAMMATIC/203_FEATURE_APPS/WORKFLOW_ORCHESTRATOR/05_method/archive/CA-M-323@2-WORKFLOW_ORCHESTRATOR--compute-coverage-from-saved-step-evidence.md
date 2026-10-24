---
atom_id: CA-M-323@2
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 03:06:32 +0400
subjects:
  governs: Workflow Run/coverage
  depends_on:
  - Workflow
  - Step
  - Action
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Journal
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
