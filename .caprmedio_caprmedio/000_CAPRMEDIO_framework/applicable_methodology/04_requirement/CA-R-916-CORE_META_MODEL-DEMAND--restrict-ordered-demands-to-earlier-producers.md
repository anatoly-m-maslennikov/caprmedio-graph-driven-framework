---
atom_id: CA-R-916
ref_id: CA-R-916
container:
  scope_unit: CA-SU-11
role: Requirement
form: Demand
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
tier: 5
relations:
  child_of:
  - CA-R-932@37
status: Active
version: 37
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-916-CORE_META_MODEL-DEMAND--restrict-ordered-demands-to-earlier-producers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-916-CORE_META_MODEL-DEMAND--restrict-ordered-demands-to-earlier-producers.md
  source_atom_id: CA-R-916
  source_atom_revision: 37
  source_sha256: 853d97cf87819979a9f98e565bf63f21d8583b2401671ade2371b0668f9136b5
  original_relations_sha256: c20ed3844d666cd523ff76d7355fb5c2277a21d8c1137804e80822202d14a70b
---
## Summary
Restrict ordered Demands to earlier Producers

## Claim

### Prose Claim


Demand Atoms whose Consumer Atom Scope Unit and Producer Claim Target Scope Unit are ordered siblings.


**if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.
