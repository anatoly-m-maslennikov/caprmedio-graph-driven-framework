---
subjects:
  governs: Subject/CAPRMEDIO/Carrier.Canonical Address
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier/Directory
version: 26
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
atom_id: CA-D-296
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Materialize Content Role Directories on First Artifact

## Scope

administrative Content Role directories in Scope Units.

## Claim

a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

## Details

an absent Content Role directory **must** represent empty role placement, **not** an absent Scope Unit. this administrative directory does **not** itself carry a Structural Entity **or** become a Directory Carrier under CA-D-451. this materialization condition does **not** require deletion of an existing empty directory.
