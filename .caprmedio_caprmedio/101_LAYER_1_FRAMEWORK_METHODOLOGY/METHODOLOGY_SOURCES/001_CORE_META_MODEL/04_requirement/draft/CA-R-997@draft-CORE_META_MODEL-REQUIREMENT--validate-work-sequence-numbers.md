---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Work Sequence Number"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom/Content Role: Plan.Work Sequence Number"]
version: 20
updated_at: "2026-10-16 12:00:24 +0000"
relations:
  child_of:
    - CA-R-991
    - CA-R-992
atom_id: "CA-R-997@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Validate Work Sequence Numbers

## Scope

supplied Work Sequence Numbers for direct Plans decomposing the same Hub or sharing the same top-level Plan container.

## Claim

**every** supplied Work Sequence Number **must** be a unique positive ordinal among direct Plans decomposing the same Hub **or** sharing the same top-level Plan container.

## Details
