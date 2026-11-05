---
atom_id: CA-R-1359
ref_id: CA-R-1359
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
tier: 3
relations:
  child_of:
  - CA-R-1270
status: Active
version: 30
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-1359-CORE_META_MODEL-RULE--define-claim-value-set.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1359-CORE_META_MODEL-RULE--define-claim-value-set.md
  source_atom_id: CA-R-1359
  source_atom_revision: 30
  source_sha256: dfc86690375e751e6647bddaede0514cb2a285b4429c770f9cf20086196b5b65
  original_relations_sha256: 0fa3c79fd31c027d4114f94dde8bf00fa821694f342a125a29903cd019455764
---
## Summary

Define Claim Value Set

## Claim

### Prose Claim


Claim Value Set expressions.


a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.
