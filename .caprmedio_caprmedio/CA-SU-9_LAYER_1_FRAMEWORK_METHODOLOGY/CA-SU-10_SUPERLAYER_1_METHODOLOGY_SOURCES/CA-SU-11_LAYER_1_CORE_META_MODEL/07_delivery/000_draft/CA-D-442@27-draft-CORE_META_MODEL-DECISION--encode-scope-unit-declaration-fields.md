---
atom_id: CA-D-442
ref_id: CA-D-442@27-draft
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Draft
version: 27
updated_at: 2026-11-05 12:58:42 +0400
carrier_destination:
  file:
    name: CA-D-442@27-draft-DECISION--encode-scope-unit-declaration-fields.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/000_draft
---
## Summary

Encode Scope Unit declaration fields

## Claim

### Prose Claim


Carry a Scope Unit Declaration as a Markdown Atom. Its frontmatter carries Role = Requirement, Form = Scope Unit Declaration and the specific Scope Unit as `subjects.active`. Its Claim carries the declared structural facts in CFEL.

The shared Scope Unit model supplies field formats and cardinalities. Project inherits its unordered state and absence of order.number from the Project model. Folder names are derived by the shared Delivery Policy; they are not authored in a Declaration.
