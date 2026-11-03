---
atom_id: CA-R-2254
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Format/datetime
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Format
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2254-CORE_META_MODEL-ENTITY_DEFINITION--define-datetime-value-format.md
  source_atom_id: CA-R-2254
  source_atom_revision: 5
  source_sha256: f7ecfc1db1895c3afb45c7c30bca943b162094b8fb403d5b38085efbc10b2313
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define datetime Value Format

## Claim

The datetime Value Format admits date-and-time values. It does not set a
timezone convention, precision, cardinality, uniqueness, or carrier
representation.


```CFEL
CFEL <+ Format/datetime
```

## Semantics

datetime is the value domain selected by a `[datetime]` annotation on one
direct Property value.
