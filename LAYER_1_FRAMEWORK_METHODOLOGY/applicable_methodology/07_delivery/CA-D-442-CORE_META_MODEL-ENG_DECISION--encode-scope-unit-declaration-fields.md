---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Scope Unit
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 26
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
atom_id: CA-D-442
form: Decision
status: Active
tier: 3
role: Delivery
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-442-CORE_META_MODEL-ENG_DECISION--encode-scope-unit-declaration-fields.md
  source_atom_id: CA-D-442
  source_atom_revision: 26
  source_sha256: ce2f0f7523dde5f5060778d99b7664d09fd681abb280d6c612027559a22db2a4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Encode Scope Unit declaration fields

## Claim

Carry a Scope Unit Declaration as a Markdown Atom. Its frontmatter carries Role = Requirement, Form = Scope Unit Declaration and the specific Scope Unit as `subjects.active`. Its Claim carries the declared structural facts in CFEL.

The shared Scope Unit model supplies field formats and cardinalities. Project inherits its unordered state and absence of order.number and Scope Unit ID from the Project model. Folder names are derived by the shared Delivery Policy; they are not authored in a Declaration.
