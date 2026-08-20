---
subject_scopes:
  - relation-model
version: 2
updated_at: 2026-08-20 19:53:00
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register complete relation-kind metadata

GOV must expose exactly one canonical machine-readable Atom relation-type dictionary with one row per admitted direct relation. Each row declares the direct name, its derived inverse name, allowed direct-source and direct-target lifecycle states, persisted owner and direction, upstream endpoint, allowed source and target classes, cardinality, authority effect, transitivity, symmetry, applicable authority modes, status, and exclusive meaning. Atom carriers may author only direct names; every inverse typed relation is derived and must never be stored. Direct names and inverse names are each unique, no inverse name may also be admitted as a direct name, and any missing, duplicate, or ambiguous row makes the relation unavailable to deterministic Tools.
