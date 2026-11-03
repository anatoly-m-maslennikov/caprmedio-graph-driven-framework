---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection/(.Form := Applicable Methodology)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation//DERIVED_FROM
version: 34
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1314
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1314-PROJECT_CONFIGURATION-RULE--preserve-source-atom-revision-identity-in-applicable-methodology.md
  source_atom_id: CA-R-1314
  source_atom_revision: 34
  source_sha256: cec92e7bf49897f7c845b134e882cdfa961d46532fa3f117d0cb2708801a8e15
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Preserve Source Atom Revision Identity in Applicable Methodology

## Claim scope

The direct source relation of each projected Applicable Methodology member.

## Claim

Applicable Methodology **must** retain each member’s **`=1`** direct DERIVED_FROM relation **to** that member’s exact source Atom Revision.
