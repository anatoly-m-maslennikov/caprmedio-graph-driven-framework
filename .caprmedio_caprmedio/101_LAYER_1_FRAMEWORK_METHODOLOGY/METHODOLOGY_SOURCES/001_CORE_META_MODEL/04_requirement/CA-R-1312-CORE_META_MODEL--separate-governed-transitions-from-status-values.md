---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Rule
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
version: 24
updated_at: 2026-10-27 19:59:53 +0400
relations: {}
atom_id: CA-R-1312
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary
Separate Governed Transitions from Status Values

## Scope
Artifact Revision Status values associated with admission, acceptance, commitment, activation, completion, **or** archival.

## Claim
an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.

## Details
the same distinction applies **when** a Workflow uses several Steps **to** establish the Status value.
