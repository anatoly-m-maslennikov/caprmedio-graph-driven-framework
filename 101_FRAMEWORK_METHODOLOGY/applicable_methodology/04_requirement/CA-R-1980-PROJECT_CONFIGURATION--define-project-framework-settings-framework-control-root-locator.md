---
atom_id: CA-R-1980
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Framework Control-Root Locator"
relations:
  child_of:
  - CA-R-1176
version: 3
updated_at: "2026-10-19 15:56:12 +0400"
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1980-PROJECT_CONFIGURATION--define-project-framework-settings-framework-control-root-locator.md
  source_atom_id: CA-R-1980
  source_atom_revision: 3
  source_sha256: 8b132f2b394e37e5f19d9383cfbc6c63da021f6ad2baaa7f322ce2e978f562bf
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
# Summary

Define Project.Framework Settings.Framework Control-Root Locator

## Scope

the Project's framework control-root reference in Framework Settings.

## Claim

Framework Control-Root Locator **means** the Framework Settings reference to the Project's governed framework control directory.

## Details

Evidence: CA-D-370 requires the locator to resolve to the Directory Carrier prescribed by CA-D-317 without selecting another authority root. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no path or alternative authority root; those remain Delivery rules.
