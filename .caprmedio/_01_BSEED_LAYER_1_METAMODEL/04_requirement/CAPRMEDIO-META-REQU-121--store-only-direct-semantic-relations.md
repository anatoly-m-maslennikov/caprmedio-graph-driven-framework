---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-20 05:09:11
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-118--let-the-dependent-atom-own-the-relation
    - CAPRMEDIO-META-REQU-107--bind-traceability-to-exact-claims-and-revisions
---
# Store only direct semantic relations

An Atom stores a relation only when that relation expresses a direct semantic dependency, explanation, realization, evaluation, evidence, resolution, replacement, or other registered meaning between the two endpoints.

CAPRMEDIO derives transitive lineage and reachability from chains of direct relations instead of copying every ancestor relation into every descendant.

Persisted relations represent direct semantic edges; transitive lineage is derived.
