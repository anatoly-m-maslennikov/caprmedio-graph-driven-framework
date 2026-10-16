---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Status: Backlog"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom/Content Role: Plan.Label", "Entity/Continuant/Object/Atom/Content Role: Plan.Status", "Entity/Carrier/Directory Carrier"]
version: 7
updated_at: "2026-10-16 12:03:33 +0000"
relations: {"relates_to": ["CA-D-469", "CA-R-1542", "CA-R-1576"]}
atom_id: "CA-D-475@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize the Plan Backlog directory

## Scope

the Plan Backlog Directory and version-labeled Plan Carrier locations.

## Claim

the Plan Backlog Directory **must** be `03_plan/001_backlog`; it is a Status container, **not** a Plan Atom. a Version-labeled Plan uses the ordinary Plan Carrier grammar under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems rather than an independently identified Version Plan Collection **or** special `version-<VERSION>` container.

## Details
