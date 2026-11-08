---
atom_id: CA-R-1314
ref_id: CA-R-1314
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form := Applicable Methodology)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DERIVED_FROM
tier: 1
status: Active
version: 34
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1314-PROJECT_CONFIGURATION-RULE--preserve-source-atom-revision-identity-in-applicable-methodology.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1314-PROJECT_CONFIGURATION-RULE--preserve-source-atom-revision-identity-in-applicable-methodology.md
  source_atom_id: CA-R-1314
  source_atom_revision: 34
  source_sha256: 59f5b2e568ac50e3aac5ed320ea3d0548c2f28367c180546b95b767413d73d62
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Preserve Source Atom Revision Identity in Applicable Methodology

## Claim

### Prose Claim


The direct source relation of each projected Applicable Methodology member.


Applicable Methodology **must** retain each member’s **`=1`** direct DERIVED_FROM relation **to** that member’s exact source Atom Revision.
