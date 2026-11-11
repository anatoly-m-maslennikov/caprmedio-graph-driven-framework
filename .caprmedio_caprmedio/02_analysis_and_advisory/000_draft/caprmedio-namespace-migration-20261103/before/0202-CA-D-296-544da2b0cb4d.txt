---
subjects:
  active: Carrier.Canonical Address
  passive:
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Scope Unit
  - Atom
  - Carrier/Directory
version: 29
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-296
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Materialize Content Role Directories on First Artifact

## Claim scope

administrative Content Role directories in Scope Units.

## Claim

a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

## Details

an absent Content Role directory **must** represent empty role placement, **not** an absent Scope Unit. this administrative directory does **not** itself carry a Structural Entity **or** become a Directory Carrier under CA-D-451. this materialization condition does **not** require deletion of an existing empty directory.
