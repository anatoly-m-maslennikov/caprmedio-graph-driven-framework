---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Form
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
version: 37
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-923
atom_id: CA-R-924
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-924-CORE_META_MODEL-RULE--register-core-relational-atom-classifications.md
  source_atom_id: CA-R-924
  source_atom_revision: 37
  source_sha256: 619c712e6624da6971daa939dfc052332fc7f6d5b754fe43d4996021e780f79e
  original_relations_sha256: a04b2740365697ee3e4186cfbec88741d45af9b261c1a52f42e455a9e0171e3d
---
## Summary
Register Core Relational Atom Classifications

## Claim

### Prose Claim


Allowed qualified Types of Relational Atom.


the Core contribution **to** allowed qualified Types of Relational Atom **must** be (`Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)`, `Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)`, `Atom/(.Header.Role := Plan)/(.Header.Form := Plan)`); a Plan is relational **only** **when** its actual Claim target differs under the Relational Atom definition, **not** merely because it has decomposition, blocking, **or** a particular Label.
