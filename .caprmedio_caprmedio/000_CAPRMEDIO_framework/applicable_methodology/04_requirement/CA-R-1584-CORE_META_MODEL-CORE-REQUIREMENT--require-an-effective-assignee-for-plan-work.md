---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Assignee"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Actor"]
version: 8
updated_at: "2026-10-18 03:33:42 +0400"
relations: {"relates_to": ["CA-R-1575"]}
atom_id: "CA-R-1584"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1584-CORE_META_MODEL-CORE-REQUIREMENT--require-an-effective-assignee-for-plan-work.md
  source_atom_id: CA-R-1584
  source_atom_revision: 8
  source_sha256: c2e238bf54d4909ca77e0eb1cf80a39f9923c8e08de93583fd31caa9ffc0d1ea
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require an effective Assignee for Plan work

## Scope

Plan Atoms with their own work content, excluding pure Hubs **without** their own work.

## Claim

**every** Plan Atom with its own work content **must** have **`=1`** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.

## Details
