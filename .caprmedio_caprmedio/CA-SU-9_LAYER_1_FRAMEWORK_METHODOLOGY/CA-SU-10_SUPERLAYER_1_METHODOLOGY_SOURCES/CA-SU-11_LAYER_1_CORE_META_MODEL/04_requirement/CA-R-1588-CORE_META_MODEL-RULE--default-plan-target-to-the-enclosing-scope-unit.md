---
atom_id: CA-R-1588
ref_id: CA-R-1588
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Subjects.Active'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Scope Unit
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
tier: 1
status: Active
version: 26
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1588-CORE_META_MODEL-RULE--default-plan-target-to-the-enclosing-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Default Plan target to the enclosing Scope Unit

## Claim

### Prose Claim


Plans and their resolved Claim Target Scope Units.


a Plan’s Claim Target Scope Unit **must** be resolved from its one active Subject under CA-R-2102. Its current Scope Unit is established by containment; Plan nesting **or** Label does not independently select a target, and a Hub does not become one by default.
