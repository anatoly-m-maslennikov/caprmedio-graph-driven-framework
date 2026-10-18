---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Status"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Atom.Status"]
version: 8
updated_at: "2026-10-18 03:33:39 +0400"
relations: {"relates_to": ["CA-R-1412"]}
atom_id: "CA-R-1539"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1539-CORE_META_MODEL-GENERAL-REQUIREMENT--register-core-plan-status-values.md
  source_atom_id: CA-R-1539
  source_atom_revision: 8
  source_sha256: e9e4c2aafb9c61cac081626289ae39de0c1c828d7f3b988583c0f8cc43055b17
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register Core Plan Status Values

## Scope

Core Plan Status values.

## Claim

the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

## Details
