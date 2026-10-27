---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Status: Backlog'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Label'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Status'
  - Subject/Engineering/Carrier/Directory Carrier
version: 16
updated_at: 2026-10-24 10:48:25 +0400
relations:
  relates_to:
  - CA-D-469
  - CA-R-1542
  - CA-R-1576
atom_id: CA-D-475@16
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize the Plan Backlog directory

## Scope

the Plan Backlog Directory and version-labeled Plan Carrier locations.

## Claim

the Plan Backlog Directory **must** be `03_plan/001_backlog`; it is a Status container, **not** a Plan Atom. a Version-labeled Plan uses the ordinary Plan Carrier grammar under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems rather than an independently identified Version Plan Collection **or** special `version-<VERSION>` container.

## Details
