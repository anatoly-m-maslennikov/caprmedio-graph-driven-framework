---
identity:
  id: CA-R-3072
  ref_id: CA-R-3072@1
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State
  tier: 3
state:
  status: archived
  version: 1
  updated_at: 2026-11-11 16:27:40 +0400
destination:
  file:
    name: CA-R-3072@1-CORE_META_MODEL-DECLARATION--declare-atom-header-state.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---

## Summary

Declare Atom.Header.State

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.State{::1} :: []{::0};

Atom.Header.State.*[in (Status, Version, Updated At)]{::3};

Atom.Header.State.Status ;> Atom.Header.State.Version;

Atom.Header.State.Version ;> Atom.Header.State.Updated At
```
