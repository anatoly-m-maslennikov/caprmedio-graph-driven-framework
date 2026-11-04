---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/Directory
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
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
  source_sha256: 43cb7576a8d7e461bad20aea937a8a6afbe20e93b2493af0697bd79afe9defb6
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Classify folders by their Carrier responsibility

## Claim

### Prose Claim


filesystem folders that carry or place Project artifacts.


a filesystem folder **must** be classified as a Directory Carrier **only** **when** it carries a Structural Entity under CA-D-263.

- a folder's visibility **in** a graph **or** its containment of files does **not** itself establish that binding.
- administrative Content Role directories **and** Status subdirectories provide Carrier placement, **not** separate Structural Entities **or** Directory Carriers. Status placement remains governed by CA-D-295 **and** CA-D-352.
