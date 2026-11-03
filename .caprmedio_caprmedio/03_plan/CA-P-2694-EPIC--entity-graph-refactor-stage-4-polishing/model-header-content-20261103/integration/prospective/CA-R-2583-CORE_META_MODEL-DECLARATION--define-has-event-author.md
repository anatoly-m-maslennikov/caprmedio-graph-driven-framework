---
atom_id: CA-R-2583
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_EVENT_AUTHOR
version: 5
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2583-CORE_META_MODEL-DECLARATION--define-has-event-author.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define HAS_EVENT_AUTHOR

## Claim

### Formal Claim

```CFEL
Event Record// ((HAS_EVENT_AUTHOR)) Actor//;
Relation//HAS_EVENT_AUTHOR ((HAS_INVERSE)) Relation//IS_EVENT_AUTHOR_OF;

Relation//HAS_EVENT_AUTHOR ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

HAS_EVENT_AUTHOR identifies the Actor who performed the recorded event.

Forward `Host ((HAS_EVENT_AUTHOR)) Target` and reverse `Target <((HAS_EVENT_AUTHOR)) Host` are views of the same Relation fact.
HAS_EVENT_AUTHOR relates Event Record instance to Actor instance.
