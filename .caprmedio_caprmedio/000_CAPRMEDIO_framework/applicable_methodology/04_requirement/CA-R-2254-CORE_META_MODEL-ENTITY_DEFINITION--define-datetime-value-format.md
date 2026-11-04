---
atom_id: CA-R-2254
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format/datetime
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2254-CORE_META_MODEL-ENTITY_DEFINITION--define-datetime-value-format.md
  source_atom_id: CA-R-2254
  source_atom_revision: 6
  source_sha256: 410e95f24f10b861c13981c9906c0f9e172b46d4ea6de4a041c6cca71b2a3bdf
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define datetime Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/datetime
```

### Prose Claim


The datetime Value Format admits date-and-time values. It does not set a
timezone convention, precision, cardinality, uniqueness, or carrier
representation.



## Semantics

datetime is the value domain selected by a `[datetime]` annotation on one
direct Property value.
