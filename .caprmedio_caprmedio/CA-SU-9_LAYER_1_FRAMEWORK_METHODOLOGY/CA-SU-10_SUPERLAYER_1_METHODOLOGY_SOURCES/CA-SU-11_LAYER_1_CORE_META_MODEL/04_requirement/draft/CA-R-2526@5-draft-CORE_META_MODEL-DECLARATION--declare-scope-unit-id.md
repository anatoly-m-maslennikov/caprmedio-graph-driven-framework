---
atom_id: CA-R-2526
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit.ID
version: 5
updated_at: 2026-11-05 12:58:42 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2526@5-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare Scope Unit ID

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.ID: [string]{:1};

Scope Unit.ID.*[]{:0};

# instances
Scope Unit//$unit;

$unit.ID{:1}
```

## Semantics

Every Scope Unit has a stable ID. A non-root Scope Unit keeps its ID through moves and renames; the ID distinguishes those operations from removal. `CA-SU--1` identifies the predefined Scope Unit named `world`.
