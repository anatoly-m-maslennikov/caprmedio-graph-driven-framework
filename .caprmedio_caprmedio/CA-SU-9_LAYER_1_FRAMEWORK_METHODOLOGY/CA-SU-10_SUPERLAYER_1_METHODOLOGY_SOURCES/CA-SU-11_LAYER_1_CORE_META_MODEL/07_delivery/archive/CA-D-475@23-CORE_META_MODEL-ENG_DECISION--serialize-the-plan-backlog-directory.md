---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status: Backlog'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Label'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status'
  - Entity/Carrier/Directory
version: 23
updated_at: 2026-10-29 10:13:51 +0400
relations: {}
atom_id: CA-D-475@23
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize the Plan Backlog directory

## Claim scope

the Plan Backlog Directory and version-labeled Plan Carrier locations.

## Claim

the Plan Backlog Directory **must** be `03_plan/001_backlog`; it is a Status container, **not** a Plan Atom. a Version-labeled Plan uses the ordinary Plan Carrier grammar under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems rather than an independently identified Version Plan Collection **or** special `version-<VERSION>` container.
