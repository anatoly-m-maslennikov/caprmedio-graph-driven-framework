---
atom_id: CA-R-2583
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_EVENT_AUTHOR
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2583-CORE_META_MODEL-DECLARATION--define-has-event-author.md
  source_atom_id: CA-R-2583
  source_atom_revision: 4
  source_sha256: 2e17480eea852f5b79117725f73109d702f48acad2a10c9a8c02cbae5cfdc71c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define HAS_EVENT_AUTHOR

## Claim

HAS_EVENT_AUTHOR identifies the Actor who performed the recorded event.

```CFEL
Event Record// ((HAS_EVENT_AUTHOR)) Actor//;
((HAS_EVENT_AUTHOR)) ((HAS_INVERSE)) ((IS_EVENT_AUTHOR_OF));

((HAS_EVENT_AUTHOR)) >| Derivation == Direct
```

## Semantics


Forward `Host ((HAS_EVENT_AUTHOR)) Target` and reverse `Target <((HAS_EVENT_AUTHOR)) Host` are views of the same Relation fact.
HAS_EVENT_AUTHOR relates Event Record instance to Actor instance.

