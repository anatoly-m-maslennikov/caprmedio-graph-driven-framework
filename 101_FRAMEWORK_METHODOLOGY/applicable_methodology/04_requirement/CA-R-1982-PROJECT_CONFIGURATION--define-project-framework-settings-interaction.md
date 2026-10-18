---
atom_id: CA-R-1982
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Project.Framework Settings.Interaction"
relations:
  child_of:
  - CA-R-1176
version: 2
updated_at: "2026-10-18 03:34:59 +0400"
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1982-PROJECT_CONFIGURATION--define-project-framework-settings-interaction.md
  source_atom_id: CA-R-1982
  source_atom_revision: 2
  source_sha256: be1382ecc1d5baa6504dc15df9a915297e07b72e2ac9b80edce0a58d74435996
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
# Summary

Define Project.Framework Settings.Interaction

## Scope

the Interaction grouping in the Project's Framework Settings.

## Claim

Interaction **means** the group of Framework Settings choices that govern presentation of information to the Operator.

## Details

Evidence: CA-R-1628 defines reporting-mode values; CA-R-1439 limits effects to presentation; CA-R-1440 preserves mandatory information. These define the child setting and its constraints, not the parent grouping. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This grouping adds no authorization, workflow, validation or safety behavior.
