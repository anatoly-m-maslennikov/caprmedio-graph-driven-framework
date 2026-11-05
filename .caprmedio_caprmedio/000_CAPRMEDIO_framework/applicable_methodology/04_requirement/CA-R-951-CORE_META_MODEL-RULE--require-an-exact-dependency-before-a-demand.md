---
atom_id: CA-R-951
ref_id: CA-R-951
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
tier: 6
relations:
  child_of:
  - CA-R-933
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-951-CORE_META_MODEL-RULE--require-an-exact-dependency-before-a-demand.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-951-CORE_META_MODEL-RULE--require-an-exact-dependency-before-a-demand.md
  source_atom_id: CA-R-951
  source_atom_revision: 33
  source_sha256: 9f9fae2ad6cd685ad29467918025e3528d976aa88c20f5bbf2b4a3b3646386a9
  original_relations_sha256: c28d84bac21e6f7cc7bfde47da5b055ffadede71bf17c4da3c8b2456c1f525ea
---
## Summary
Require an exact dependency before a Demand

## Claim

### Prose Claim


Consumer Scope Units with an accepted Goal.


a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Goal authorizes an exact dependency on the demanded Producer result.
