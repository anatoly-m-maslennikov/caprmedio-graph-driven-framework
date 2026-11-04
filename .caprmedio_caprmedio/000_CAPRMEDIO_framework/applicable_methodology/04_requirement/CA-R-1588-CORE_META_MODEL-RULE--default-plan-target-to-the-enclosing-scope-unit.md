---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Subjects.Active'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
  - CAPRMEDIO_MODEL <+ Scope Unit
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1588
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1588-CORE_META_MODEL-RULE--default-plan-target-to-the-enclosing-scope-unit.md
  source_atom_id: CA-R-1588
  source_atom_revision: 26
  source_sha256: a50e103ea2571f5b8b6e647510f0f8bfe0a4a30dc4c2194d54502e0fa3fc1131
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Default Plan target to the enclosing Scope Unit

## Claim

### Prose Claim


Plans and their resolved Claim Target Scope Units.


a Plan’s Claim Target Scope Unit **must** be resolved from its one active Subject under CA-R-2102. Its current Scope Unit is established by containment; Plan nesting **or** Label does not independently select a target, and a Hub does not become one by default.
