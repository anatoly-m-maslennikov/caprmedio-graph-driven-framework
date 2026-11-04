---
atom_id: CA-R-1981
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
relations:
  child_of:
  - CA-R-1176
version: 17
tier: 3
role: Requirement
form: Rule
updated_at: 2026-11-03 23:25:51 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1981-PROJECT_CONFIGURATION-RULE--define-project-framework-settings-identifier.md
  source_atom_id: CA-R-1981
  source_atom_revision: 17
  source_sha256: dc82e9f6d7d2f5fccd6dba94aa5f2654a571940ea889560eab3e0301d14044ca
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Identifier

## Claim

### Prose Claim


the Identifier of the Project’s authoritative Framework Instance Settings Carrier.


The Identifier of the Project’s authoritative Framework Instance Settings Carrier is `caprmedio_framework_settings`.

## Details

Evidence: CA-R-1402@27 defines the owning configuration; CA-R-1404 keeps it outside the Atom type; CA-D-358 supplies its concrete identifier. Candidate #6 decision 11 places Project under Continuant; concrete CAPRMEDIO identity encodings belong in Project Configuration. This definition does not duplicate the concrete identifier spelling or create an Atom ID.
