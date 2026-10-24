---
subjects:
  governs: Artifact.Status
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
version: 19
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1312@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary
Separate Governed Transitions from Status Values

## Scope
Artifact Revision Status values associated with admission, acceptance, commitment, activation, completion, **or** archival.

## Claim
an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.

## Details
the same distinction applies **when** a Workflow uses several Steps **to** establish the Status value.
