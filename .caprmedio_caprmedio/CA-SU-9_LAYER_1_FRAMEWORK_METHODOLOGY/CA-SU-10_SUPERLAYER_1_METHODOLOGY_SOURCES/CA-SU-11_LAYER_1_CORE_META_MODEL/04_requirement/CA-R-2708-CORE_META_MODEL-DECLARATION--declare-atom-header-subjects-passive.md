---
atom_id: CA-R-2708
ref_id: CA-R-2708
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Topics.Dependencies
version: 1
tier: 3
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2708-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects-passive.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Declare Atom.Header.Subjects.Passive

## Claim

### Prose Claim

Dependencies identify direct contextual dependencies.

### Formal Claim

```CFEL
# model
Atom.Header.Topics.Dependencies{::0..1}:: [string]{::0+};

Atom.Header.Topics.Dependencies.*[]{::0};

# instances
$atom[<Atom>];

COUNT(VALUES($atom.Header.Topics.Dependencies)) = COUNT(DISTINCT VALUES($atom.Header.Topics.Dependencies))
```
