---
atom_id: CA-R-2249
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Format/bool
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Format
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2249-CORE_META_MODEL-ENTITY_DEFINITION--define-bool-value-format.md
  source_atom_id: CA-R-2249
  source_atom_revision: 5
  source_sha256: 2295372b6cd2cb94093f349ac9edf204c2ff779846d9bafd3f16d2a197cbd540
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define bool Value Format

## Claim

The bool Value Format admits the Boolean values true and false. It does not set a
property's cardinality, default, nullability, or carrier representation.


```CFEL
CFEL <+ Format/bool
```

## Semantics

bool is the value domain selected by a `[bool]` annotation on one direct
Property value.
