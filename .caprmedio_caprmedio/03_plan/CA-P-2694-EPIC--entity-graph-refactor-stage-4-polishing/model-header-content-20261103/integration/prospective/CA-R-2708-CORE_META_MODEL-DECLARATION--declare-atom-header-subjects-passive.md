---
atom_id: CA-R-2708
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Passive
version: 1
relations: {}
tier: 3
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2708-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects-passive.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Subjects.Passive

## Claim

### Prose Claim

Passive Subjects identify direct contextual dependencies.

### Formal Claim

```CFEL
Atom.Header.Subjects.Passive{:0..1}: [string]{:0+};
Atom.Header.Subjects.Passive.*[]{:0};
COUNT(Atom.Header.Subjects.Passive: $) = COUNT(DISTINCT Atom.Header.Subjects.Passive: $)
```
