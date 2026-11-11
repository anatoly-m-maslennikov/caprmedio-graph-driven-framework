---
atom_id: CA-M-265
ref_id: CA-M-265
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//evaluation_for
tier: 2
status: Active
version: 26
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-265-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-evaluation-groups-from-checked-authority.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Derive evaluation groups from checked authority

## Claim

### Prose Claim


derivation of Er, Em, and Ed groups from checked authority.


**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018-CORE_META_MODEL-CORE-REQUIREMENT--register-evaluation-targets **must not** require an invented classification.
