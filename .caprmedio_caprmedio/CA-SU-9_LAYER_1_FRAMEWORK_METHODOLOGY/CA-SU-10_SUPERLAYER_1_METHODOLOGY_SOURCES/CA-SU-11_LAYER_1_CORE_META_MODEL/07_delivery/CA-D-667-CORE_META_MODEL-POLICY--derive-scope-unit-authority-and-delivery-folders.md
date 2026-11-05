---
atom_id: CA-D-667
ref_id: CA-D-667
role: Delivery
form: Policy
status: Active
version: 2
updated_at: 2026-11-03 23:25:51 +0400
tier: 1
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.ID
  - CAPRMEDIO_MODEL <+ Scope Unit.Name
  - CAPRMEDIO_MODEL <+ Scope Unit.Label
  - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO_MODEL <+ Scope Unit.order.number
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

Place each non-root folder under its respective parent's folder. Do not maintain the derived folder paths as independent values in Scope Unit Declarations.

Derived paths are readability and placement values, not another structural source. Conflicting derivations remain unresolved and are reported; do not automatically choose a new Name, parent, number or binding. Do not author Structural Level or Structural Coordinate.
