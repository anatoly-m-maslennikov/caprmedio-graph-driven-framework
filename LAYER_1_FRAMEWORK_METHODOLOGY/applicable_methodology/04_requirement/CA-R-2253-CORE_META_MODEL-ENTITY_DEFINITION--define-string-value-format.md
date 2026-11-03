---
atom_id: CA-R-2253
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format/string
  passive:
  - CFEL <+ Format
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2253-CORE_META_MODEL-ENTITY_DEFINITION--define-string-value-format.md
  source_atom_id: CA-R-2253
  source_atom_revision: 5
  source_sha256: 16a51b7018b87bfe934fd4fa4d2365ad3ec67be12e5846d5aa9bfc5d704c23c0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define string Value Format

## Claim

The string Value Format admits textual string values. It does not turn null
into a string or set a property's cardinality, uniqueness, or carrier
representation.


```CFEL
CFEL <+ Format/string
```

## Semantics

string is the value domain selected by a `[string]` annotation on one direct
Property value.
