---
atom_id: CA-R-2557
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2557-CORE_META_MODEL-DECLARATION--declare-event-record.md
  source_atom_id: CA-R-2557
  source_atom_revision: 4
  source_sha256: 0357e59cb3366ebbb2e13d0ef139d29e8fd24a449729014686c438555e535dcb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Event Record

## Claim

### Formal Claim

```CFEL
# model
Event Record {:0}((IS_PROPERTY_OF));

Event Record ((NARROWER_THAN)) Continuant;

# instances
Event Record//$event_record {:1}((IS_CONTAINED_BY)) Journal//$journal
```

### Prose Claim


An Event Record is immutable.


## Semantics

An Event Record is a persistent description of an event and its recorded evidence.
