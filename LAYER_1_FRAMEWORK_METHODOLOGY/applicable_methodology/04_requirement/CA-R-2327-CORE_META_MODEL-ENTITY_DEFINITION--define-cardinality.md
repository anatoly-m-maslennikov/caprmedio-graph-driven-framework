---
atom_id: CA-R-2327
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Cardinality
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2327-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality.md
  source_atom_id: CA-R-2327
  source_atom_revision: 6
  source_sha256: 453ef31f76dccc8b2ba1c08f83028c33d1b08d08420c5653b5e7d51ff1f9ac5b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Cardinality

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Cardinality
```

### Prose Claim


Cardinality is CFEL syntax for expressing the allowed number of direct values,
dependent Properties, Relation instances or contained parts.



The forms are `{:n}`, `{:n+}` and `{:n..m}` with non-negative integer bounds.

