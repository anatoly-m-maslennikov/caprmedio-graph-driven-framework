---
atom_id: CA-R-2618
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_ACTIVE_SUBJECT
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare HAS_ACTIVE_SUBJECT

## Claim

HAS_ACTIVE_SUBJECT links an Atom to the thing or topic named by its active Subject. Its value is derived from subjects.active; it is a canonical Relation, not a derived view of another Relation. A Declaration addresses a Node; other Atoms are not restricted to the Node branch.

```CFEL
Atom/(.Role: Requirement)/(.Form: Declaration)// ((HAS_ACTIVE_SUBJECT)) (Node, Node.**);

((HAS_ACTIVE_SUBJECT)) >| Derivation == Direct;

Atom// ((HAS_ACTIVE_SUBJECT)) $active_subject
```

## Semantics



The Target is the thing or topic named by subjects.active; for a Declaration it is a Node, while other Atoms may name non-Node entities.
Forward `Host ((HAS_ACTIVE_SUBJECT)) Target` and reverse `Target <((HAS_ACTIVE_SUBJECT)) Host` are views of the same Relation fact.
HAS_ACTIVE_SUBJECT relates Atom to its active Subject target. It is canonical even though its value is obtained from subjects.active.

