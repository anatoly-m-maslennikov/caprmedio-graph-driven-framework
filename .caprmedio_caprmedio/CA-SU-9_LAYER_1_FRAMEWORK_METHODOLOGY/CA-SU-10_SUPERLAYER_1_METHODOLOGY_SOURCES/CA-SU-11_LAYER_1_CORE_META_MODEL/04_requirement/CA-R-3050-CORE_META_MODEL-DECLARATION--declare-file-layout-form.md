---
identity:
  id: CA-R-3050
  ref_id: CA-R-3050
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)/(.Header.Context.Form := File Layout)
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom.Header.Destination.File
  tier: 3
state:
  status: active
  version: 1
  updated_at: '2026-11-11T18:17:52+04:00'
destination:
  file:
    name: CA-R-3050-CORE_META_MODEL-DECLARATION--declare-file-layout-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare File Layout Form

## Claim

### Prose Claim

A File Layout Claim specifies how delivered files are named, where they are placed, or how files and folders are arranged. Paths are relative to the repository root.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Delivery)).Header.Context.Form :: File Layout;
```
