---
identity:
  id: CA-R-970308655
  ref_id: CA-R-970308655
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern).Header.Context.Concern
  tier: 3
state:
  status: active
  version: 1
  updated_at: 2026-11-11 16:27:40 +0400
destination:
  file:
    name: CA-R-970308655-CORE_META_MODEL-DECLARATION--declare-atom-header-context-concern.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Atom/(.Header.Context.Role := Concern).Header.Context.Concern

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern{::1} :: []{::0};

Atom/(.Header.Context.Role in (Concern)).Header.Context.Concern.*[in (Priority)]{::1}
```
