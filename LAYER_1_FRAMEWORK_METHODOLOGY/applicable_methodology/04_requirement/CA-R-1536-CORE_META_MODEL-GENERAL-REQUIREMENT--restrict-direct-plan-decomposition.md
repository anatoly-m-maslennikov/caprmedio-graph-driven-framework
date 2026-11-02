---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan"]
version: 9
updated_at: "2026-10-19 15:53:23 +0400"
relations: {"relates_to": ["CA-R-1576", "CA-R-1579", "CA-R-1590"]}
atom_id: "CA-R-1536"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1536-CORE_META_MODEL-GENERAL-REQUIREMENT--restrict-direct-plan-decomposition.md
  source_atom_id: CA-R-1536
  source_atom_revision: 9
  source_sha256: e88af3ca4bcabe7aa4bccfbed5e71ed20a1b61aa0de501c1660062cb0c3c0fed
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Restrict Direct Plan Decomposition

## Scope

direct `DECOMPOSES_INTO` relations between Plan Atoms.

## Claim

`DECOMPOSES_INTO` **must** connect **only** distinct Plan Atoms; **any** Plan **may** decompose into other Plans regardless of their Labels, **without** requiring incoming decomposition.

## Details
