---
atom_id: CA-R-2252
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/decimal
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2252-CORE_META_MODEL-ENTITY_DEFINITION--define-decimal-value-format.md
  source_atom_id: CA-R-2252
  source_atom_revision: 6
  source_sha256: 6832355d4bd3bbe58190783047f85ee726a5eecbae54bcda7296455dc6eb95e4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define decimal Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/decimal
```

### Prose Claim


The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.



## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
Property value.
