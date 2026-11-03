---
atom_id: CA-R-2618
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//HAS_ACTIVE_SUBJECT
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2618-CORE_META_MODEL-DECLARATION--declare-has-active-subject.md
  source_atom_id: CA-R-2618
  source_atom_revision: 1
  source_sha256: e7a39d02d9b7d866e79624602754c192095bdb923ee95f19e4870bd032c3c902
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

