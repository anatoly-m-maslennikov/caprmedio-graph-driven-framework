---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-20 19:41:00
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-META-REQU-121--store-only-direct-semantic-relations
---
# Register complete relation-kind metadata

GOV must expose one canonical registry entry for every admitted semantic relation kind. Each entry declares the authored direct name, derived inverse name, persisted owner and direction, upstream endpoint, allowed source and target classes, cardinality, authority effect, transitivity, symmetry, applicable authority modes, lifecycle status, and exclusive meaning. Only the direct form is authored; inverse navigation is derived. Direct and inverse names must be unique, and any missing, duplicate, or ambiguous entry makes the relation unavailable to deterministic Tools.
