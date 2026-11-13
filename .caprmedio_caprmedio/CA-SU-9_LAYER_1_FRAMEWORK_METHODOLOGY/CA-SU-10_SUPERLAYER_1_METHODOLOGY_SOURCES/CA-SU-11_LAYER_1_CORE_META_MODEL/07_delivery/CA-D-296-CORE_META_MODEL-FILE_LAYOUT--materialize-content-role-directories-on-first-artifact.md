---
atom_id: CA-D-296
ref_id: CA-D-296
container:
  scope_unit: CA-SU-11
role: Delivery
form: file_layout
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 3
status: active
version: 34
updated_at: '2026-11-12T19:34:39.244837+00:00'
carrier_destination:
  file:
    name: CA-D-296-CORE_META_MODEL-FILE_LAYOUT--materialize-content-role-directories-on-first-artifact.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Materialize Content Role Directories on First Artifact

## Claim

### Prose Claim

Within a Scope Unit, derive the Role folder from the Role Declaration selected by `Header.Context.Role`.

1. Pad its Role Order Number to at least two decimal digits.
2. Encode the canonical Role name in lowercase snake case.
3. Join the two parts with one underscore.

Create the folder when the first Atom needs it. The applicable Status and Container layout determines the remaining placement.

### Formal Claim

```python
placement_rules = ({"kind": "role_root"},)
```
