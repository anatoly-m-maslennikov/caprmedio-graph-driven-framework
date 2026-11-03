---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Selection
  passive:
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-833
  - CA-R-808
  - CA-R-879
atom_id: CA-E-481
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-481-CORE_META_MODEL-POLICY--validate-the-normative-authority-hierarchy.md
  source_atom_id: CA-E-481
  source_atom_revision: 22
  source_sha256: 39c5a4b20aa926e6da42669fde2f29d4e18049c3bda0c0fbf0da751bd33e7b9d
  original_relations_sha256: be79cc6e03c2c93b1ca7941d6b2dc8bfbffc174d340a258e50efb1ec789ee673
---
## Summary

Validate the normative-authority hierarchy

## Claim scope

the active normative-authority subgraph.

## Claim

the Evaluation of the active normative-authority subgraph **must** fail **when** **any** declared authority-bearing direct edge lacks its registered typing **or** the directed subgraph **contains** a cycle under CA-R-833.

## Details

- the evaluated input is the active normative-authority subgraph selected under its registered direct Relation types. unresolved selection **or** typing **must not** be reported as a conforming hierarchy.
- retain the distinction between declared direct authority edges **and** inverse-derived views under CA-R-808 **and** CA-R-879. an inverse view **must not** become another independently declared edge **in** the cycle check.

this representation-independent criterion does **not** select a graph-construction implementation **or** a concrete test specimen.
