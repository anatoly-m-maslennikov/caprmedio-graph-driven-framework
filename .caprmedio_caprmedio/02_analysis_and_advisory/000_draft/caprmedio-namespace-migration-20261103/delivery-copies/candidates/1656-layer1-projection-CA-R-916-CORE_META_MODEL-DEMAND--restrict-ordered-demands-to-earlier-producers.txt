---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-R-932@37
atom_id: CA-R-916
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Demand
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-916-CORE_META_MODEL-DEMAND--restrict-ordered-demands-to-earlier-producers.md
  source_atom_id: CA-R-916
  source_atom_revision: 37
  source_sha256: da9fa72b049661910f47f34e5e6ddd306c62e879d7047865a8b08f300d2e5ca7
  original_relations_sha256: c20ed3844d666cd523ff76d7355fb5c2277a21d8c1137804e80822202d14a70b
---
## Summary
Restrict ordered Demands to earlier Producers

## Claim scope

Demand Atoms whose Consumer Atom Scope Unit and Producer Claim Target Scope Unit are ordered siblings.

## Claim

**if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.
