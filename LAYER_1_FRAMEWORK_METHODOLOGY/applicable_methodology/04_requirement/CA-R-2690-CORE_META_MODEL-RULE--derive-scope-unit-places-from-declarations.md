---
atom_id: CA-R-2690
ref_id: CA-R-2690
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/Directory
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2690-CORE_META_MODEL-RULE--derive-scope-unit-places-from-declarations.md
  source_atom_id: CA-R-2690
  source_atom_revision: 1
  source_sha256: a763b80b48f53df2ed3e3740dcf2b623eb7727673307ceea62c777c2b73a97bd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Derive Scope Unit places from Declarations

## Claim

Each non-Project Scope Unit has Authority and Delivery folders derived from its Scope Unit Declaration. Delivery Atoms govern representation, placement, and general Carrier conventions without repeating a unit's selected paths.
