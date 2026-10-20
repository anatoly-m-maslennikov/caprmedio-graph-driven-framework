---
atom_id: CA-R-1979
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Confidence"
relations:
  child_of:
  - CA-R-1176
version: 3
updated_at: "2026-10-19 15:56:11 +0400"
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1979-PROJECT_CONFIGURATION--define-project-framework-settings-confidence.md
  source_atom_id: CA-R-1979
  source_atom_revision: 3
  source_sha256: dffe5112bf5c13252ffbab2fff962ee54dec3ad08c9182ad6a53e51b09e10a3f
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
# Summary

Define Project.Framework Settings.Confidence

## Scope

the Confidence grouping in the Project's Framework Settings.

## Claim

Confidence **means** the group of Framework Settings defaults for the declared Confidence Thresholds.

## Details

Evidence: CA-R-1652 defines the necessary-information threshold default; CA-R-380 defines the semantic-resolution threshold default. These define the child settings, not the parent grouping. Candidate #6 decision 8 retains Settings as the default source, and decision 18 distinguishes Project settings from the framework's name. This grouping adds no threshold, override layer or mandatory value. Concrete CAPRMEDIO setting definitions belong in Project Configuration.
