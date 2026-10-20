---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Status: Backlog"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom/Content Role: Plan.Label", "Entity/Node/Continuant/Atom/Content Role: Plan.Status", "Entity/Carrier/Directory Carrier"]
version: 9
updated_at: "2026-10-19 15:55:55 +0400"
relations: {"relates_to": ["CA-D-469", "CA-R-1542", "CA-R-1576"]}
atom_id: "CA-D-475"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-475-CORE_META_MODEL-STANDARD--serialize-the-plan-backlog-directory.md
  source_atom_id: CA-D-475
  source_atom_revision: 9
  source_sha256: 3ec3f1eb7c99e29e2d29737b6b5d4de8475f1ac0c43939ab372a6519ef803b3e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize the Plan Backlog directory

## Scope

the Plan Backlog Directory and version-labeled Plan Carrier locations.

## Claim

the Plan Backlog Directory **must** be `03_plan/001_backlog`; it is a Status container, **not** a Plan Atom. a Version-labeled Plan uses the ordinary Plan Carrier grammar under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems rather than an independently identified Version Plan Collection **or** special `version-<VERSION>` container.

## Details
