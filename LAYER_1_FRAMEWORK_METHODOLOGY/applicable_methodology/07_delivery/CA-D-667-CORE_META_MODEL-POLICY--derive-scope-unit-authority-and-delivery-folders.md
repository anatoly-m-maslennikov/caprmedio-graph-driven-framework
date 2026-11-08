---
atom_id: CA-D-667
ref_id: CA-D-667
role: Delivery
form: Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.ID
  - CAPRMEDIO_MODEL <+ Scope Unit.Name
  - CAPRMEDIO_MODEL <+ Scope Unit.Label
  - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO_MODEL <+ Scope Unit.order.number
tier: 1
status: Active
version: 4
updated_at: "2026-11-07 15:28:42 +0400"
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-667-CORE_META_MODEL-POLICY--derive-scope-unit-authority-and-delivery-folders.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-667-CORE_META_MODEL-POLICY--derive-scope-unit-authority-and-delivery-folders.md
  source_atom_id: CA-D-667
  source_atom_revision: 4
  source_sha256: 6c91eaec3d94914427727552b9a54bff1741a8888217e33428e656cc9cd12b0b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

Place each non-root folder under its respective parent's folder. Do not maintain the derived folder paths as independent values in the Project Scope Unit Declaration or non-Project Scope Delegations.

Derived paths are readability and placement values, not another structural source. Conflicting derivations remain unresolved and are reported; do not automatically choose a new Name, parent, number or binding. Do not author Structural Level or Structural Coordinate.
