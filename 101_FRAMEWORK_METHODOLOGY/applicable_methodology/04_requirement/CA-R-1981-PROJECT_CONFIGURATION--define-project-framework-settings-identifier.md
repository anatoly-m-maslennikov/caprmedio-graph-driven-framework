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
  governs: "Entity/Continuant/Node/Project.Framework Settings.Identifier"
relations:
  child_of:
  - CA-R-1176
version: 2
updated_at: "2026-10-18 03:34:59 +0400"
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1981-PROJECT_CONFIGURATION--define-project-framework-settings-identifier.md
  source_atom_id: CA-R-1981
  source_atom_revision: 2
  source_sha256: 646ae3f7bb38ecc8ed5bc0248786e517530248395df8bffef7a385ff29633a06
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
