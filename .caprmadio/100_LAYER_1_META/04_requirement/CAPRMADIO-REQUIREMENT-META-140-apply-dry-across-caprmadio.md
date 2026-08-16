---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-140
scope_path: layer:meta
subject_scopes:
  - principles
tier: principle
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Apply DRY across CAPRMADIO

Whenever it is possible to resolve a governed meaning completely and unambiguously from one canonical owner, CAPRMADIO stores and maintains that meaning only once. Every other use references, derives, generates, or adapts the canonical owner instead of restating the same governed knowledge.

This rule applies across semantics, requirements, methods, assurance definitions, delivery rules, implementation, Ops, identities, schemas, settings, mappings, documentation, tools, skills, tests, evaluations, and generated views. Similar text or code with different meanings or ownership boundaries is not duplication and must not be forced into one abstraction.

A duplicate representation is permitted only when an explicit Requirement makes a materialized copy necessary for an external contract, portability, performance, availability, audit snapshot, or independently usable publication. The copy is non-authoritative, identifies its canonical source, and has a deterministic regeneration or reconciliation rule appropriate to its use.
