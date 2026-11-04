---
atom_id: CA-R-2253
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/string
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2253-CORE_META_MODEL-ENTITY_DEFINITION--define-string-value-format.md
  source_atom_id: CA-R-2253
  source_atom_revision: 6
  source_sha256: f5c86c8e98ef8fc92f822c8dad2c4824577f51d4b38c4f257774f3d5c9efaece
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define string Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/string
```

### Prose Claim


The string Value Format admits textual string values. It does not turn null
into a string or set a property's cardinality, uniqueness, or carrier
representation.



## Semantics

string is the value domain selected by a `[string]` annotation on one direct
Property value.
