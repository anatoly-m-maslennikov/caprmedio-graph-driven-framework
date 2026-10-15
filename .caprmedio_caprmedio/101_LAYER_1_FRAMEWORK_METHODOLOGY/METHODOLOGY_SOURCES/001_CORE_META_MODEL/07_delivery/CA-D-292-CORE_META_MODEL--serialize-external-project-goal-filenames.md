---
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal/Filename"
  depends_on:
    ["Entity/Continuant/Actor/Type: Operator", "Project/Scope Unit", "Entity/Continuant/Object/Project", "Project Name"]
version: 16
updated_at: "2026-10-15 18:50:55 +0000"
relations: {}
atom_id: "CA-D-292"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Serialize External Project Goal Filenames

## Scope

external Project Goal filenames.

## Claim

**every** external Project Goal filename **must** match `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>` **without** a Project prefix, Content Role letter, **or** number.

the `<PROJECT_SCOPE>` component **must** be the exact registered Project Name.

## Details
