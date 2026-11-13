---
atom_id: CA-R-2509
ref_id: CA-R-2509@4
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
tier: 3
status: archived
version: 4
updated_at: '2026-11-11T18:56:17+04:00'
carrier_destination:
  file:
    name: CA-R-2509@4-CORE_META_MODEL-DECLARATION--declare-concern.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom/(.Role := Concern)

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Context.Role :: Concern;

Atom/(.Header.Context.Role := Concern) >| (Role Order Number == 1);
```

## Semantics

A Concern identifies a question, conflict, or problem.
