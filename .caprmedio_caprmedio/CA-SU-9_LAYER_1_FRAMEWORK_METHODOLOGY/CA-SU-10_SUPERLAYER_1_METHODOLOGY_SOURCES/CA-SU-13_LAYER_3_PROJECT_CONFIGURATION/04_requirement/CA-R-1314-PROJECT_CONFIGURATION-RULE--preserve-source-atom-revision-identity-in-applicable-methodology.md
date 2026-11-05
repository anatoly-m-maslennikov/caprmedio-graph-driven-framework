---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form := Applicable Methodology)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DERIVED_FROM
version: 34
updated_at: 2026-11-02 08:06:47 +0400
atom_id: CA-R-1314
ref_id: CA-R-1314
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-R-1314-PROJECT_CONFIGURATION-RULE--preserve-source-atom-revision-identity-in-applicable-methodology.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
---
## Summary

Preserve Source Atom Revision Identity in Applicable Methodology

## Claim

### Prose Claim


The direct source relation of each projected Applicable Methodology member.


Applicable Methodology **must** retain each member’s **`=1`** direct DERIVED_FROM relation **to** that member’s exact source Atom Revision.
