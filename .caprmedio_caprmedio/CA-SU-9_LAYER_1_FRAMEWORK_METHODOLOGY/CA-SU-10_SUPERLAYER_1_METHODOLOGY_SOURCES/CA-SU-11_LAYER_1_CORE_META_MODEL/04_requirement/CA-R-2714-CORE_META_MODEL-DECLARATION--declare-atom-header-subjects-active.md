---
atom_id: CA-R-2714
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
version: 2
updated_at: 2026-11-04 05:21:15 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2714-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects-active.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Subjects.Active

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Subjects.Active: [string]{:0..1};

Atom.Header.Subjects.Active.*[]{:0};

# instances
Atom//$atom;

IF ($atom.Header.Status >| Status Group = Current)
THEN ($atom.Header.Subjects.Active{==1})
```
