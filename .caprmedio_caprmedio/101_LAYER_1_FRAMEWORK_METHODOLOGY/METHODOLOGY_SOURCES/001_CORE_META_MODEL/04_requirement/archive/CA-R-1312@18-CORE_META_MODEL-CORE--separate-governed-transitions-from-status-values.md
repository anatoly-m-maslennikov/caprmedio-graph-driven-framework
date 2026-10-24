---
subjects:
  governs: Artifact.Status
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
version: 18
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-R-1312@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary
Separate Governed Transitions from Status Values

## Scope
Artifact Revision Status values associated with admission, acceptance, commitment, activation, completion, **or** archival.

## Claim
an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.

## Details
the same distinction applies **when** a Workflow uses several Steps **to** establish the Status value.
