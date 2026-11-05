---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-833
  - CA-R-808
  - CA-R-879
atom_id: CA-E-481
ref_id: CA-E-481
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Evaluation
form: Eval Policy
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-E-481-CORE_META_MODEL-EVAL_POLICY--validate-the-normative-authority-hierarchy.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
---
## Summary

Validate the normative-authority hierarchy

## Claim

### Prose Claim


the active normative-authority subgraph.


the Evaluation of the active normative-authority subgraph **must** fail **when** **any** declared authority-bearing direct edge lacks its registered typing **or** the directed subgraph **contains** a cycle under CA-R-833.

## Details

- the evaluated input is the active normative-authority subgraph selected under its registered direct Relation types. unresolved selection **or** typing **must not** be reported as a conforming hierarchy.
- retain the distinction between declared direct authority edges **and** inverse-derived views under CA-R-808 **and** CA-R-879. an inverse view **must not** become another independently declared edge **in** the cycle check.

this representation-independent criterion does **not** select a graph-construction implementation **or** a concrete test specimen.
