---
atom_id: CA-R-1705
ref_id: CA-R-1705
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")/(.Header.Form := Rationale)
tier: 2
relations:
  child_of:
  - CA-R-1702
status: Active
version: 33
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1705-CORE_META_MODEL-RULE--requirement-create-rationale-after-its-subject.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1705-CORE_META_MODEL-RULE--requirement-create-rationale-after-its-subject.md
  source_atom_id: CA-R-1705
  source_atom_revision: 33
  source_sha256: 49259b43b0bc01d7caf09fa1479cdb0cf53e4e0a33452e8c9c0ff0a8ffe75352
  original_relations_sha256: 86f48d79fbbfe66ffab2b0bb686a446bbbe206535c96d6e0d3b25f21670f9677
---
## Summary

Requirement — Create Rationale **after** its subject

## Claim

### Prose Claim


Rationale Atoms and their pre-existing specification subjects.


a Rationale is an Analysis & Advisory Atom created **only** **after** **every** specification Atom it explains already exists. the Rationale stores the directed relation **to** its subjects; specification Atoms contain **none** of (embedded Rationale, persisted Rationale backlink).

Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Evaluation condition, Delivery rule, **or** acceptance meaning requires a new applicable specification Atom rather than a Rationale.

## Primary claim

a Rationale follows **and** points **to** its pre-existing specification subjects **without** modifying them.

