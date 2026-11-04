---
atom_id: CA-R-2250
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/int
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2250-CORE_META_MODEL-ENTITY_DEFINITION--define-int-value-format.md
  source_atom_id: CA-R-2250
  source_atom_revision: 6
  source_sha256: 8245418bdb1fc8dc4468bffe785f7090b5d4f46b2e2c30e0c06919e778ef1880
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define int Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/int
```

### Prose Claim


The int Value Format admits integer numeric values with no fractional part. It
does not set a numeric range, cardinality, uniqueness rule, or carrier
representation.



## Semantics

int is the value domain selected by an `[int]` annotation on one direct
Property value.
