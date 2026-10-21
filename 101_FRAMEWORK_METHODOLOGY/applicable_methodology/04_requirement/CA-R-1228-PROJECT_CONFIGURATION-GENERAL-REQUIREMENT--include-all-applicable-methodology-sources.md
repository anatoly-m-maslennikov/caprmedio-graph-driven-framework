---
subjects:
  governs: "Applicable Methodology Source Set"
  depends_on:
    ["Methodology Source", "Core Meta-Model", "Project Configuration", "Extension", "Entity/Node/Continuant/Project.Framework Settings"]
version: 20
updated_at: "2026-10-19 15:56:04 +0400"
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
  source_atom_revision: 20
  source_sha256: c5a9e95c4ab658d66e02b1252d5e148a01fa60a932fd887badc2d2a1a096f081
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Include **all** applicable Methodology Sources

## Scope

The Applicable Methodology source set under current Framework Instance Settings.

## Claim

the Applicable Methodology source set **must** include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** installed Extension Source applicable under the current Framework Instance Settings. **when** **none** is applicable, the Extension contribution **is empty** **without** a rule requiring zero installed Extensions **or** a Carrier for an empty INSTALLED_EXTENSIONS collection.

## Details
