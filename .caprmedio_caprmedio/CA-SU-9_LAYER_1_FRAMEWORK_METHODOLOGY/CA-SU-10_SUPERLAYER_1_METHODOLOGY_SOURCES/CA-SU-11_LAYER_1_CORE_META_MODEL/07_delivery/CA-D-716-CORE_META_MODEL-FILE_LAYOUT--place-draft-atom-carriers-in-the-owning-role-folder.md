---
identity:
  id: CA-D-716
  ref_id: CA-D-716
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: file_layout
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Status >| Status Group := Draft
    dependencies:
    - CAPRMEDIO_MODEL <+ Carrier
  tier: 3
state:
  status: active
  version: 5
  updated_at: '2026-11-12T19:34:49.576334+00:00'
destination:
  file:
    name: CA-D-716-CORE_META_MODEL-FILE_LAYOUT--place-draft-atom-carriers-in-the-owning-role-folder.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Place Draft Atom Carriers in the owning Role folder

## Claim

### Prose Claim

Place Draft Atom Markdown Carriers in the shared `<owning scope unit>/<role folder>/<status folder>/` directory. The Atom's owning Scope Unit and Role determine this directory.

### Formal Claim

```python
placement_rules = ({"kind": "status", "role": None, "status": "draft", "base": "role", "folder": "<status folder>"},)
```
