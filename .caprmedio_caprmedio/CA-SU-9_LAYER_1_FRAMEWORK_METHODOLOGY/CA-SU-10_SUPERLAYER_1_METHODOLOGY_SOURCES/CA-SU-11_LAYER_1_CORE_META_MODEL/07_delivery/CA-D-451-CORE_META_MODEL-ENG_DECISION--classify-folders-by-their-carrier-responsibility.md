---
atom_id: CA-D-451
ref_id: CA-D-451
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
tier: 3
status: Active
version: 21
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-451-CORE_META_MODEL-DECISION--classify-folders-by-their-carrier-responsibility.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Classify folders by their Carrier responsibility

## Claim

### Prose Claim


filesystem folders that carry or place Project artifacts.


a filesystem folder **must** be classified as a Directory Carrier **only** **when** it carries a Structural Entity under CA-D-263.

- a folder's visibility **in** a graph **or** its containment of files does **not** itself establish that binding.
- administrative Content Role directories **and** Status subdirectories provide Carrier placement, **not** separate Structural Entities **or** Directory Carriers. Status placement remains governed by CA-D-295 **and** CA-D-352.
