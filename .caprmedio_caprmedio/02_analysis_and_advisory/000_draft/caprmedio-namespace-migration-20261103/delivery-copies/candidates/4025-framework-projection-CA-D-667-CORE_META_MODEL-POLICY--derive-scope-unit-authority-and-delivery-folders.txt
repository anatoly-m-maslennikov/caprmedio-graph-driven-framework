---
atom_id: CA-D-667
role: Delivery
form: Policy
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/Directory.Name
  passive:
  - CAPRMEDIO <+ MODEL <+ Scope Unit.ID
  - CAPRMEDIO <+ MODEL <+ Scope Unit.Name
  - CAPRMEDIO <+ MODEL <+ Scope Unit.Label
  - CAPRMEDIO <+ MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO <+ MODEL <+ Scope Unit.order.number
relations: {}
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-667-CORE_META_MODEL-POLICY--derive-scope-unit-authority-and-delivery-folders.md
  source_atom_id: CA-D-667
  source_atom_revision: 1
  source_sha256: c9a4109bf686586a54cd1058570be4078268f1ea365428d44c996b81437076c9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Derive Authority and Delivery Folder Names

## Claim

The Project Authority Folder is `.caprmedio_<project name>`, without a Scope Unit ID.

For a non-root Scope Unit, derive the folder names from its ID, Label, order.number and Name:

| Scope Unit | Authority Folder name | Delivery Folder name |
| --- | --- | --- |
| Ordered | `<id>_<label>_<order>_<name>` | `<label>_<order>_<name>` |
| Unordered | `<id>_<label>_<name>` | `<label>_<name>` |

`<id>` is the stable Scope Unit ID. `<order>` is `order.number`. For an Unordered unit, omit the order segment and its separator. When Label is absent, omit its segment and separator.

Place each non-root folder under its respective parent's folder. Do not maintain the derived folder paths as independent values in Scope Unit Declarations.

Derived paths are readability and placement values, not another structural source. Conflicting derivations remain unresolved and are reported; do not automatically choose a new Name, parent, number or binding. Do not author Structural Level or Structural Coordinate.
