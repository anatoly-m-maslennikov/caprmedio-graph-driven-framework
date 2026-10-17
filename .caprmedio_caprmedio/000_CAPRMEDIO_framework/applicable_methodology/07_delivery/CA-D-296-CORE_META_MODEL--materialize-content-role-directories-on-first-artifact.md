---
subjects:
  governs: "Entity/Carrier.Canonical Address"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom", "Entity/Carrier/Directory Carrier"]
version: 16
updated_at: "2026-10-16 12:09:15 +0000"
relations: {}
atom_id: "CA-D-296"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-296-CORE_META_MODEL--materialize-content-role-directories-on-first-artifact.md
  source_atom_id: CA-D-296
  source_atom_revision: 16
  source_sha256: e4ebce2d700d79b2eee8b83d2128dadf1ac26d9e859fe51f6d9941d3e542339a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Materialize Content Role Directories on First Artifact

## Scope

administrative Content Role directories in Scope Units.

## Claim

a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

## Details

an absent Content Role directory **must** represent empty role placement, **not** an absent Scope Unit. this administrative directory does **not** itself carry a Structural Entity **or** become a Directory Carrier under CA-D-451. this materialization condition does **not** require deletion of an existing empty directory.
