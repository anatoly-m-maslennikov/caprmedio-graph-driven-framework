---
atom_id: CA-R-2249
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2249-CORE_META_MODEL-ENTITY_DEFINITION--define-bool-value-format.md
  source_atom_id: CA-R-2249
  source_atom_revision: 6
  source_sha256: 33e794ab91eb7360c879421930581fc5b5e5ce04ed0287d8b77eef704e3db5fd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define bool Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/bool
```

### Prose Claim


The bool Value Format admits the Boolean values true and false. It does not set a
property's cardinality, default, nullability, or carrier representation.



## Semantics

bool is the value domain selected by a `[bool]` annotation on one direct
Property value.
