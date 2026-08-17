---
subject_scopes:
  - principles
tier: principle
principle_order: 7
version: 6
updated_at: 2026-08-17 22:22:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-GOAL-001--enable-any-operator-to-build-a-working-system
---
# Apply dry across CAPRMADIO

CAPRMADIO must store and maintain a governed meaning under one canonical owner whenever that owner can resolve the meaning completely and unambiguously; every other use must reference, derive, generate, or adapt that owner.

This rule applies across semantics, requirements, methods, assurance definitions, delivery rules, implementation, Ops, identities, schemas, settings, mappings, documentation, tools, skills, tests, evaluations, and generated views. Similar text or code with different meanings or ownership boundaries is not duplication and must not be forced into one abstraction.

A duplicate representation is permitted only when an explicit Requirement makes a materialized copy necessary for an external contract, portability, performance, availability, audit snapshot, or independently usable publication. The copy is non-authoritative, identifies its canonical source, and has a deterministic regeneration or reconciliation rule appropriate to its use.
