---
atom_id: CA-D-296
ref_id: CA-D-296@32
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
status: Archived
version: 32
updated_at: '2026-11-11T18:45:40+04:00'
carrier_destination:
  file:
    name: CA-D-296@32-CORE_META_MODEL-FILE_LAYOUT--materialize-content-role-directories-on-first-artifact.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Materialize Content Role Directories on First Artifact

## Claim

### Prose Claim

Within a Scope Unit, derive the Atom's Role folder from `Header.Context.Role`. Create the folder when the first Atom needs it. Role folders organize files within their Scope Unit.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role := Concern).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/01_concern/<placement>");
Atom/(.Header.Context.Role := Analysis and Advisory).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/02_analysis/<placement>");
Atom/(.Header.Context.Role := Plan).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/03_plan/<placement>");
Atom/(.Header.Context.Role := Requirement).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/04_requirement/<placement>");
Atom/(.Header.Context.Role := Method).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/05_method/<placement>");
Atom/(.Header.Context.Role := Evaluation).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/06_evaluation/<placement>");
Atom/(.Header.Context.Role := Delivery).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/07_delivery/<placement>");
Atom/(.Header.Context.Role := Operations).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/09_operations/<placement>");
```
