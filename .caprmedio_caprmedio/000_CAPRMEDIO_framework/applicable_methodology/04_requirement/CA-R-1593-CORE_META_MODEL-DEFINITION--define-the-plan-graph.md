---
atom_id: CA-R-1593
ref_id: CA-R-1593
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Carrier
tier: 1
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1593-CORE_META_MODEL-RULE--define-the-plan-graph.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1593-CORE_META_MODEL-DEFINITION--define-the-plan-graph.md
  source_atom_id: CA-R-1593
  source_atom_revision: 25
  source_sha256: 4701e30abbbcb36dfc17be9ed7b7b65099fbdd2b61328852bc34a73c24d94000
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define the Plan Graph

## Claim

### Prose Claim


the Plan Graph.


the Plan Graph **means** a Projection whose nodes reference authoritative Plan Atoms **and** whose graph-owned Relations represent Plan containment **and** blocking. explicit once-owned Plan Relation declarations are the sources of those facts; optional directory placement represents them **without** becoming another declaration.
