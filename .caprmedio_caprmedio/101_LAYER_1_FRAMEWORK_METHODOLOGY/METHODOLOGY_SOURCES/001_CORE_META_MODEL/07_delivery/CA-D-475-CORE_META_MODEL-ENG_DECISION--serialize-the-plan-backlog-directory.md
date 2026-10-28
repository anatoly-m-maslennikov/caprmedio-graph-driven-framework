---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Status: Backlog'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Label'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Status'
  - Subject/CAPRMEDIO/Carrier/Directory
version: 20
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-475
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
