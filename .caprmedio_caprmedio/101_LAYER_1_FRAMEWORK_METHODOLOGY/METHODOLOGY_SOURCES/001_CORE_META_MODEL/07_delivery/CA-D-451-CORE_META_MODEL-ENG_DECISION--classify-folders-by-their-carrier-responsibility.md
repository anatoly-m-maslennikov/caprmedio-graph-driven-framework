---
subjects:
  governs: Subject/CAPRMEDIO/Carrier/Directory
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
version: 17
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-451
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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
