---
atom_id: CA-D-442
ref_id: CA-D-442
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 29
updated_at: "2026-11-07 15:18:44 +0400"
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-442-CORE_META_MODEL-DECISION--encode-scope-unit-declaration-fields.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-442-CORE_META_MODEL-DECISION--encode-scope-unit-declaration-fields.md
  source_atom_id: CA-D-442
  source_atom_revision: 29
  source_sha256: 3096db5d7f7cce4545311a4e03681dbe04537360b7663e8eefba8c24777f9bca
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Encode Scope Unit declaration fields

## Claim

### Prose Claim

Carry a Scope Unit’s structural declaration as a Markdown Atom:

- Project: Role Requirement, Form Scope Unit Declaration.
- Non-Project Scope Unit within the Project: Form Scope Delegation, with the assigned contribution’s Role.

Header.Topics.Main Subject identifies the declared Scope Unit. The Claim carries its declared structural facts in CFEL where expressible.

The shared model supplies field formats and cardinalities. Project inherits its unordered state and absence of order.number. Every Scope Unit has one stable ID. Folder names follow the shared Delivery Policy.
