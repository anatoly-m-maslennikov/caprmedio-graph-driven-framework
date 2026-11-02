---
atom_id: CA-R-2583
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//HAS_EVENT_AUTHOR
version: 4
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
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

