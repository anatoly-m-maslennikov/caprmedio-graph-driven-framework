---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Project.Settings.Project Name", "Entity/Node/Continuant/Project"]
version: 21
updated_at: "2026-10-19 15:55:24 +0400"
relations: {}
atom_id: "CA-D-292"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-292-CORE_META_MODEL--serialize-external-project-goal-filenames.md
  source_atom_id: CA-D-292
  source_atom_revision: 21
  source_sha256: 83f7c98ac620cd26062c9b756d821dc6b9d256f23695255340ab04eda1cab76d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize External Project Goal Filenames

## Scope

external Project Goal filenames.

## Claim

**every** external Project Goal filename **must** match `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>` **without** a Project prefix, Content Role letter, **or** number.

the `<PROJECT_SCOPE>` component **must** be the exact registered Project Name.

## Details
