---
subjects:
  governs: "Entity/Carrier/Directory Carrier"
  depends_on:
    ["Structural Entity", "Artifact Carrier Placement", "Atom/Content Role"]
version: 6
updated_at: "2026-10-15 18:52:03 +0000"
relations: {}
atom_id: "CA-D-451"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-451-CORE_META_MODEL-STANDARD--classify-folders-by-their-carrier-responsibility.md
  source_atom_id: CA-D-451
  source_atom_revision: 6
  source_sha256: 131cbe8e391ab6e76f92d1d8f4f3dade5396f84c7d2c63a5ee9e4256dd60f7ba
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Classify folders by their Carrier responsibility

## Scope

filesystem folders that carry or place Project artifacts.

## Claim

a filesystem folder **must** be classified as a Directory Carrier **only** **when** it carries a Structural Entity under CA-D-263.

- a folder's visibility **in** a graph **or** its containment of files does **not** itself establish that binding.
- administrative Content Role directories **and** Status subdirectories provide Carrier placement, **not** separate Structural Entities **or** Directory Carriers. Status placement remains governed by CA-D-295 **and** CA-D-352.

## Details
