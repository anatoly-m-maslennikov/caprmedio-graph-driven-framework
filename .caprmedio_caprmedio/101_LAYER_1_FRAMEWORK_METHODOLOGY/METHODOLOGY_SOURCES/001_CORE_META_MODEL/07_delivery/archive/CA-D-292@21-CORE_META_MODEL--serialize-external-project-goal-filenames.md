---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Project.Settings.Project Name", "Entity/Node/Continuant/Project"]
version: 21
updated_at: "2026-10-19 15:55:24 +0400"
relations: {}
atom_id: CA-D-292@21
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: Archived
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
