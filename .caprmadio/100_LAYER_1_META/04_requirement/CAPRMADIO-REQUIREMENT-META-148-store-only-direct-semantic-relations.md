---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-148
scope_path: layer:meta
subject_scopes:
  - artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-121-bind-traceability-to-exact-claims-and-revisions
---

# Store only direct semantic relations

An Atom stores a relation only when that relation expresses a direct semantic dependency, explanation, realization, assurance, evidence, resolution, replacement, or other registered meaning between the two endpoints.

CAPRMADIO derives transitive lineage and reachability from chains of direct relations instead of copying every ancestor relation into every descendant.

Persisted relations represent direct semantic edges; transitive lineage is derived.
