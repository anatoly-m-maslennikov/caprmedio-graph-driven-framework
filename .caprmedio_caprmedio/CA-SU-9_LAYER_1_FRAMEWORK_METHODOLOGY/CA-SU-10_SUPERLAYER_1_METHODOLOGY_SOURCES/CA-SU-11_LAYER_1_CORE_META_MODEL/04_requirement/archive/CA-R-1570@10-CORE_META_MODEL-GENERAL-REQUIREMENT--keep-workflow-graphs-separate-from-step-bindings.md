---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph/Relation/Type: On Result'
version: 10
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-R-1508
  - CA-R-1509
  - CA-R-1513
  - CA-R-1563
  - CA-R-1569
atom_id: CA-R-1570@10
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
global_tier: 10
---
# Summary

Keep Workflow graphs separate from Step bindings

## Scope

Workflow graph schemes and Step bindings.

## Claim

a Workflow Atom **must** own **only** its graph scheme: Step references, typed directed Relations, entry points, transition conditions, **and** terminal outcomes.

- the referenced Step Atoms own Action references, parameters, **and** input bindings.
- reusable Action Atoms own Action behavior.
- the graph **must not** independently repeat those Step bindings **or** Action definitions; folder nesting **and** file order **must not** replace its declared control flow.

## Details
