---
subjects:
  active: Carrier/Directory
  passive:
  - Entity
  - Carrier
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-451
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-451-CORE_META_MODEL-ENG_DECISION--classify-folders-by-their-carrier-responsibility.md
  source_atom_id: CA-D-451
  source_atom_revision: 21
  source_sha256: a0718542d594b55073de80556cf938d6e7e16dd768f6532512ed1a20b3938049
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Classify folders by their Carrier responsibility

## Claim scope

filesystem folders that carry or place Project artifacts.

## Claim

a filesystem folder **must** be classified as a Directory Carrier **only** **when** it carries a Structural Entity under CA-D-263.

- a folder's visibility **in** a graph **or** its containment of files does **not** itself establish that binding.
- administrative Content Role directories **and** Status subdirectories provide Carrier placement, **not** separate Structural Entities **or** Directory Carriers. Status placement remains governed by CA-D-295 **and** CA-D-352.
