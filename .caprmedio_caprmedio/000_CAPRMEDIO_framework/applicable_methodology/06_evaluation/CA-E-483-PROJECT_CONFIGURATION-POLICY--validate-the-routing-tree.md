---
atom_id: CA-E-483
ref_id: CA-E-483
container:
  scope_unit: CA-SU-13
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Architecture <+ Communication
tier: 2
relations:
  evaluation_for:
  - CA-R-1640
status: Active
version: 21
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-E-483-PROJECT_CONFIGURATION-EVAL_POLICY--validate-the-routing-tree.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-483-PROJECT_CONFIGURATION-POLICY--validate-the-routing-tree.md
  source_atom_id: CA-E-483
  source_atom_revision: 21
  source_sha256: 41b0d0813846a3573512aab08c84f92ffeaf4aa155ef69192774763d9d97314b
  original_relations_sha256: 70ae4acf9d304b2ecfd0b5d3361ca7a3e827a9d3780fff2904873c52d63c7501
---
## Summary

Validate the routing tree

## Claim

### Prose Claim


the CAPRMEDIO Routing Tree.


the Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-RULE--register-one-canonical-routing-tree **must** reject a routing tree **when** **any** of the following is present:

## Details

- an invalid schema;
- an unknown target;
- ambiguous precedence;
- a duplicate route identity;
- an authority effect that is **not** explicitly declared.
