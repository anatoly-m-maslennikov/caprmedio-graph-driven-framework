---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/Project.Settings.Project Name", "Entity/Continuant/Node/Project"]
version: 20
updated_at: "2026-10-18 07:30:14 +0400"
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
  source_atom_revision: 20
  source_sha256: 9a7d835b1c04bc5f279c73723d36b0dc8ef9f919ea5f29f80f9fb19471549102
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
