---
atom_id: CA-R-1775
ref_id: CA-R-1775
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
tier: 1
relations:
  child_of:
  - CA-M-447
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1775-CORE_META_MODEL-RULE--let-parents-own-immediate-child-goals.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Let Parents Own Immediate Child Goals

## Claim

### Prose Claim


parent Scope Units and their immediate child Scope Units.


**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.
