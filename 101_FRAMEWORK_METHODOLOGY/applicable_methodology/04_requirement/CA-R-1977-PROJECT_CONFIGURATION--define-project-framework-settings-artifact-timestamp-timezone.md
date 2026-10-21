---
atom_id: CA-R-1977
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Artifact Timestamp Timezone"
relations:
  child_of:
  - CA-R-1176
version: 3
updated_at: "2026-10-19 15:56:11 +0400"
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1977-PROJECT_CONFIGURATION--define-project-framework-settings-artifact-timestamp-timezone.md
  source_atom_id: CA-R-1977
  source_atom_revision: 3
  source_sha256: 10019fcc30a1248512f6988564feb42fcb19fb51708b2e6e33ebe6bac3c2eb36
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
# Summary

Define Project.Framework Settings.Artifact Timestamp Timezone

## Scope

the Artifact timestamp timezone setting in Framework Settings.

## Claim

Artifact Timestamp Timezone **means** the Framework Settings value that supplies the timezone interpretation used when emitting Artifact timestamps.

## Details

Evidence: CA-D-390 supplies the timezone interpretation and its concrete encoding. Candidate #6 keeps Settings attached to Project and keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no format, allowed value or default; those remain separate Delivery rules.
