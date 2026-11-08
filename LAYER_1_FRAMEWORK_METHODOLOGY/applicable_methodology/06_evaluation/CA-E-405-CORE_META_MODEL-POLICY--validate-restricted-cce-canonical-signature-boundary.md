---
atom_id: CA-E-405
ref_id: CA-E-405
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Transformation
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Validation
tier: 5
relations:
  evaluation_for:
  - CA-R-1360
  - CA-M-240
status: Active
version: 31
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-405-CORE_META_MODEL-EVAL_POLICY--validate-restricted-cce-canonical-signature-boundary.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-405-CORE_META_MODEL-POLICY--validate-restricted-cce-canonical-signature-boundary.md
  source_atom_id: CA-E-405
  source_atom_revision: 31
  source_sha256: f9b03d20d7f6951c48d864b301436362ea783e4c25017696f086fc2dda0ad934
  original_relations_sha256: bf40f64d58f9585b75c6cc377531519804c7350c17c4520e03b0c0afdf328dc8
---
## Summary

Validate Restricted CCE Canonical Signature Boundary

## Claim

### Prose Claim


Canonical Signature derivations evaluated against the restricted CCE boundary.


the Evaluation **must** reject a Canonical Signature derivation **if** any of the following is true:

- it rewrites one source Claim.
- it treats one Canonical Signature as authority.
- it accepts mixed **and** **or** groups.
- it rewrites negation, implication, **where**, **without**, temporal condition, quantifier, extension-defined CCE Operator, **or** unparseable prose.
- it fails **to** flatten nested same-operator groups.
- it retains duplicate atomic predicates.
- it yields different Canonical Signatures from Boolean groups that differ **only** by operand order.
