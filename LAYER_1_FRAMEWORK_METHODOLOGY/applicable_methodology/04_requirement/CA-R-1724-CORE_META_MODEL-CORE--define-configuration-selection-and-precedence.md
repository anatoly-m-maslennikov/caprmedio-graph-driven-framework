---
subjects:
  governs: "Configuration Selection and Precedence"
  depends_on:
    ["Entity/Node/Continuant/Project.Framework Settings", "Extension", "Tool"]
version: 24
updated_at: "2026-10-19 15:53:53 +0400"
relations: {}
atom_id: "CA-R-1724"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1724-CORE_META_MODEL-CORE--define-configuration-selection-and-precedence.md
  source_atom_id: CA-R-1724
  source_atom_revision: 24
  source_sha256: 1b55c7768c16a6ddf42adcde1d91b42edf5748946c57247885ff310368c19800
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Configuration selection and precedence

## Scope

Framework Instance Settings Artifact selection of available Tools **and** Extensions.

## Claim

the Framework Instance Settings Artifact **may** select, combine, parameterize, activate **in** foreground **or** background, **or** disable available Tools **and** Extensions **and** **must** resolve composition precedence explicitly **without** changing **any** selected capability's governed meaning. installation establishes availability, **not** activation: an installed Extension **may** remain disabled, **and** its retained settings do **not** enable it **unless** the Framework Instance Settings Artifact explicitly does so. the Framework Instance Settings Artifact **must** own the current activation selection **and** selected revision of **every** selected Extension.

## Details
