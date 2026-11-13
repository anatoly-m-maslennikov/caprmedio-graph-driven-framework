---
atom_id: CA-R-2784
ref_id: CA-R-2784@1
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Container.scope_unit
tier: 3
status: archived
version: 1
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2784@1-CORE_META_MODEL-DECLARATION--declare-atom-header-container-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Atom.Header.Container.scope_unit

## Claim

### Prose Claim

The value is the stable ID of the containing Scope Unit.
### Formal Claim

```CFEL
# model
Atom.Header.Context.Container.scope_unit :: [string]{::0..1};

Atom.Header.Context.Container.scope_unit.*[]{::0}
```

