---
subjects:
  governs: "Applicable Methodology Source Set"
  depends_on:
    ["Methodology Source", "Core Meta-Model", "Project Configuration", "Extension", "Entity/Continuant/Object/Project.Framework Settings"]
version: 19
updated_at: "2026-10-18 07:48:59 +0400"
relations: {}
atom_id: "CA-R-1228"
content_role: "Requirement"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1228-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--include-all-applicable-methodology-sources.md
  source_atom_id: CA-R-1228
  source_atom_revision: 19
  source_sha256: a0aa6891b0d9e5673ba0d2f789d99604ea99ee1df265bde54639654bb088c671
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Include **all** applicable Methodology Sources

## Scope

The Applicable Methodology source set under current Framework Instance Settings.

## Claim

the Applicable Methodology source set **must** include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** installed Extension Source applicable under the current Framework Instance Settings. **when** **none** is applicable, the Extension contribution **is empty** **without** a rule requiring zero installed Extensions **or** a Carrier for an empty INSTALLED_EXTENSIONS collection.

## Details
