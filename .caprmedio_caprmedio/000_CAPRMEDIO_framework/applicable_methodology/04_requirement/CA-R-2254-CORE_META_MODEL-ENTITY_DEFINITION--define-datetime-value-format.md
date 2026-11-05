---
atom_id: CA-R-2254
ref_id: CA-R-2254
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/datetime
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: Active
version: 6
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2254-CORE_META_MODEL-DECLARATION--define-datetime-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2254-CORE_META_MODEL-ENTITY_DEFINITION--define-datetime-value-format.md
  source_atom_id: CA-R-2254
  source_atom_revision: 6
  source_sha256: dc360443a3096fcf50e383362023c84e021c482f22fa60ef5f7d8a11565f3793
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define datetime Value Format

## Claim

### Prose Claim


The datetime Value Format admits date-and-time values. It does not set a
timezone convention, precision, cardinality, uniqueness, or carrier
representation.



### Formal Claim

```CFEL
# model
CFEL <+ Format/datetime
```

## Semantics

datetime is the value domain selected by a `[datetime]` annotation on one
direct Property value.
