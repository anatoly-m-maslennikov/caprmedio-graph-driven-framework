---
atom_id: CA-D-559@6
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal
  depends_on:
  - Implementation
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Carrier
version: 6
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-R-1745
  - CA-R-1720
  - CA-D-549
  - CA-D-504
---
# Summary

Deliver runtime Journals to configured sinks

## Scope

technical and business runtime Journal Carriers.

## Claim

runtime technical **and** business Journals **may** be delivered **to** an explicitly configured local database, remote database, **or** governed logging sink. these Carriers **need not** reside under `.caprmedio_<project_name>/_journal/` **or** `.caprmedio_runtime/`.

## Details

Journal classification and recorded-history authority are independent of storage technology. The configuration identifies the intended sink; applicable production logging policy remains in force. The shared Project-control Work Journal and persistent view Projections retain their separate _journal and _projection locations. Runtime cleanup and sink migration must preserve accepted Journal history; this Delivery does not authorize history deletion or change retention policy.
