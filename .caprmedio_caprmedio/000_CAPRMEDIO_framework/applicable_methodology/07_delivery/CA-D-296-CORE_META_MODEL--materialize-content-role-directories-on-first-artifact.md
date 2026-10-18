---
subjects:
  governs: "Entity/Carrier.Canonical Address"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role", "Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Atom", "Entity/Carrier/Directory Carrier"]
version: 17
updated_at: "2026-10-18 03:34:35 +0400"
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
  source_atom_revision: 17
  source_sha256: f0bf6bfd53b4e6c430d21fb41e4e07961a26aee7554ad915ce7897c4032f0aa1
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
