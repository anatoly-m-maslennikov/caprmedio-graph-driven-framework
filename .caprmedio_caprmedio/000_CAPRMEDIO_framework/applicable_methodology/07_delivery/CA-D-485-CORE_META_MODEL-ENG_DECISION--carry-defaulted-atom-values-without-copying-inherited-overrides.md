---
atom_id: CA-D-485
ref_id: CA-D-485
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
tier: 3
status: Active
version: 27
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-D-485-CORE_META_MODEL-DECISION--carry-defaulted-atom-values-without-copying-inherited-overrides.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-485-CORE_META_MODEL-ENG_DECISION--carry-defaulted-atom-values-without-copying-inherited-overrides.md
  source_atom_id: CA-D-485
  source_atom_revision: 27
  source_sha256: 4d049dbd0949371e55f6211b85e412f6c09cf3ccfed44c2d48b8706f025e2b69
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Carry defaulted Atom values without copying inherited overrides

## Claim

### Prose Claim


defaulted Atom values and inherited external settings.


a writer **must** preserve the distinction between a defaulted Atom Property **and** an inherited external setting:

- a required Atom value selected by applying a default is still carried at its canonical internal location; equality **to** that default does **not** permit omitting the value.
- an unselected optional override remains absent; do **not** copy an inherited effective setting into a locally selected override.
- retain an explicit override even **when** it currently equals the inherited value, because later upstream changes **must not** change that selection.
