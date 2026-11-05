---
atom_id: CA-R-2784
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Container.scope_unit
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 06:17:36 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2784@1-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-container-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare Atom.Header.Container.scope_unit

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Container.scope_unit :: [string]{::0..1};

Atom.Header.Container.scope_unit.*[]{::0}
```

### Prose Claim

The value is the stable ID of the containing Scope Unit.
