---
atom_id: CA-R-1958
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier
relations:
  child_of:
  - CA-R-1174
version: 15
updated_at: 2026-11-02 00:18:22 +0400
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1958-CORE_META_MODEL--define-entity-carrier.md
  source_atom_id: CA-R-1958
  source_atom_revision: 15
  source_sha256: bf30005579aeaf1cee907c1ea68d007c2ac7ca83c6bde312049550a76ce3c9d9
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define Entity/Carrier

## Claim scope

Carrier representations of Continuants.

## Claim

A Carrier **means** a storage representation of a Continuant, distinct from what it represents. A Carrier can represent a record of an Occurrent, **not** the Occurrent itself.

### Formal claim

```text
Carrier.ID[string]{1}
Carrier.Canonical Address[string]{1}
Carrier.Format[string]{1}
```

For implementation_of, the direct owner is the governed Implementation Carrier and each tuple targets the specification Atom it implements. For evidence_for, the direct owner is the evidence Carrier and each tuple targets the Evaluation or Implementation Carrier it supports. These are endpoint permissions, not extra fields on reusable Relation Types or additional storage facts for their derived inverses.
