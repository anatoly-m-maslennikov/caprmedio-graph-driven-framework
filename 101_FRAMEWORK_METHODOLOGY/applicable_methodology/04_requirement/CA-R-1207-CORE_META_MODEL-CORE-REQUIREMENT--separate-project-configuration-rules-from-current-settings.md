---
subjects:
  governs: "Project Configuration"
  depends_on:
    ["Entity/Continuant/Object/Project", "Extension", "Entity/Continuant/Object/Project.Framework Settings"]
version: 16
updated_at: "2026-10-15 18:41:13 +0000"
relations: {}
atom_id: "CA-R-1207"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1207-CORE_META_MODEL-CORE-REQUIREMENT--separate-project-configuration-rules-from-current-settings.md
  source_atom_id: CA-R-1207
  source_atom_revision: 16
  source_sha256: 2259561f3e6a53f5f1f1c830be3f8f3e6296eaaa86fc47b36915b6c42450cbee
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Separate Project Configuration Rules from Current Settings

## Scope

Ownership of Project-specific expansion rules, constraints, defaults, current Extension activation, and selected Extension revisions.

## Claim

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.

## Details
