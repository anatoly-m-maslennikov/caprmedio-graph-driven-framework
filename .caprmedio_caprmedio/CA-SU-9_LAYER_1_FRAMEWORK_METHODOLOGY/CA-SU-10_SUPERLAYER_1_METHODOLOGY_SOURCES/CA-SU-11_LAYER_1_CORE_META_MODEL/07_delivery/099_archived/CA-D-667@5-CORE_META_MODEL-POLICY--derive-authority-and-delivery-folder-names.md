---
identity:
  id: CA-D-667
  ref_id: CA-D-667@5
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: policy
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
    dependencies:
    - CAPRMEDIO_MODEL <+ Scope Unit.ID
    - CAPRMEDIO_MODEL <+ Scope Unit.Name
    - CAPRMEDIO_MODEL <+ Scope Unit.Label
    - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
    - CAPRMEDIO_MODEL <+ Scope Unit.order.number
    - CAPRMEDIO_MODEL <+ Scope Unit.Paths.Authority
    - CAPRMEDIO_MODEL <+ Scope Unit.Paths.Delivery
  tier: 1
state:
  status: archived
  version: 5
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-D-667@5-CORE_META_MODEL-POLICY--derive-authority-and-delivery-folder-names.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/099_archived
---


## Summary

Derive Authority and Delivery Folder Names

## Claim

### Prose Claim


The Project Authority Folder is `.caprmedio_<project name>`, without a Scope Unit ID.

For a non-root Scope Unit, derive the folder names from its ID, Label, order.number and Name:

| Scope Unit | Authority Folder name | Delivery Folder name |
| --- | --- | --- |
| Ordered | `<id>_<label>_<order>_<name>` | `<label>_<order>_<name>` |
| Unordered | `<id>_<label>_<name>` | `<label>_<name>` |

`<id>` is the stable Scope Unit ID. `<order>` is `order.number`. For an Unordered unit, omit the order segment and its separator. When Label is absent, omit its segment and separator.

Place each non-root folder under its respective parent's folder. Resolve `Scope Unit.Paths.Authority` and `Scope Unit.Paths.Delivery` from their respective folder trees relative to the Project root. Do not maintain the derived folder paths as independent values in Scope Unit Declarations.

Derived paths are readability and placement values, not another structural source. Conflicting derivations remain unresolved and are reported; do not automatically choose a new Name, parent, number or binding. Do not author Structural Coordinate.
