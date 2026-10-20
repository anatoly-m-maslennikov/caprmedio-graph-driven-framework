---
atom_id: CA-R-1981
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Identifier"
relations:
  child_of:
  - CA-R-1176
version: 3
updated_at: "2026-10-19 15:56:12 +0400"
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1981-PROJECT_CONFIGURATION--define-project-framework-settings-identifier.md
  source_atom_id: CA-R-1981
  source_atom_revision: 3
  source_sha256: a080b5ba82a5a9c6ee958bab8b4a31438d1535371ed18eee8698186cb3ca0fee
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
# Summary

Define Project.Framework Settings.Identifier

## Scope

the identifier of the Project's authoritative Framework Settings configuration.

## Claim

Framework Settings Identifier identifies the Project's authoritative Framework Settings configuration, **not** an Atom.

## Details

Evidence: CA-R-1402 defines the owning configuration; CA-R-1404 keeps it outside the Atom type; CA-D-358 supplies its concrete identifier. Candidate #6 decision 11 places Project under Continuant; concrete CAPRMEDIO identity encodings belong in Project Configuration. This definition does not duplicate the concrete identifier spelling or create an Atom ID.
