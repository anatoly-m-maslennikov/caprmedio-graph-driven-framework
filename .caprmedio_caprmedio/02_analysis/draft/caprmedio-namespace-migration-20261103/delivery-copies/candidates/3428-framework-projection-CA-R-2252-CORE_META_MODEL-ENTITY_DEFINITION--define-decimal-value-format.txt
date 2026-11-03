---
atom_id: CA-R-2252
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Format/decimal
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Format
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2252-CORE_META_MODEL-ENTITY_DEFINITION--define-decimal-value-format.md
  source_atom_id: CA-R-2252
  source_atom_revision: 5
  source_sha256: 0bbc45ea878bf5cf86f564be177dad8783f17eeb99d878cc4ab02684ecf2478b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define decimal Value Format

## Claim

The decimal Value Format admits decimal numeric values. It does not set scale,
precision, a numeric range, cardinality, uniqueness, or carrier
representation.


```CFEL
CFEL <+ Format/decimal
```

## Semantics

decimal is the value domain selected by a `[decimal]` annotation on one direct
Property value.
