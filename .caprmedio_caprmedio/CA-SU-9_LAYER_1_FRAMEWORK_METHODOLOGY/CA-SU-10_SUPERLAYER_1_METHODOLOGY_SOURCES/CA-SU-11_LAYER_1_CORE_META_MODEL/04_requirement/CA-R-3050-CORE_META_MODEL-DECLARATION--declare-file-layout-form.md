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
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)/(.Header.Context.Form
      := File Layout)
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom.Header.Destination.File
  tier: 3
state:
  status: active
  version: 2
  updated_at: '2026-11-12T17:23:54+00:00'
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

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Delivery

class FileLayout(Delivery):
    pass

declare_entity(entity_class=FileLayout, entity_name='File Layout', qualification_property_path="Atom.Header.Context.Form")
```
