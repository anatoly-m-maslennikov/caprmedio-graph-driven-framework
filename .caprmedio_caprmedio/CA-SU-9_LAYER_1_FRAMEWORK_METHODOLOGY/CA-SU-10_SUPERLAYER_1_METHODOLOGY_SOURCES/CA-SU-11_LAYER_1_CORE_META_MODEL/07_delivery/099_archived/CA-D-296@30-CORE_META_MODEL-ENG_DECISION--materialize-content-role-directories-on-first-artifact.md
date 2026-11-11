---
atom_id: CA-D-296
ref_id: CA-D-296@30
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 3
status: Archived
version: 30
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-296@30-CORE_META_MODEL-ENG_DECISION--materialize-content-role-directories-on-first-artifact.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Materialize Content Role Directories on First Artifact

## Claim

### Prose Claim


administrative Content Role directories in Scope Units.


a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

## Details

an absent Content Role directory **must** represent empty role placement, **not** an absent Scope Unit. this administrative directory does **not** itself carry a Structural Entity **or** become a Directory Carrier under CA-D-451. this materialization condition does **not** require deletion of an existing empty directory.
