---
atom_id: CA-R-1981
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier.ID
relations:
  child_of:
  - CA-R-1176
version: 16
tier: 3
role: Requirement
form: Rule
updated_at: 2026-11-02 08:06:47 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1981-PROJECT_CONFIGURATION-RULE--define-project-framework-settings-identifier.md
  source_atom_id: CA-R-1981
  source_atom_revision: 16
  source_sha256: c4b146655abdf2aa92f9c2555ab46a2119cbeb7238ab71242b4c99ada17168c4
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Identifier

## Claim scope

the Identifier of the Project’s authoritative Framework Instance Settings Carrier.

## Claim

The Identifier of the Project’s authoritative Framework Instance Settings Carrier is `caprmedio_framework_settings`.

## Details

Evidence: CA-R-1402@27 defines the owning configuration; CA-R-1404 keeps it outside the Atom type; CA-D-358 supplies its concrete identifier. Candidate #6 decision 11 places Project under Continuant; concrete CAPRMEDIO identity encodings belong in Project Configuration. This definition does not duplicate the concrete identifier spelling or create an Atom ID.
