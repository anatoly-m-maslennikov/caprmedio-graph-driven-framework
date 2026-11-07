---
atom_id: CA-D-386
ref_id: CA-D-386
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 3
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-386-CORE_META_MODEL-DECISION--serialize-concern-priority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-386-CORE_META_MODEL-ENG_DECISION--serialize-concern-priority.md
  source_atom_id: CA-D-386
  source_atom_revision: 23
  source_sha256: 136385e619afafd6ed5397518b4644d5d1a4a96bfe8a4ee727d03c5768e1ae39
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Concern Priority

## Claim

### Prose Claim


Concern Atom Carriers and non-Concern Content Role Atom Carriers.


a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.
