---
atom_id: CA-R-2557
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Event Record
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2557-CORE_META_MODEL-DECLARATION--declare-event-record.md
  source_atom_id: CA-R-2557
  source_atom_revision: 4
  source_sha256: 9bffebb01a7a74b77241a7e3c9e906dd6c94c2c44c4870d3b6ce95611f9fd560
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record

## Claim

An Event Record is immutable.

```CFEL
Event Record {:0}((IS_PROPERTY_OF));
Event Record ((NARROWER_THAN)) @Continuant;
Event Record// {:1}((IS_CONTAINED_BY)) Journal//
```

## Semantics

An Event Record is a persistent description of an event and its recorded evidence.
