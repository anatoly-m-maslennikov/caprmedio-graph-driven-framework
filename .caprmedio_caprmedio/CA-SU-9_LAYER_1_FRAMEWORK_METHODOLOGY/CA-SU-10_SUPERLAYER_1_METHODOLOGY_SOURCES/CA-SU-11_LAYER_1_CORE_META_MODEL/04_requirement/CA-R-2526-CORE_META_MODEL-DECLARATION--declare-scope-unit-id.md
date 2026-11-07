---
atom_id: CA-R-2526
ref_id: CA-R-2526
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.ID
tier: 3
status: Active
version: 6
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-2526-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Scope Unit ID

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.ID:: [string]{::1};

Scope Unit.ID.*[]{::0};

# instances
Scope Unit//$unit;

$unit.ID{::1}
```

## Semantics

Every Scope Unit has a stable ID. A non-root Scope Unit keeps its ID through moves and renames; the ID distinguishes those operations from removal. `CA-SU--1` identifies the predefined Scope Unit named `world`.
